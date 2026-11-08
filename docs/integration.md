# Интеграция Project Medusa в OpenYAMM (Alpha 0.1)

Состояние на 2026-11-06. Уровни достоверности: **[проверено]** — командой или тестом (указано), **[код]** — по
исходникам, **[игра]** — ждёт проверки на Windows у пользователя.

## Схема

| Что | Где |
|---|---|
| Контент Medusa (ruleset-пакет) | этот репозиторий, `content/engine/rulesets/medusa/` |
| Изменения движка и Windows CI | `Plane-PPP/openyamm`, ветка `feature/project-medusa` (от `feature/minotaur-rebalance` @ `0c172ed`) |
| Связь при разработке (Linux) | `tools/link-dev.sh` → симлинк `openyamm-medusa/assets_dev/engine/rulesets/medusa` |
| Связь в релизе (Windows CI) | `packaging/medusa/install_content.py` **копирует** пакет из закреплённого коммита этого репозитория (`packaging/medusa/content.json` в движке) в `assets_dev/engine/rulesets/medusa`; симлинки запрещены |

Medusa — отдельный ruleset `medusa` (вкладка New Game). Правила — Standard MMMerge + Minotaur Rebalance: `MawRules`
создаются только для id `maw` (`game/app/GameSession.cpp`). Свой мир (`worlds/medusa`) пока не нужен; данные лежат так,
что их можно перенести в мир позже (аудит, §7).

## Пакет `content/engine/rulesets/medusa/`

| Файл | Назначение |
|---|---|
| `ruleset.yml` | id, название, `idRanges` (QBits и topics 20000–20999, портреты 79–89), `newGame.starts` (карточка Mount Nighon), таблицы |
| `content/continent_settings.patch.txt` | Строка 2 (Antagarich): Death map 1 и 2 → `out10.odm` 3114, −11055, 513, dir 0 |
| `content/character_data.patch.txt` | Пустой патч (заголовок): режим override требует путь |
| `content/character_data.append.txt` | Строка 79: героиня, кукла типа 1 (`pc02*`), класс 42 Sorcerer, голос 1, раса 0, лица `med01-` |
| `icons_x2/med01-01.png … med01-56.png` | Кадры лица 118×158 RGBA. С Alpha 0.2 — черновой набор героини, см. [portraits.md](design/portraits.md) |

Иконки пакета подключает `GameApplication::activateRuleset` → `AssetFileSystem::setRulesetIconRoot`; HUD, экран
создания партии и персонажа ищут кадры в `Data/icons` по имени (`med01-NN`, без атласа `faces_med01`). Корень иконок
ruleset переживает смену активного мира (`switchActiveWorld`, загрузка карты другого мира) с Alpha 0.2.1; до неё он
стирался, и HUD на Mount Nighon (мир mm7) показывал пустую рамку. **[проверено]** тестом `AssetFileSystem keeps the
active ruleset's icons when a map switches the active world`; в игре — **[игра]**.

`character_selection.yml` не заменяется: карточка Medusa открывает штатное создание партии Antagarich (континент 2,
классы и расы MM7). Небо, экраны загрузки, видео поражения — тоже Antagarich.

## Старт в Mount Nighon

- Карта: `out10.odm`, `map_stats.txt` #69 «Mount Nighon», мир `mm7`. **[проверено]** чтением таблицы и тестом.
- Точка: оригинальная площадка Town Portal «Nighon» из `town_portal_switch.txt` (карта 69: X 3114, Y −11055, Z 513,
  направление 0). Тест сверяет патч с этой строкой. **[проверено]** тестом `Project Medusa: the installed package…`.
- Окружение (по `out10.scene.yml`, скрипт в scratchpad, не в репозитории): ближайшие актёры — крестьяне (монстры
  360–366, уровни 1–3, группа 51) в 660–2200 ед. и стража Water Warlock (419, уровень 35, группа 55, `hostility_type 0`)
  в 1300–2200 ед., все на z=512 (точка старта — z 513). Ближайшие спавны враждебной группы 56 (Hydra/Roc/Warlock) —
  от 9 273 ед. **[проверено]** по данным сцены; поведение стражи в игре **[игра]**.
- События `out10.lua`: onLoad ставит QBit 721 (Town Portal Nighon) и делает группу 56 враждебной; зависимостей от
  сюжетных флагов нет. Дома, сундуки, обелиск (QBit 684), выходы в `7d07`/`d02` — штатные MM7. **[код]**
- Поражение: в мире `mm7` движок берёт Death map 1 (пока не взят QBit 519 Emerald Island), иначе Death map 2 — обе
  указывают на ту же точку Нигона. **[код]** `GameApplication::resolvePartyDefeatRespawnDestination`.
- Не изолировано: Town Portal/Lloyd/Dimension Door и выходы ведут в обычный мир MM7; «Antagarich» в Dimension Door
  ведёт на Emerald Island/Harmondale (жёстко в `GameplayPartyOverlayInputController.cpp`). Для альфы допустимо.

## Изменения движка (`feature/project-medusa`)

| Файл | Изменение |
|---|---|
| `game/content/RulesetDefinition.{h,cpp}` | `RulesetStartCard`, разбор `newGame.starts` (1–3 карточки, `continent` + `title` обязательны, ключи уникальны); `hasRulesChoices()`; `loadAvailableRulesets` пропускает сломанный пакет и сохраняет остальные |
| `game/ui/MenuDesignScreen.{h,cpp}` | `drawDesign(hiddenPrefixes)`: экран сам рисует скрытые элементы разметки |
| `game/ui/screens/NewGameScreen.{h,cpp}` | Карточки ruleset вместо трёх континентов (по центру ряда, вид и шрифты карточки Antagarich, строки на ширину названия); без «Rules…» для ruleset без опций; строка «… - Begin in …» из карточки; сломанный пакет не убирает остальные вкладки |
| `engine/AssetFileSystem.{h,cpp}` | `setRulesetIconRoot`: иконки активного ruleset (`engine/rulesets/<id>/icons_x2`) ищутся после пакетов иконок; заменить существующие не могут |
| `game/app/GameApplication.cpp` | `activateRuleset` выставляет корень иконок ruleset (Standard — пусто) |
| `tests/ProjectMedusaTests.cpp`, `tests/AssetFileSystemTests.cpp` | Новые тесты (ниже) |
| `.github/workflows/medusa-windows.yml`, `packaging/medusa/*` | Windows CI и упаковка патча |

Ресурсы движка (разметка `continent_selection.yml`, таблицы) **не менялись**: патч не заменяет большие паки.

## Портреты и кукла

- Кадры `med01-NN` ищутся по имени в `Data/icons` → в т. ч. `engine/rulesets/medusa/icons_x2` (только при активном
  Medusa). Атлас `faces_med01.*` не нужен: без атласа HUD грузит PNG (`GameplayHudCommon::loadHudTexture`). **[код]**
- Замена кадров без C++: `tools/import_portraits.py <папка>` → коммит → новая сборка CI (меняется только пак
  `engine.rulesets`).
- Кукла: колонка `head` в `character_data.txt` **разбирается, но нигде не рисуется** (`CharacterDollTable.cpp:145`,
  других использований нет): голова на кукле — часть картинки тела `pc02bod` (166×594). Значит, «голова Medusa» на
  кукле = своя картинка тела `med01bod.png` (166×594, тот же контур, что `pc02bod`) в `icons_x2/` пакета и правка одной
  ячейки (колонка 9) в `character_data.append.txt`. Без C++. Аудит фаз A–B в этом пункте был неточен.
- Смерть/стирание: общие `DEAD`/`ERADCATE` для всех героев (`GameplayUiRuntime.cpp`). Свой кадр смерти потребует
  правки движка.

## Сохранения

Сохранение пишет id ruleset и персонажа (`characterDataId` 79, `portraitTextureName` `med01-01`, `portraitPictureId`
78). **[проверено]** тестом «saves keep the Project Medusa ruleset…». Без пакета загрузка такого сохранения
отказывает, текущая игра остаётся (аудит §6). **[код]**

## Тесты

```sh
cd ../openyamm-medusa
safe-heavy-run run -- ./build/tests/openyamm_unit_tests --test-case='*Medusa*,*start card*,*ruleset*,*Ruleset*,AssetFileSystem*'
```

Сборку в `openyamm-medusa/build` см. [build-and-install.md](build-and-install.md).
