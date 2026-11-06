# Новая indoor-карта для OpenYAMM с нуля

Статус: **проект инструкции, ещё не выполнен от начала до конца.** Шаги собраны по исходникам OpenYAMM на `0c172ed`
и опыту Amber Island. Шаги 1–4 подтверждаются кодом и автотестами репозитория, но в этой работе не запускались. Все
пометки «проверить» нужно снять во время прототипа ([план башни](tower-prototype-plan.md)).

Почему не MMEditor: см. [Amber Island](amber-island-development-workflow.md), раздел 7, и
[аудит редактора](openyamm-level-editor-capabilities.md).

## Схема

```text
Blender (.blend)
  └─ экспорт glTF Binary (.glb): узлы ROOM_/PORTAL_/MECH_/TRIGGER_/LIGHT_/DECOR_/SPAWN_, материалы = текстуры
       └─ <map>.geometry.yml   метаданные, ключ = имя узла (git, правится руками или редактором)
            └─ компилятор OpenYAMM (editor Build / --headless-build-map / mm9_compile_indoor_source)
                 └─ <map>.blv  скомпилированная геометрия, BSP, порталы, двери
<map>.scene.yml   сущности, начальное состояние, двери, сундуки (git)
<map>.lua         события: RegisterEvent(...) (git)
map_stats.txt     строка карты с world_id (git)
```

Источник истины: `.blend` → `.glb` + YAML + Lua. `.blv` всегда производный файл.

## 0. Подготовка (один раз)

1. Blender 4.x с встроенным экспортёром glTF. **На этом хосте Blender не установлен** (`which blender` пуст).
2. Сборка редактора и инструментов. По правилам VM только через `safe-heavy-run`:

   ```sh
   safe-heavy-run check
   safe-heavy-run run -- cmake -S . -B build -DOPENYAMM_BUILD_EDITOR=ON -DOPENYAMM_BUILD_TOOLS=ON
   safe-heavy-run run -- cmake --build build --target mm9_compile_indoor_source openyamm_indoor_source_tests
   safe-heavy-run run -- cmake --build build --target openyamm-editor
   safe-heavy-run run -- ./build/tools/openyamm_indoor_source_tests
   ```

   Проверить: точный путь бинарников внутри `build/`, `openyamm_indoor_source_tests` должен пройти 21 тест. Изменение
   опций `build/CMakeCache.txt` затрагивает общий каталог сборки, которым пользуется и Codex. Либо согласовать, либо
   собирать в отдельном каталоге (дольше: полная пересборка движка).

## 1. Геометрия в Blender

Правила, общие для MMEditor и OpenYAMM:

- Ось Z вверх. 1 единица Blender = `unit_scale` игровых единиц (по умолчанию 128): коридор 2.5 × 3 м даёт 320 × 384
  единиц. Ориентир по размерам — `doortest.blv` Amber Island (высота 512, проём под дверь шириной 368). Точную высоту
  и радиус партии взять из кода движения перед моделированием (в этой работе не сверялась).
- Каждая комната — отдельный объект `ROOM_<имя>`. Комнаты замкнуты, нормали смотрят **внутрь**: игрок находится внутри
  объёма. В MMEditor вырожденные грани молча отбрасываются (`Editor Import.lua:153`); проверьте Mesh → Clean Up.
- Проём между комнатами закрывается отдельным объектом `PORTAL_<комнатаA>_<комнатаB>`: одна плоская выпуклая грань
  точно по контуру проёма. Порталов не больше, чем нужно. Тест OpenYAMM «indoor source marks the room above a floor
  portal» показывает, что горизонтальные порталы (люк, лестничный пролёт) поддерживаются.
- Материал называется как текстура MM (`T5s1FL`, `T6s1bs`…) или сопоставляется в `materials` по `source_material`.
  Текстуры в BLV нельзя вращать и масштабировать, только сдвигать. Ставьте UV в масштабе текстуры, без поворота;
  проверить, как компилятор обрабатывает поворот UV.
- Дверь — отдельный объект `MECH_<имя>`, обычно в открытом положении (`source_pose: open`, базовая поза в нативном
  формате). Кнопка или рычаг — `TRIGGER_<имя>`.
- Свет `LIGHT_<имя>`, декорации `DECOR_<имя>`, монстры `SPAWN_<имя>`: пустышки или маленькие меши в нужной точке.
- Не делайте пересекающихся стен внутри одной комнаты и тонких «ножей» менее 2–3 единиц: такие места вызывают
  застревания (опыт Amber Island, видео Dev Stream 09).

Экспорт: File → Export → glTF 2.0 Binary, с UV, без анимаций и камер. Проверить, нужно ли «+Y Up» выключить для
`coordinate_system: blender_z_up`.

## 2. Метаданные `<map>.geometry.yml`

Создаются импортом (Editor → Import Source Geometry, `EditorSession::importIndoorSourceGeometryFromModel`), который
раскладывает узлы по префиксам. Структура (`editor/document/IndoorGeometryMetadata.cpp`, функция записи):

```yaml
format_version: 1
kind: indoor_geometry
map_file: tower1.blv
source:
  asset_path: tower1.glb
  coordinate_system: blender_z_up
  unit_scale: 128
  import: {source_format: glb, triangulate_ngons: true, generate_bsp: true,
           generate_outlines: true, generate_portals: true, reserve_sector_zero: false}
materials:
  - {id: floor, source_material: T5s1FL, texture: T5s1FL, texture_width: 128, texture_height: 128}
rooms:
  - {id: room_west, name: West, source_nodes: [ROOM_west]}
  - {id: room_east, name: East, source_nodes: [ROOM_east]}
portals:
  - {id: portal_west_east, front_room: room_west, back_room: room_east, source_node: PORTAL_west_east}
mechanisms:
  - id: door_main
    kind: slide
    source_nodes: [MECH_door_main]
    trigger_surfaces: [door_main_handle]
    door: {source_pose: open, direction: [1, 0, 0], move_length: 368, open_speed: 50, close_speed: 50}
surfaces:
  - {id: door_main_handle, source_node: TRIGGER_door_main_handle, trigger: {event_id: 1, type: door}}
```

Это схема для ориентира, а не проверенный файл: точные поля и вложенность сверять с
`loadIndoorGeometryMetadataFromText`. Значения двери взяты из `doortest.blv` Amber Island.

## 3. Сцена `<map>.scene.yml` и события

Команды «New Indoor Map» в редакторе нет. Возьмите маленькую сцену существующей карты как шаблон
(`git show HEAD:assets_dev/worlds/mm7/maps/7d05.scene.yml`, 325 строк). Нужные разделы: `format_version`,
`kind: indoor_scene`, `source.geometry_file`, `environment`, `spawns`, `initial_state` (`location`, `doors`, `chests`,
`actors`, `variables`). Для карты, собранной из источника, `legacy_companion_file` не нужен (проверить).

События в `assets_dev/worlds/<world>/events/maps/<map>.lua` пишутся вручную. Это не сгенерированный файл, и его
можно редактировать:

```lua
-- Tower floor 1
RegisterEvent(1, "Door", function()
    evt.SetDoorState(1, DoorAction.Trigger)
end, "Door")
```

## 4. Сборка и регистрация

```sh
# вариант A: без редактора
safe-heavy-run run -- ./build/tools/mm9_compile_indoor_source \
    tower1.glb tower1.geometry.yml tower1.blv tower1.doors.yml tower1.faces.yml
# вариант B: через сцену, как это делает редактор
safe-heavy-run run -- ./build/editor/openyamm-editor --world <world> --headless-build-map <path>/tower1.scene.yml
```

Регистрация в игре: строка в `assets_dev/engine/data_tables/map_stats.txt` с файлом карты и `world_id`. Это
изменение общей таблицы движка, его нужно согласовать. Для собственной RPG правильнее отдельный мир
`assets_dev/worlds/<id>/world.yml` (образец: `assets_dev/worlds/mm8/world.yml`, ключи `id`, `name`, `sourceGame`,
`start.map`).

## 5. Проверка

1. Автоматически (`tests/scenarios/*.yml`, запуск `./build/game/openyamm --headless-run-scenario <file>`):
   `load_map`; `movement_segment` из комнаты в комнату с `expect_stop` (коллизии и переход через портал);
   `execute_event` для двери и повторный `movement_segment` через проём; `save_game` / `load_game`.
2. Визуально: `./tools/run_game.sh --isolated tower1 --world <world> --map tower1.blv ...` со снимком через
   `debug.screenshot_path` (см. `AGENTS.md`, Native Game Visual Checks).
3. Повторное редактирование: изменить геометрию в Blender, переэкспортировать с теми же именами узлов, пересобрать и
   убедиться, что двери и события сохранились.

Автотест не доказывает, что карту приятно проходить: ручной прогон обязателен.

## Частые ошибки (из опыта Amber Island)

| Симптом | Причина | Где искать |
|---|---|---|
| Игрок застревает | Щели и тонкие пересечения стен, несоосные вершины на стыке комнат | Видео Dev Stream 09, «Collision Test / Fix» |
| Комната не рисуется сквозь проём | Портал не совпадает с контуром проёма или неправильно ориентирован | `Editor BSP.lua:422-431` (ориентация определяет переднюю комнату) |
| Текстура «плывёт» | Поворот и масштаб UV, которых формат не поддерживает | MMEditor Readme |
| Свойства граней пропали после реимпорта | Привязка к вершинам (MMEditor) | В OpenYAMM не менять имена узлов |
