# Project Medusa

Оригинальная RPG на движке [OpenYAMM](https://github.com/pjasicek/openyamm). Главная героиня — полумедуза.

Состояние: **Alpha 0.1** — вкладка Project Medusa в New Game, старт в Mount Nighon (MM7), героиня с временными
кадрами портрета. Правила — Standard MMMerge с Minotaur Rebalance. Игровая проверка на Windows ожидается.

| Репозиторий | Что |
|---|---|
| [Plane-PPP/project-medusa](https://github.com/Plane-PPP/project-medusa) (этот) | Контент, документы, инструменты |
| [Plane-PPP/openyamm, ветка `feature/project-medusa`](https://github.com/Plane-PPP/openyamm/tree/feature/project-medusa) | Изменения движка и Windows CI |

| Каталог | Содержимое |
|---|---|
| `content/engine/rulesets/medusa/` | Ruleset-пакет Medusa для OpenYAMM: `ruleset.yml`, таблицы, кадры портрета `icons_x2/` |
| `maps/` | Исходники карт: `.blend`, `.glb`, `geometry.yml`, `scene.yml`, Lua |
| `portraits/` | Исходники портретов высокого разрешения; `templates/` — окно и схема кадра; `reference/` — оригиналы MM, локально, не коммитятся |
| `scenes/`, `assets/`, `scripts/` | Сцены, прочие ресурсы, игровые скрипты |
| `tools/` | `link-dev.sh` (связь с движком), `make_placeholder_portraits.py`, `import_portraits.py`, `portrait_kit.py` (сборка и проверка кадров портрета) |
| `docs/` | [TODO](docs/TODO.md), [решения](docs/DECISIONS.md), [интеграция](docs/integration.md), [сборка и установка](docs/build-and-install.md), `design/`, `research/` |

Начать: [CLAUDE.md](CLAUDE.md).

Лицензия контента не выбрана. Оригинальные ресурсы Might and Magic и Amber Island в репозиторий не входят: Medusa
читает карту, куклу и картинки из установленной игры по именам. Кадры `med01-*` — набор портретов v2 (Alpha 0.2.2).
