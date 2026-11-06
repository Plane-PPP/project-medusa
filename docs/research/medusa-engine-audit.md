# Аудит OpenYAMM для Project Medusa (фазы A–B)

Дата: 2026-11-06. Код: OpenYAMM `feature/minotaur-rebalance` @ `0c172ed` (он же исходная точка
`feature/project-medusa`). Ссылки `файл:строка` даны на этот коммит.

Уровни достоверности:
- **[код]** — установлено чтением исходников, не запускалось;
- **[проверено]** — проверено командой (указана);
- **[предположение]** — требует проверки.

Важное ограничение среды: на этой VM нет полного набора игровых ресурсов (sparse checkout, `assets_dev` ≈ 100 МБ из
нескольких ГБ, partial clone) и нет дисплея. Запуск игры здесь невозможен; игровые проверки выполняются на машине
пользователя. **[проверено]** `du -sh assets_dev`, `echo $DISPLAY`.

## 1. New Game: выбор Ruleset и континента

| Что | Где | Вывод |
|---|---|---|
| Экран | `game/ui/screens/NewGameScreen.{h,cpp}`, разметка `assets_dev/engine/ui/gameplay/continent_selection.yml` | Два этапа: `FlowStage::ContinentSelection` → `CharacterCreation` **[код]** |
| Вкладки RULESET | `NewGameScreen::drawRulesetSwitch` (`NewGameScreen.cpp:2265`), `drawSegmentedSwitch` | Вкладки строятся из списка `m_rulesets`: Standard + каждый пакет `engine/rulesets/<id>/ruleset.yml`, по алфавиту id (`RulesetDefinition.cpp:605`). Ширина вкладок равная, подпись ужимается под ширину. **[код]** |
| Карточки континентов | `NewGameScreen::drawContinentSelection` (`NewGameScreen.cpp:2631`), цикл по **жёстко заданным** ключам `enroth/antagarich/jadame` (`:2644`) | Карточки и их тексты зашиты в коде и YAML-разметке. Для Medusa нужна правка C++. **[код]** |
| Данные континентов | `assets_dev/engine/data_tables/character_selection.yml` (`new_game_continents`: id 1 Jadam, 2 Antagarich, 3 Enroth, 4 Between time) | Ruleset может заменить файл целиком (MAW так и делает: `rulesets/maw/ruleset.yml:230`) **[код]** |
| Стартовая карта | `GameApplication::resolveContinentStartDestination` (`GameApplication.cpp:10916`) | Берётся из `continent_settings.txt`, колонки «Death map 1» и X/Y/Z/Dir для id континента **[код]** |
| Запуск сессии | `GameApplication::startNewSessionFromCharacterCreation` (`GameApplication.cpp:11154`) | Активирует ruleset, сеет партию, грузит карту **[код]** |
| Правила MAW | `GameSession.cpp:363` | `MawRules` создаются **только** для `ruleset.id == "maw"`. Любой другой пакет играет по правилам Standard, а значит и со всеми изменениями Minotaur Rebalance (они в общем коде Standard). **[код]** |

### Дефект: новая игра не может начаться на indoor-карте

`startNewSessionFromCharacterCreation` после загрузки карты требует `m_pOutdoorPartyRuntime != nullptr`
(`GameApplication.cpp:11247`). Этот объект создаётся только в outdoor-ветке `initializeSelectedMapRuntime`
(`:8331`), а `shutdownRenderer` его сбрасывает (`:9931`). Значит, при стартовой BLV-карте функция вернётся в главное
меню. **[код]**, в игре не проверено. Минимальное исправление — проверять `m_pMapSceneRuntime`; это изменение движка,
кандидат в upstream.

## 2. Создание партии

- Кандидаты — строки `character_data.txt`, отмеченные «Available at start» (или все при `free_selection: true`),
  с расой из `race_class_availability` (`NewGameScreen::rebuildCandidates`, `NewGameScreen.cpp:858`). **[код]**
- Новая строка `character_data.txt` с `x` и расой Human (0) автоматически появится в списке лиц. Ruleset может
  добавить строку через `append`, не трогая таблицу движка. Прецедент: MAW-портрет 78 «Lich Troll 2»
  (`rulesets/maw/ruleset.yml:291-296`, `content/character_data.append.txt`). **[код]**
- Выбранное лицо сохраняется в персонаже: `portraitTextureName`, `portraitPictureId`, `characterDataId`
  (`game/maps/SaveGame.cpp:1404-1412`). Формат сохранений менять не нужно. **[код]**

## 3. Загрузка миров и карт

- Активный мир — один: `--world`, по умолчанию из настроек (`main.cpp:206, 366`). Манифест — `worlds/<id>/world.yml`
  (`game/content/ContentManifest.h`): старт, QBits, idRanges, tableContributions, экраны загрузки, музыка. **[код]**
- Каталоги `maps/events/textures` монтируются для **всех** папок `worlds/*` (`collectExistingWorldPackageRoots`,
  `AssetFileSystem.cpp:260`). **[код]**
- Но список миров жёстко задан в нескольких местах: `KnownWorldPackageIds = {"mm6","mm7","mm8"}`
  (`AssetFileSystem.cpp:119`) и определение владельца карты (`GameDataLoader.cpp:2463`). `activeWorldContinentId`
  знает только mm6/mm7/mm8 (`GameApplication.cpp:10894`). **[код]**
- Карты регистрируются строкой в общей `map_stats.txt`. Мир не может дописать туда строки, а ruleset может
  (`GameDataLoader.cpp:2456`, режимы override/append). **[код]**

Вывод: новый **мир** `worlds/medusa` потребует правок движка в нескольких местах. Новый **ruleset-пакет** работает на
существующих механизмах.

## 4. Портреты

| Вопрос | Ответ |
|---|---|
| Таблица лиц | `assets_dev/engine/data_tables/character_data.txt` (`CharacterDollTable.h`): тип куклы, класс, голос, пол, «Available at start», ресурсы тела, головы и рук, **префикс кадров лица** (`pc02-`), NPCPic, раса |
| Кадры | `<префикс>01` … `<префикс>56`, PNG в `engine/icons_x2/` (их читают меню и создание партии) плюс атлас `faces_<set>.oytex` и `faces_<set>.yml` для HUD; сборка `tools/cook_ui_textures.py` (нужен `build/game/openyamm_model_texture_cook`) |
| Размер | 118×158 px (×2 от оригинальных 59×79). **[проверено]** заголовки PNG `pc02-01.png`, `7pc05-01.png`, `faces_pc41.yml: frame_width 118, frame_height 158` |
| Имя кадра | `portraitTextureNameForTextureFrame` подменяет две последние цифры (`GameplayUiRuntime.cpp:265`) |
| Состояние → кадр | `PortraitId` (`game/tables/PortraitEnums.h`) → `portrait_frame_data.txt` (номер текстуры и тайминг; многокадровые последовательности: моргание, разговор, урон) → `resolvePortraitTextureName` (`GameplayUiRuntime.cpp:2509`) |
| Реакции | `face_animations.txt`: событие (убийство, урон, ловушка, торговля…) → список выражений `PortraitId`; `portrait_fx_events.txt` — эффекты поверх портрета |
| Dead / Eradicated | Общие картинки `DEAD` и `ERADCATE` для всех героев (`GameplayUiRuntime.cpp:2511-2519`): индивидуальный кадр смерти движок **не использует** |
| Голоса | `character_voices.txt`, `character_speech_events.txt`; голос выбирается при создании, можно взять существующий женский |

Полная таблица 56 кадров и приоритеты состояний — в `docs/design/portraits.md`.

## 5. Paperdoll

- Тип куклы (`doll_types.txt`): 0 человек-мужчина, 1 человек-женщина, 2 минотавр, 3 тролль, 4 гном, 5 дракон. По нему
  выбираются картинки брони и анкеры рук и оружия. **[код]**
- Тело, голова и руки задаются в строке `character_data.txt` (`pc02bod` 166×594, `pc02head`, `pc02LHd`…).
  **[проверено]** размер `pc02bod.png`.
- Для Medusa в v1 достаточно новой строки с `Paperdoll type = 1` и ресурсами тела существующей героини (например
  `pc02*`). Новая раса не нужна. Голова на кукле (`head`) — отдельная картинка: со старой головой лицо на кукле и
  портрет будут разными. Варианты: нарисовать одну картинку головы Medusa или временно оставить чужую.

## 6. Изоляция контента и состояния

| Данные | Хранение | Риск для Medusa |
|---|---|---|
| QBits | `Party::m_questBits` (`unordered_set<uint32_t>`, `Party.h:880`), без верхнего предела | Диапазон заявляется в `idRanges`. MAW занимает 10001–10099. Предлагается Medusa 20000–20999 |
| Ruleset игры | `SaveGame` хранит id и опции ruleset и версию схемы пакета (`SaveGame.cpp:5327`) | Сохранение Medusa загрузит пакет Medusa. Если пакета нет, загрузка откажет и текущая игра сохранится (`GameApplication.cpp:10485-10510`) |
| Сохранения Standard/MAW | Не меняются | Нет |
| Ошибка в `ruleset.yml` | `loadAvailableRulesets` возвращает ошибку на весь список | Сломанный пакет Medusa может убрать вкладки ruleset. Нужна проверка пакета тестом |
| Моды в релизной сборке | `mods/engine/...` и `mods/worlds/<id>/...` монтируются только для упакованных ресурсов (`AssetFileSystem.cpp:592, 1008`) | В разработке — симлинк в `assets_dev` (PhysFS симлинки разрешает, `AssetFileSystem.cpp:546`), в релизе — папка `mods/engine/rulesets/medusa` |

## 7. Архитектурная развилка: чем считать Medusa

| Вариант | Как | Правки C++ | Риск для Standard/MAW | Плюсы | Минусы |
|---|---|---|---|---|---|
| **A. Ruleset-пакет `medusa`** (рекомендуется) | `engine/rulesets/medusa/`: `ruleset.yml` без опций, замена `character_selection.yml` (один континент «Prologue»), строка `continent_settings` (старт), строки `character_data` (лицо), `map_stats` (свои карты) | Карточки стартов из `ruleset.yml` вместо трёх зашитых; скрыть «Rules…» без опций; позже — старт на indoor-карте | Низкий: MAW-код включается только для id `maw`, таблицы движка не меняются | Сразу работает сохранение и загрузка, вкладка, отдельный контекст, Minotaur Rebalance | «Ruleset» по смыслу шире, чем правила; нельзя одновременно Medusa + MAW |
| B. Новый мир `worlds/medusa` | `world.yml` + свои карты; выбор мира в New Game | Убрать жёсткие списки mm6/mm7/mm8 (`AssetFileSystem.cpp:119`, `GameDataLoader.cpp:2463`, `GameApplication.cpp:10894`), выбор мира в меню, регистрация карт мира | Средний: монтирование ресурсов и владение картами | Правильная модель «отдельной игры» в будущем | Больше изменений до первого запуска; карты всё равно в общей `map_stats` |
| C. Новый слой «приключение» | Отдельная система | Много | Средний | — | Параллельная система, против правил `AGENTS.md` |

Рекомендация: **A сейчас**, и держать данные Medusa так, чтобы позже перенести их в мир (B), когда понадобятся свои
текстуры, музыка и экраны загрузки.

## 8. Временная стартовая карта

| Карта | Тип | Плюсы | Минусы |
|---|---|---|---|
| **`out15.odm` «Tutorial»** (рекомендуется для v1) | outdoor | Нет NPC и сюжета, события — только 20 сундуков (`worlds/mm8/events/maps/out15.lua`); outdoor-старт обходит дефект из §1 | В сцене `underwater: true`: зелёный подводный туман, часть предметов нельзя использовать. Стартовые координаты неизвестны |
| `d42.blv` Arena, `d50.blv` NWC | indoor | Маленькие | Нужен фикс indoor-старта; в NWC шуточные NPC разработчиков, в Arena своя логика |
| `out01.odm` | outdoor | Гарантированно рабочий старт | Сюжет MM8 (Dagger Wound) |

Карта используется по ссылке, без копии: оригинал не меняется, Medusa только задаёт старт.

## 9. Минимальный набор изменений для фазы C

Движок (`openyamm-medusa`, ветка `feature/project-medusa`):

1. `RulesetDefinition`: необязательный блок `newGame.starts` (карточки: ключ континента, название, подзаголовок,
   строка «Begin in…», картинка) + разбор + doctest.
2. `NewGameScreen::drawContinentSelection`: если у выбранного ruleset есть `starts`, рисовать их (одна карточка по
   центру), иначе — три существующие. Standard и MAW не меняются.
3. Не показывать «Rules…» для ruleset без опций.
4. Разметка: при трёх вкладках расширить `ContinentSelectionRulesetSwitch` или проверить ужатие подписи на 16:9 и 4:3.
5. (Для старта на своей BLV) исправить проверку из §1.

Контент (`project-medusa/content/engine/rulesets/medusa/`, черновик уже лежит в репозитории): `ruleset.yml`,
`content/character_selection.yml`, патч и append для `continent_settings.txt`.

Проверки: doctest на разбор `ruleset.yml` и на набор вкладок и карточек; headless-сценарий старта (если на машине
есть ресурсы MM8); ручной запуск на машине пользователя: вкладки 16:9 и 4:3, клавиатура и мышь, старт, сохранение и
загрузка, повторная загрузка Standard и MAW.
