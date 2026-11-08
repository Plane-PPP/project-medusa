# Project Medusa — инструкция для агентов

Project Medusa — оригинальная RPG на движке OpenYAMM: самостоятельное приключение, не модификация сюжета MM6–MM8.
Текущая версия — Alpha 0.2.2 (ruleset-пакет, старт Mount Nighon, героиня с портретами v2).

## Где что лежит

| Путь | Что |
|---|---|
| `/home/plane/projects/project-medusa` (этот репозиторий, публичный `Plane-PPP/project-medusa`) | Контент: пакет `content/engine/rulesets/medusa`, карты, портреты, скрипты, документы |
| `/home/plane/projects/openyamm-medusa` | Git worktree OpenYAMM, ветка `feature/project-medusa` (от `feature/minotaur-rebalance` @ `0c172ed`), публикуется в `Plane-PPP/openyamm`: C++, Windows CI, `packaging/medusa/` |
| `/home/plane/projects/openyamm` | Основной checkout, ветка `feature/minotaur-rebalance`. **Не трогать** без отдельной задачи (читать `build/` можно) |

Связь: `tools/link-dev.sh` создаёт симлинк пакета Medusa в `openyamm-medusa/assets_dev/engine/rulesets/medusa`.
Windows CI копирует пакет из коммита, закреплённого в `openyamm-medusa/packaging/medusa/content.json`.

## Начало сессии

1. Прочитать `docs/TODO.md`, `docs/DECISIONS.md`, `docs/integration.md`, `docs/build-and-install.md`.
2. `git status` в обоих репозиториях; незакоммиченные изменения могут быть чужой работой.
3. Для работы с движком соблюдать `openyamm-medusa/AGENTS.md` и `/home/plane/AGENTS.md`.

## Сборка и тесты

- Только через `safe-heavy-run`. Каталог сборки Medusa — `openyamm-medusa/build` (настроен, см.
  `docs/build-and-install.md`: локальный cmake из `~/.local/share/openyamm-toolchain`, offline-зависимости).
  Общий `openyamm/build` не трогать.
- Тесты: `safe-heavy-run run -- ./build/tests/openyamm_unit_tests --test-case='*Medusa*,*start card*,*ruleset*'`.
- На VM нет полных игровых ресурсов и дисплея: игровая проверка — на машине пользователя (Windows). Автотест не
  доказывает, что функция работает в игре. Различать: код / unit-тесты / CI-сборка / игра.

## Выпуск новой сборки

1. Коммит и push здесь (`main`).
2. В движке вписать SHA в `packaging/medusa/content.json`, коммит, push `feature/project-medusa` → workflow
   `Project Medusa Windows build` (push-триггер; `workflow_dispatch` недоступен, пока workflow нет в `main`).
3. Артефакт `project-medusa-alpha-patch-<sha>-windows-x64`; при успехе — prerelease (не стабильный релиз).

## Запрещено без разрешения

- force push, rebase опубликованной истории, изменение `main`/`master`/`upstream`/`feature/minotaur-rebalance` движка,
  новые GitHub-репозитории;
- изменение ресурсов MM6–MM8, существующих сохранений, общего каталога сборки и конфигурации другого агента;
- включение ресурсов Amber Island и оригинальных ресурсов MM в этот репозиторий;
- разработка собственного редактора карт или диалогов до доказанной нехватки существующих средств.

Разрешено пользователем (2026-11-06): коммиты и обычный push в `Plane-PPP/project-medusa` и в ветку
`feature/project-medusa` форка `Plane-PPP/openyamm`, запуск CI, CI-артефакты и prerelease `medusa-alpha-*`.

## После значимого шага

Обновить `docs/TODO.md`, записать решение в `docs/DECISIONS.md`, отделять «проверено» от «по коду» и «предположение».
