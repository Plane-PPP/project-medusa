# Ruleset-пакет Project Medusa

Устанавливается в движок как `engine/rulesets/medusa/` (разработка — `tools/link-dev.sh`, релиз — копия в Windows CI).
Файлы `.md` в релизный пак не попадают.

- `ruleset.yml` — описание, карточка New Game (`newGame.starts`), таблицы.
- `content/` — правки таблиц движка: старт Antagarich → Mount Nighon, строка героини 79.
- `icons_x2/med01-NN.png` — кадры лица героини 118×158. Сейчас **временные заглушки TEMP**
  (`tools/make_placeholder_portraits.py`); финальные — `tools/import_portraits.py`.

Подробно: `docs/integration.md`.
