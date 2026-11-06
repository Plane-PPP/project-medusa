# Игровая структура Project Medusa

## Как Medusa встроена в OpenYAMM (v1)

- **Пакет ruleset `medusa`** (`engine/rulesets/medusa/`), вкладка «Project Medusa» рядом со Standard MMMerge и MAW.
- Правила — Standard (с изменениями Minotaur Rebalance). Механики MAW не включаются: `MawRules` создаются только для
  id `maw`.
- Одна стартовая карточка Mount Nighon (`newGame.starts` в `ruleset.yml`), открывает штатное создание партии
  Antagarich (континент 2, `character_selection.yml` не заменяется); старт задаёт строка 2 `continent_settings.txt`
  (override: Death map 1 и 2 → `out10.odm` у площадки Town Portal).
- Сохранение помнит ruleset `medusa`; без пакета загрузка такого сохранения откажет, игра Standard и MAW не
  пострадает.

## Диапазоны идентификаторов (предложение)

| Домен | Диапазон Medusa | Занято другими |
|---|---|---|
| QBits | 20000–20999 | MAW 10001–10099 |
| NPC topics | 20000–20999 | MAW 10001–10099 |
| Портреты (`character_data`) | 79–89 | MAW 78 |
| Карты (`map_stats` #) | проверить последний занятый id (сейчас строк 781) | — |
| Континент | не нужен (используется 2, Antagarich) | 1–4 |

Диапазоны объявляются в `idRanges` пакета; движок проверяет их пересечение с мирами.

## Изоляция от прохождения MM8

- Код — в worktree `openyamm-medusa` (ветка `feature/project-medusa`); основной checkout и сохранения MM8 не
  трогаются.
- Игровые запуски для Medusa — с `--isolated` (свои настройки и сохранения).
- Мир на старте Medusa — MM7 (Mount Nighon, `out10.odm`). Выходы, Town Portal и Dimension Door ведут в обычный мир
  MM7; закрыть их — задача собственных карт или изоляции событий (см. [интеграцию](../integration.md)).

## Позже

- Собственный мир `worlds/medusa` (тексты, музыка, экраны загрузки, свои карты без общей `map_stats`) — когда
  ruleset-пакета станет мало.
- Раса «полумедуза» с механиками (окаменяющий взгляд) — отдельное решение.
