# Сборка, Windows CI и установка

## Совместимость

| Что | Значение |
|---|---|
| База кода | `feature/minotaur-rebalance` @ `0c172ed` (OpenYAMM upstream 1.20, `1add1d3`) |
| Нужная установка у игрока | ровно `minotaur-1.20-c80ebaa9634d-25-1` (файл `app/current` в папке игры) |
| Почему эта | последний опубликованный базис Minotaur (`packaging/minotaur/latest-baseline.json`). Между его исходником `c80ebaa` и `0c172ed` изменены только документы, тесты, `tools/check_doc_i18n.py` и файлы базиса — код и ресурсы игры те же. **[проверено]** `git diff --name-only c80ebaa9634d 0c172ed` |
| Версия после установки | `minotaur-1.20-medusa-0.1-<sha12>-<run>-<attempt>` (установщик Minotaur требует префикс `minotaur-`) |

## Что меняет патч

Патч — штатное инкрементальное обновление Minotaur (`tools/minotaur_updates.py`), тот же установщик
`Apply-MinotaurUpdate.cmd` с проверкой базовой версии, SHA256 и атомарным переключением `app/current`.

- **Заменяет** программу: новая папка `app/<версия>/` (`openyamm.exe`, `OpenYAMM-launcher.exe`, DLL, шейдеры —
  точный список пишется в `MEDUSA-VERSION.txt` внутри ZIP), затем переключает `app/current`.
- **Добавляет/меняет** пак ресурсов `engine.rulesets` (~0,4 МБ: MAW + Medusa, включая 56 PNG-кадров) в
  `assets/packs/`. Остальные паки (≈ 5 ГБ) переиспользуются.
- **Не трогает** `saves/`, `settings.ini`, логи, ресурсы MM6–MM8.
- В папку патча добавлены `README-MEDUSA-RU.txt` (установка, откат, чек-лист) и `MEDUSA-VERSION.txt`.

## Windows CI

Workflow `.github/workflows/medusa-windows.yml` в `Plane-PPP/openyamm`, ветка `feature/project-medusa`.

- Запуск: push в `feature/project-medusa` (пути движка/пакетов/CI). Ручной `workflow_dispatch` GitHub разрешает только
  для workflow из ветки по умолчанию, а `main` по условиям не меняется — поэтому основной триггер push.
- Контент: коммит `Plane-PPP/project-medusa` из `packaging/medusa/content.json` (поле `commit`). Чтобы собрать новый
  контент: закоммитить и запушить здесь → вписать SHA в `content.json` движка → закоммитить и запушить движок.
- Шаги: checkout движка → checkout контента по SHA → MSYS2 → копия пакета (`install_content.py`) → проба ресурсов →
  configure → сборка → тесты (`*Medusa*`, `*start card*`, `*ruleset*`, иконки ruleset, тесты Minotaur, runtime-тесты
  создания партии) → упаковка ресурсов → тонкий архив и проверка → патч над базисом → проверка состава патча →
  Step Summary → артефакты.
- Сохранены оптимизации Minotaur CI: `measure_windows_build.py` (замер ресурсов и `MINOTAUR_BUILD_JOBS`), фазы с
  логом времени и памяти, артефакт `medusa-build-resources-*`.
- Артефакты: `project-medusa-alpha-patch-<sha>-windows-x64` (ZIP патча, 30 дней), `project-medusa-metadata-<sha>`
  (размер/SHA256 и `minotaur-baseline.json` новой версии, 90 дней).

## Установка у игрока

См. `packaging/medusa/README-MEDUSA-RU.txt` в движке (он же лежит в ZIP). Коротко: рекомендуемый вариант для альфы —
скопировать папку игры и ставить патч в копию; откат — удалить копию.

## Локальная сборка на VM (Linux)

Только через `safe-heavy-run`. Каталог `openyamm-medusa/build`; общий `openyamm/build` не трогать.

Первая настройка (сделано 2026-11-06): зависимости собираются offline. В `openyamm-medusa/build` скопированы
`manual-sources/` и `_deps/*-src` из `openyamm/build` (только чтение оттуда), `ubuntu-sysroot/` (заголовки GL/X11);
кэш CMake засеян не-INTERNAL параметрами основного `CMakeCache.txt` с заменой путей. CMake — из
`~/.local/share/openyamm-toolchain/root/usr/bin` (нужен `LD_LIBRARY_PATH=…/root/usr/lib/x86_64-linux-gnu`).

```sh
T=~/.local/share/openyamm-toolchain
safe-heavy-run run -- env PATH=$T/root/usr/bin:$PATH LD_LIBRARY_PATH=$T/root/usr/lib/x86_64-linux-gnu \
  cmake --build ../openyamm-medusa/build --target openyamm_unit_tests
cd ../openyamm-medusa && safe-heavy-run run -- ./build/tests/openyamm_unit_tests --test-case='*Medusa*'
```

Перед тестами пакета: `tools/link-dev.sh` (симлинк). Тесты установленного пакета без него пропускаются.

## Опубликовано (2026-11-06)

| Что | Ссылка / SHA |
|---|---|
| Контент | https://github.com/Plane-PPP/project-medusa — `main` |
| Движок | https://github.com/Plane-PPP/openyamm/tree/feature/project-medusa — `2c1ae60` (первый коммит Medusa поверх `0c172ed`) |
| Закреплённый контент в CI | `887b0fd46d9ceba89fdd37f626a08c7147b980fe` (`packaging/medusa/content.json`) |
| Первый Windows CI | https://github.com/Plane-PPP/openyamm/actions/runs/42184813008 |

### Результат первого CI (run 42184813008, движок `2c1ae60`) — **[проверено] CI**

- Все шаги успешны: Windows-сборка, тесты Medusa/ruleset/Minotaur и runtime-тесты создания партии, упаковка,
  проверка тонкого архива, проверка состава патча (в паке `engine.rulesets` есть `medusa/ruleset.yml`, таблицы,
  `med01-01/56.png` и `maw/ruleset.yml`; в ZIP — `openyamm.exe` и README).
- Артефакт `Project-Medusa-Alpha-0.1-Windows-Patch.zip`, 22 955 695 байт.
- Версия после установки: `minotaur-1.20-medusa-0.1-2c1ae605467a-1-1`.
- Изменён 1 пак (`engine.rulesets-27bc4bdd4ec0da44.zip`, 186 411 байт), переиспользовано 165 паков (5,8 ГБ).
- Базис новой версии (`minotaur-baseline.json`) — в артефакте `project-medusa-metadata-2c1ae60…`; положить его в
  `packaging/minotaur/bases/` ветки Medusa после успешной установки у пользователя.
- Известная мелочь: SHA256 в `Project-Medusa-Alpha-0.1-Windows-Patch.json` посчитан до добавления README Medusa
  (`finish_patch.py` дописывает файлы в ZIP после отчёта) — исправить в следующей итерации.
- Скачивание артефакта на VM: канал к хранилищу Azure очень медленный (~5 КБ/с); помогает
  `curl --http1.1 -C -` по подписанной ссылке (токен в хранилище не передавать).
