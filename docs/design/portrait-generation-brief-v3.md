# ТЗ v3: портрет героя партии — генерация и пакет для импорта в игре

Версия 3, 2026-11-10. Продолжает [v2](portrait-generation-brief-v2.md): **генерация кадров не меняется**, по v2
сделан набор Medusa v2 (`portraits/med01/v2/`, Alpha 0.2.2). v3 добавляет второй этап — пакет портрета, который
игрок добавляет в OpenYAMM кнопкой **Choose Portrait → Add Portrait...** (функция для апстрима, ветка
`feature/custom-portrait-import` форка `Plane-PPP/openyamm`; описание движка —
[`devdocs/CUSTOM_PORTRAITS.md`](https://github.com/Plane-PPP/openyamm/blob/feature/custom-portrait-import/devdocs/CUSTOM_PORTRAITS.md)).

Два этапа разделены:

| Этап | Результат | Кто и чем | Проверка |
|---|---|---|---|
| 1. Генерация | 56 кадров `01.png … 56.png`, **944×1264** RGBA, одно окно-овал | Codex по [v2](portrait-generation-brief-v2.md), разделы 1–8; `tools/portrait_kit.py compose/qa` | `qa` — FAIL 0, `review.md` |
| 2. Пакет | папка: `portrait.yml` + `01.png … 56.png` **118×158** 8-bit RGBA | `tools/make_portrait_package.py` движка (ниже) | импорт в игре: кнопка сама проверяет пакет |

Для пакета Project Medusa (ruleset, `med01-`) по-прежнему используется `tools/import_portraits.py` этого
репозитория; пакет импорта — для любого героя без ruleset и без пересборки игры.

## 1. Что требует игра (подтверждено кодом движка)

| Что | Значение |
|---|---|
| Кадры | ровно 56, `01.png … 56.png`; номер кадра = номер текстуры из `portrait_frame_data.txt` (таблица кадров — [v2, раздел 6](portrait-generation-brief-v2.md#6-таблица-кадров)) |
| Размер | **118×158** (×2 к оригинальным 59×79); упаковщик уменьшает 944×1264 (Lanczos) |
| Формат | PNG, 8 бит, **RGBA** (тип цвета 6); фон прозрачный, мягкий край альфы |
| Запрещено | чистые `#FF00FF` и `#00FFFF` (движок делает их прозрачными; упаковщик убирает их из почти прозрачных краёв) |
| Смерть, стирание | не рисуются: общие `DEAD` / `ERADCATE` |
| Кукла, раса, пол, голос | **не из пакета**: их даёт базовый персонаж `base_character` — строка `character_data.txt` |

## 2. Метаданные `portrait.yml`

```yaml
schema: 1
id: medusa              # 1–32 символа a-z 0-9 _ ; имена файлов в игре: user_medusa-01 … -56
name: "Medusa"          # имя для сообщений игры, до 48 символов
base_character: 2       # строка character_data.txt: кукла, раса, пол, класс и голос по умолчанию
```

Как выбрать `base_character`: строка с той же расой и полом, что у героя, доступная при старте
(`Available at start` = `x`, есть `Race`). Портрет появится в выборе там же, где предлагается эта строка (те же
континенты, расы и классы). Для героини-полумедузы — **2** (человек, женщина, кукла `pc02`; с неё же скопирована
строка 79 Project Medusa).

## 3. Порядок упаковки

1. Этап 1 по v2 закончен: `final/01.png … 56.png`, `qa` без FAIL.
2. Упаковать (нужен Pillow):

   ```sh
   python3 tools/make_portrait_package.py portraits/med01/v2/final \
       --id medusa --name "Medusa" --base-character 2 --output medusa_portrait --zip
   ```

   `tools/make_portrait_package.py` лежит в репозитории движка (ветка `feature/custom-portrait-import`). Скрипт
   проверяет 56 кадров и пропорцию 59:79, уменьшает до 118×158, убирает ключевые цвета, пишет `portrait.yml`;
   `--zip` дополнительно создаёт `medusa_portrait.zip` с фиксированными датами (одни и те же кадры дают одни и те же
   байты).
3. Импорт: распаковать ZIP, в игре New Game → создание партии → портрет → **Choose Portrait** →
   **Add Portrait...** → выбрать папку `medusa_portrait`. Игра проверяет пакет и пишет причину, если он не подходит.

## 4. Готово, когда

- Этап 1 — по [v2, раздел 8](portrait-generation-brief-v2.md#8-готово-когда).
- Упаковщик отработал без ошибок; в папке пакета 57 файлов (`portrait.yml` и 56 кадров).
- Пакет импортируется в игре; портрет виден в выборе, в нижней панели после старта и после загрузки сохранения.

## Готовый пакет Medusa для проверки импорта

Собран из кадров v2 этого репозитория (`content/engine/rulesets/medusa/icons_x2/med01-NN.png` → `NN.png`),
`--id medusa --name "Medusa" --base-character 2 --zip`; перегенерация не нужна. Готовый файл:
[`portraits/packages/medusa_portrait.zip`](../../portraits/packages/medusa_portrait.zip), SHA256
`6608db58bfe28500884bbe1ece8417212678c10b9eea77a04ea24bd869fbd19a` (две сборки подряд дают один и тот же ZIP).
