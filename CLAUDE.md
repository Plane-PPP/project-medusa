# Project Medusa — инструкция для агентов

Project Medusa — оригинальная RPG на движке OpenYAMM: самостоятельное приключение, не модификация сюжета MM6–MM8.

## Где что лежит

| Путь | Что |
|---|---|
| `/home/plane/projects/project-medusa` (этот репозиторий) | Контент и исходники игры: пакет `content/engine/rulesets/medusa`, карты, портреты, скрипты, документы |
| `/home/plane/projects/openyamm-medusa` | Git worktree OpenYAMM, ветка `feature/project-medusa` (от `feature/minotaur-rebalance` @ `0c172ed`): C++ и интеграция |
| `/home/plane/projects/openyamm` | Основной checkout, ветка `feature/minotaur-rebalance`. **Не трогать** без отдельной задачи |

Связь: `tools/link-dev.sh` создаёт симлинк пакета Medusa в `openyamm-medusa/assets_dev/engine/rulesets/medusa`. В
релизной сборке пакет кладётся в `mods/engine/rulesets/medusa/`.

## Начало сессии

1. Прочитать `docs/TODO.md` и `docs/DECISIONS.md`.
2. `git status` в обоих репозиториях; незакоммиченные изменения могут быть чужой работой.
3. Для работы с движком соблюдать `openyamm-medusa/AGENTS.md` и `/home/plane/AGENTS.md`.

## Сборка и тесты

- Только через `safe-heavy-run` (в песочнице агента он не запускается, нужен запуск на хосте с разрешения).
- Каталог сборки Medusa — `openyamm-medusa/build`. Общий `openyamm/build` не трогать.
- Тесты: `safe-heavy-run run -- ./build/tests/openyamm_unit_tests --test-case='*pattern*'`.
- На VM нет полных игровых ресурсов и дисплея: игровая проверка — на машине пользователя. Автотест не доказывает, что
  функция работает в игре.

## Запрещено без разрешения

- push, создание удалённых репозиториев, rebase опубликованной истории;
- изменение ресурсов MM6–MM8, существующих сохранений, общего каталога сборки и конфигурации другого агента;
- включение ресурсов Amber Island и оригинальных ресурсов MM в этот репозиторий;
- разработка собственного редактора карт или диалогов до доказанной нехватки существующих средств.

## После значимого шага

Обновить `docs/TODO.md`, записать решение в `docs/DECISIONS.md`, отделять «проверено» от «по коду» и «предположение».
