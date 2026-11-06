# Редактор уровней OpenYAMM: аудит и сравнение с MMEditor

Статус: исследование, 2026-11-06, ветка `feature/minotaur-rebalance` на `0c172ed`. Код не менялся, сборок и запусков
не было. Всё ниже установлено чтением исходников, если не указано иное.

Связанные документы: [Amber Island](amber-island-development-workflow.md),
[создание indoor-карты](custom-indoor-level-workflow.md), [план башни](tower-prototype-plan.md).

## Статусы

| Статус | Значение |
|---|---|
| **Проверено** | Проверено в этой работе запуском или разбором реальных файлов |
| **Реализовано, не проверено** | Код и автотесты есть, но в этом checkout не собраны и не запускались |
| **Частично** | Есть важные пробелы |
| **Отсутствует** | Кода нет |
| **Ошибка** | Найдено расхождение, которое ломает сценарий |

## 1. Что где лежит

| Компонент | Путь | Примечание |
|---|---|---|
| Редактор (ImGui + bgfx) | `editor/app/`, `editor/document/`, `editor/viewport/` | Собирается только с `-DOPENYAMM_BUILD_EDITOR=ON` (`CMakeLists.txt:35`). В `build/` сейчас `OFF`, бинарника нет |
| Импорт моделей | `editor/import/ObjModelImport.cpp` | OBJ (`v`, `vt`, `usemtl`, `o`/`g`, `f`) и glTF/GLB (cgltf) |
| Импорт indoor-источника | `editor/import/IndoorSourceGeometryImport.cpp` | Классификация узлов по префиксу имени |
| Компилятор indoor | `editor/import/IndoorSourceGeometryCompiler.cpp`, `IndoorDerivedGeometry.cpp` | GLB + `geometry.yml` → `IndoorMapData` → BLV, BSP, контуры, порталы, двери |
| CLI-компилятор | `tools/mm9_compile_indoor_source_main.cpp`, цель `mm9_compile_indoor_source` (`tools/CMakeLists.txt:60`) | Требует `-DOPENYAMM_BUILD_TOOLS=ON` (`CMakeLists.txt:36`), сейчас `OFF` |
| Headless-сборка карты | `openyamm-editor --headless-build-map <scene>` (`editor/app/main.cpp:113`, `EditorHeadlessDiagnostics.cpp:3618-3664`) | Загружает документ, валидирует, вызывает `buildRuntime` |
| Регрессия редактора | `--headless-run-regression-suite` (`main.cpp:101`), в т.ч. `verifyIndoorMapPackageLoad` (`EditorHeadlessDiagnostics.cpp:2043`) | Содержит синтетический GLB с узлами всех префиксов (`:2112-2160`) |
| Юнит-тесты компилятора | `tests/IndoorSourceGeometryCompilerTests.cpp`, 21 `TEST_CASE`, цель `openyamm_indoor_source_tests` | Тоже под `OPENYAMM_BUILD_TOOLS` |
| Загрузка карт игрой | `game/maps/MapAssetLoader.cpp:4495` (ODM), `:4865` (BLV); `game/indoor/IndoorMapData.cpp`, `game/outdoor/OutdoorMapData.cpp` | MM6/MM7/MM8 |
| Описание сцены | `<map>.scene.yml` (`game/maps/IndoorSceneYml.cpp`) | Сущности, состояние, двери, переопределяет данные DLV |
| Метаданные геометрии | `<map>.geometry.yml` (`editor/document/IndoorGeometryMetadata.*`) | Источник, материалы, комнаты, порталы, механизмы, поверхности, сущности, свет |
| События | `assets_dev/worlds/<world>/events/maps/<map>.lua`, API в `game/events/EventRuntime.cpp:9175-9300`, `assets_dev/engine/scripts/common/event_support.lua` | `RegisterEvent(id, title, fn)`, `SetMapMetadata{…}` |
| `level_generation/` | **Отсутствует в публичном репозитории.** В upstream когда-то был только `level_generation/lighting/baked_outdoors/README.md`, удалён в `856f27d` | Документы, на которые ссылается `AGENTS.md`, здесь недоступны |

## 2. Indoor-источник: соглашения

Узлы GLB классифицируются по префиксу имени (`IndoorSourceGeometryImport.cpp:306-393`):

| Префикс | Становится | Аналог в MMEditor |
|---|---|---|
| `ROOM_<id>` | Комната (сектор) | Объект `o`/`g` при импорте «as rooms» |
| `PORTAL_<a>_<b>` | Портал между комнатами | Грань с материалом `_Portal_` |
| `TRIGGER_<id>` | Кликабельная поверхность с событием | Свойства грани Event/TriggerByClick |
| `MECH_<id>` | Механизм: дверь, лифт, поворотная створка | New Door + VertexFilter |
| `DECOR_<id>` | Декорация (спрайт или 3D-модель) | Sprite |
| `LIGHT_<id>` | Источник света | Light |
| `SPAWN_<id>` | Точка спавна | Spawn |
| другое | Предупреждение «Unclassified indoor source mesh/node» | — |

Ключевое отличие: метаданные (`geometry.yml`) привязаны к **имени узла**, а не к позициям вершин, как в MMEditor.
После правки геометрии в Blender и повторного импорта идентификаторы, события и параметры дверей сохраняются, если
имена узлов не менялись. Тест «indoor source rejects stale room membership instead of guessing an owner» показывает,
что устаревшие привязки отклоняются явно, а не угадываются.

Параметры источника по умолчанию (`IndoorGeometryMetadata.h`): `coordinate_system: blender_z_up`,
`unit_scale: 128` (1 метр Blender = 128 игровых единиц), `merge_vertices_epsilon: 0.01`,
`triangulate_ngons: true`, `generate_bsp/outlines/portals: true`.

## 3. Сравнение с MMEditor

| Функция | MMEditor (GrayFace) | OpenYAMM | Что требуется |
|---|---|---|---|
| Импорт геометрии | OBJ, Y-up с поворотом, `ImportScale`. Объекты становятся комнатами. Портал задаётся текстурой `_Portal_`, невидимость `_Invisible_` или `d<1` (`Editor Import.lua`) | OBJ и GLB. Для indoor-источника нужен GLB: метаданные строятся по узлам glTF, в редакторе есть только «Import Source Geometry» из модели | **Реализовано, не проверено.** Стандартизировать экспорт GLB из Blender |
| Новая indoor-карта | New: пустая карта того же типа | Есть «New Outdoor Map» (`createNewOutdoorMap`), **команды «New Indoor Map» нет**. Indoor-источник импортируется в уже открытый indoor-документ | **Отсутствует.** Минимальная доработка: шаблон `scene.yml` или команда создания пустого indoor-пакета |
| Сектора и порталы | Автоматические порталы по общим вершинам, ручные `_Portal_`, BSP на комнату | Комнаты из `ROOM_*`, порталы из `PORTAL_*`, `generate_portals`, BSP и контуры (`IndoorDerivedGeometry.cpp`). Тесты есть: BSP с пересекающимися полигонами, портал в полу | **Реализовано, не проверено** |
| Двери | New Door, Door Shape, VertexFilter, свойства в редакторе | `MECH_*` + `mechanisms` в `geometry.yml`: ось, дистанция, скорости, `source_pose`, `kind` (`slide`, `rise`, `nudge`, `rotating`), `extra_rooms`. Генерация `IndoorSceneDoor` | **Реализовано, не проверено.** Поворотные двери новее, чем в MM7 |
| Лестницы, лифты | Наклонные полы, двери-лифты по Z | Наклонные полы классифицируются по нормали (типы 3/4/5/6), лифт как механизм. Тест «authored closed lift…». Отдельные `ladders` в сцене (`devdocs/INDOOR_ROTATING_MOVERS_AND_LADDERS.md`) | **Реализовано, не проверено** |
| Текстуры | Bitmap по имени из `map_Kd`. Нельзя вращать или растягивать, UV задаётся смещением от первой вершины | `materials` в `geometry.yml`: `source_material` → `texture`, размеры. Тест «preserves pixel UVs…» | **Реализовано, не проверено.** Нужно проверить, переносятся ли поворот и масштаб UV или приводятся к смещению, как в BLV |
| Объекты, монстры, свет | Внутриигровая расстановка | `DECOR_`/`LIGHT_`/`SPAWN_` в источнике. В редакторе есть CreateIndoorActor/Decoration/Object/Spawn и Create Party Start | **Реализовано, не проверено** |
| События | `.evt`/Lua MMExtension, свойство Event на грани | `TRIGGER_*` (`event_id`, `cog_number`). Lua `RegisterEvent`. Редактор показывает события и умеет `simulateMapEvent` | **Частично.** Привязка есть, редактора логики нет |
| Сохранение | Проект `.dat` + Compile в `.blv`/`.dlv` | Save Source (`scene.yml`, `geometry.yml`) + Build (`.blv`). Атомарная запись (`EditorDocument.cpp:2735-2775`) | **Реализовано, не проверено** |
| Редактирование готовой карты | Internal Map: открыть карту из LOD. Реимпорт теряет свойства граней | Открыть indoor-карту мира (`openIndoorMap`), сцена из `scene.yml`. Реимпорт источника сохраняет метаданные по именам | **Реализовано, не проверено**. По устойчивости к реимпорту превосходит MMEditor |
| Экспорт геометрии | Export, Export Selected в OBJ | Экспорта indoor-геометрии в OBJ/GLB не найдено | **Отсутствует.** Нужен только для переноса существующих карт в Blender |
| Отмена | Ограниченно (импорт не отменяется) | `captureUndoSnapshot` / `undo` | **Реализовано, не проверено** |
| Платформа | Windows, внутри `mm7.exe` + MMExtension | Linux, Windows, macOS | — |

## 4. Совместимость форматов

| Вопрос | Ответ | Статус |
|---|---|---|
| Оригинальные карты MM7 в OpenYAMM | Да, мир `mm7`: 63 BLV и 13 ODM с `scene.yml` в `assets_dev/worlds/mm7/maps/` | Используется игрой; в этой работе не запускалось |
| BLV/DLV Amber Island без преобразования | Структура v7 совпадает байт в байт для всех 11 BLV и DLV | **Проверено разбором** (не в игре) |
| ODM из MMEditor | Пустая метка версии, OpenYAMM выбирает layout MM8 (`OutdoorMapData.cpp:71-89`) и теряет BModels | **Ошибка** по анализу файлов. Минимальное исправление: различать v7 и v8 по структуре, а не только по метке |
| Геометрия из MMEditor напрямую | Только через скомпилированный BLV. Свои файлы проекта MMEditor (`.dat`) OpenYAMM не читает | — |
| Сохранение модифицированной карты без потерь | Для indoor-источника: да, перекомпиляция из GLB + YAML. Для готового BLV: редактируется сцена (`scene.yml`), геометрия BLV остаётся как есть | **Реализовано, не проверено** |
| События и скрипты Amber Island | Нет: другой Lua API (MMExtension против `RegisterEvent`, именованные таблицы против позиционных аргументов) и хуки памяти | **Проверено чтением кода** |
| Что нужно адаптировать | ODM-детекция; перевод Lua вручную или конвертером; миграция таблиц в объединённые таблицы MMerge; регистрация карт в `map_stats.txt` | — |

Разделение по уровням: **геометрия** BLV совместима, ODM требует правки детекции; **объекты** (DLV) совместимы
структурно, но ID монстров и предметов указывают на таблицы мода; **логика** несовместима.

## 5. Пробелы, блокирующие первую собственную карту

1. В рабочей сборке выключены `OPENYAMM_BUILD_EDITOR` и `OPENYAMM_BUILD_TOOLS`, поэтому компилятор и редактор нужно
   собрать. Сборка выполняется через `safe-heavy-run`, внутри песочницы агента он отказывается запускаться
   (нет systemd bus), нужен запуск на хосте.
2. Нет создания пустой indoor-карты: нужен шаблон `scene.yml`.
3. Карта появляется в игре только через строку в общем `assets_dev/engine/data_tables/map_stats.txt` (колонка
   `world_id`), то есть меняется существующий ресурс движка.
4. Документация процесса (`level_generation/README.md`, на который ссылается `AGENTS.md`) отсутствует в публичном
   репозитории.

Ни один пункт не требует переработки движка. Пункты 2 и 4 закрываются документацией и шаблоном, пункт 3 — одной
строкой таблицы при согласовании.
