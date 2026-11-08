# ТЗ v2: 56 кадров лица героини-полумедузы (для Codex)

Версия 2, 2026-11-08. Заменяет [v1](portrait-generation-brief.md) для генерации в Codex. Таблица событий и состояний
движка из v1 остаётся верной; кадрирование, направления поворотов и способ работы ниже исправлены по замерам
оригинальных портретов (pc01–pc29, 7pc01–7pc25 из `assets_dev/engine/icons_x2` OpenYAMM).

Исполнитель: Codex со встроенной генерацией изображений и Python (Pillow, numpy). Цель — набор `01.png … 56.png`,
который в игре смотрится не хуже оригинальных лиц партии: та же героиня во всех кадрах, без скачков размера и тона,
анимации плавные. Проверка набора автоматическая (`tools/portrait_kit.py qa`), плюс визуальный отчёт.

---

## 0. Что изменилось относительно v1 и почему

| Было в v1 | По оригиналам | Следствие |
|---|---|---|
| «Голова без шеи, вырезана по контуру волос», подбородок 96 % | Голову видно сквозь **неподвижное мягкое яйцевидное окно**, которое касается нижнего края кадра. У многих героев (pc09, pc10, pc12, pc15, pc18, pc21–24) под подбородком видна **короткая шея**, которая уходит в низ овала. Подбородок на 85–93 % высоты | Шея нужна, но только короткая, до низа овала. Плеч и ключиц нет, горизонтального среза нет. Подбородок на 88 % |
| Повороты меняют позу «по выравниванию в редакторе» | Окно одно и то же во всех кадрах (IoU силуэта с 01 = 0,90–0,99), голова поворачивается внутри него, её размер не меняется. Окно сдвигается только в 35 (на 25 % высоты вниз) и 36 (на 52 %) | Все кадры собираются в одно окно: `compose` |
| Правка по маске в интерфейсе ChatGPT | У Codex нет выделения: генератор всякий раз перерисовывает картинку целиком | Генерируется весь кадр, затем `compose` берёт из него **только** глаза, рот или лицо и вклеивает в мастер. Волосы, змеи и силуэт остаются пиксель в пиксель |
| 18 LookRight — «влево по изображению», 19 — «голова вправо» | pc05, 7pc05, pc02: **18 — глаза (и голова) вправо по изображению, 19 — влево** | В v1 18 и 19 перепутаны. Пункт TODO «18 смотрит не туда» исправляется по этой таблице, не по v1 |
| 25 — поворот влево, 29 — вправо; 30 — подбородок вверх, 33 — вниз | pc02: 25 — лицо повёрнуто вправо по изображению (~35°), 29 — влево; 30 — голова опущена, 33 — чуть поднята | Направления в таблице раздела 6 взяты по pc02 |
| 35 «глаза закрыты, голова на 15 % ниже» | 35: голова наклонена вперёд, глаза открыты и смотрят исподлобья, всё окно опущено на 25 %; 36: видна только макушка | `compose --frame 35/36` сдвигает окно сам |
| Урон 37–39 — синяк и ссадина | Оригиналы резче: голову отбрасывает, видны кровь у губ или носа, синяки, у 39 — запрокинутая голова | Описания усилены |
| Яркость не задана | Средняя яркость головы у оригиналов 80–120 (pc02 — 116). Alpha 0.2 — 84, на 118×158 лицо темнеет | Мастер: 100–125. Кадры выражений — в пределах ±10 от мастера |
| Край альфы 2–4 px | Переход 1–3 px при 118×158 (≈ 14 px на холсте ×8) | Окно в `compose` уже с таким краем |

Недочёты Alpha 0.2, которые этот процесс устраняет: шея с плечами и горизонтальным срезом; голова меньше окна
(занимает 60 % кадра против 69–74 % у оригиналов); жёсткий край альфы; кадры с разных листов отличаются размером и
стилем (21–33 против 01); в кивке 32–33 другое лицо.

## 1. Входные файлы

| Путь (репозиторий `project-medusa`) | Что |
|---|---|
| `tools/portrait_kit.py` | Сборка кадров в окно и проверка набора (раздел 4). Нужны Pillow и numpy |
| `portraits/templates/oval-alpha-944x1264.png` | Альфа-окно, измеренное по 57 оригиналам |
| `portraits/templates/layout-guide-944x1264.png` | Схема: окно, линия зрачков, нос, рот, подбородок (только для глаз генератора, не копировать линии) |
| `portraits/reference/mm/pc02-NN.png`, `pc05-NN.png`, `7pc05-NN.png` | Три полных оригинальных набора (118×158) — образец позы и силы выражения каждого кадра |
| `portraits/reference/mm/pc04/10/12/15/18-01.png` | Примеры шеи в окне |
| `portraits/reference/mm/x4/` | Те же кадры 472×632 — **их** прикладывать к запросам генератору |
| `portraits/generated/master-v2/variant-0N.png` | Прежние кандидаты Codex (только локально, не в git) — можно взять за основу мастера, если пользователь выберет |

`portraits/reference/` не коммитится: это графика игры, а репозиторий публичный (там лежит `.gitignore`).

Окружение: `python3 -m venv "$TMPDIR/portrait-venv" && "$TMPDIR/portrait-venv/bin/pip" install pillow numpy`.
Сборка одного кадра занимает около 5 с CPU, весь набор — 4–5 минут. Пакетную сборку и `qa` запускать через
`safe-heavy-run run -- …` (`/home/plane/AGENTS.md`).

## 2. Холст и геометрия (проверяется автоматически)

Холст **944×1264** (×8 от игровых 118×158), RGBA. Генератор отдаёт около 1129×1393 с прозрачным фоном: это
нормально, на холст кадр переносит `compose`, а не генератор.

| Что | Значение на 944×1264 | Допуск |
|---|---|---|
| Окно | эллипс, центр (472, 640), полуоси 430×622: от x 42 до 902, от y 18 до низа кадра | задаёт `compose` |
| Зрачки | y = 620 (49 %), x = 330 и 614 | ±25 по y, ±30 по x |
| Кончик носа | y = 800 (63 %), на оси x = 472 | ±40 |
| Линия рта | y = 935 (74 %) | ±40 |
| Подбородок | y = 1110 (88 %) | ±45 |
| Шея | от подбородка вниз, сужается вместе с низом окна; уходит в прозрачность по краю окна | без плеч и ключиц, без горизонтального среза |
| Волосы и змеи | заполняют окно до краёв (голова занимает 90–100 % окна); всё, что за окном, обрезается | — |

Оригиналы pc02 (зрачки 612, нос 800, рот 940, подбородок 1120) укладываются в эти числа: это проверено.

## 3. Героиня (неизменная часть, дословно в каждый запрос)

```
CHARACTER LOCK — identical in every image:
Young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face:
oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with
amber-gold irises and normal round human pupils, dark well-shaped arched eyebrows.
Skin: light sage-green tint (about #B8C4A2), smooth, evenly lit, NOT dark or grey.
Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer
cheekbones and down the sides of the neck; the same shape and size on both sides. No scales on the nose, lips or
forehead centre.
Hair: very dark green-black hair with bottle-green highlights, forehead free, no fringe; it falls behind the ears to
just below the jaw on both sides and frames the neck, filling the space beside the neck.
Snakes: exactly FIVE slender living snakes grow from the hair: two at the left temple, two at the right temple, one
coiled on the crown. Emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths.
They stay inside the head outline and never cover the eyes or the face. Same count and placement every time.
Short neck visible under the chin. No shoulders, no collarbones, no clothing, no jewellery.
```

```
STYLE LOCK — identical in every image:
Late-1990s Might and Magic VIII party portrait, remastered: pre-rendered 3D CG head, smooth broad shading, clear
readable facial planes, restrained specular highlights, soft frontal studio light slightly from the upper left,
warm neutral tone. Not a photograph, not a painting, no brush strokes, no outline.
Front view, camera at eye level. The head fills a tall portrait frame: top of the hair near the top edge, pupils
just below the middle of the height, chin at about 88 % of the height, short neck below it.
Transparent background. One head only: no sheet, no grid, no text, no frame, no guide lines, no shadow.
```

```
NEGATIVE:
reptile face, slit pupils, snake eyes, fangs, forked tongue, monster, snake body, tail, extra snakes, snakes over
the face, horns, extra eyes, shoulders, collarbones, clothing, jewellery, crown, background scene, vignette, drop
shadow, text, watermark, frame, border, guide lines, sprite sheet, cartoon, anime, painterly, photo, dark moody
lighting, different hairstyle, different face, changed head size.
Never use pure magenta #FF00FF or pure cyan #00FFFF.
```

## 4. Инструмент `tools/portrait_kit.py`

| Команда | Что делает |
|---|---|
| `mask --out portraits/templates` | Пишет окно и схему (уже лежат в репозитории) |
| `grid IMAGE --out G.png [--crop X0 Y0 X1 Y1]` | Сетка с координатами поверх картинки: по ней Codex считывает зрачки, нос, рот, подбородок |
| `compose RAW --kind master --pupils LX LY RX RY --out final/01.png` | Ставит мастер на холст: зрачки — в канонические точки, окно — по шаблону |
| `regions final/01.png --out R.png` | Показывает области вклейки «глаза» и «рот» по `final/landmarks.json` |
| `compose RAW --kind eyes\|mouth\|face --master final/01.png --out final/NN.png` | Совмещает сгенерированный кадр с мастером по волосам и контуру (масштаб, поворот, сдвиг), подгоняет цвет и вклеивает **только** область. Печатает `registration score` |
| `compose RAW --kind head --master … --out …` | Кадры цвета (08, 09, 12, 54): вся голова из нового кадра, силуэт мастера |
| `compose RAW --kind pose --master … --frame NN --out …` | Новая поза в том же окне: размер и верх головы — как у мастера, тон подогнан. `--frame 35/36` опускает окно |
| `qa final --reference portraits/reference/mm [--partial]` | Проверки (ниже) и материалы для просмотра в `final/qa/`. Код выхода 1 при любом FAIL |

`final/landmarks.json` (пишет Codex после утверждения мастера, по `grid`):

```json
{"pupil_left": [330, 620], "pupil_right": [614, 620], "brow_y": 545, "nose_tip": [472, 800],
 "mouth_left": [380, 935], "mouth_right": [565, 935], "chin": [472, 1110]}
```

Инструмент проверен на оригинальных кадрах pc02: 55 кадров, случайно сдвинутых (±40 px), повёрнутых (±3°) и
масштабированных (0,90–1,12) на холсте 1129×1393, собраны обратно и совпали с оригиналом. На копиях мастера
остаточная разница в области лица — 2–5 из 255, это сглаживание при пересчёте.

### Что проверяет `qa`

- 56 файлов, 944×1264, RGBA; нет пикселей чистых `#FF00FF` и `#00FFFF`.
- Ничего непрозрачного за окном; низ — не прямой срез; голова заполняет окно.
- Мастер: координаты из `landmarks.json` в допусках раздела 2; яркость головы 95–140 (FAIL) или 100–125 (норма).
- Кадры выражений: волосы, змеи и контур совпадают с 01 (средняя разница ≤ 2,5), лицо при этом изменилось.
- Все кадры, кроме 35/36: IoU силуэта с 01 ≥ 0,90; площадь ±6 % (поза ±8 %); тон ±10 (поза и урон ±22).
- 35/36: окно опущено на 9–17 % и 20–34 % (как в оригиналах).
- 08 желтее 01, 09 краснее, 12 серый камень (насыщенность ≤ 0,12, FAIL), 54 покраснел.
- «Нет» 25→29: центр яркости лица идёт в одну сторону, а крайние кадры — в разные (предупреждение: лишь
  приближение, подтверждать анимацией).

Материалы в `final/qa/`: `sheet-game-size.png` (набор в размере игры, под каждым кадром — тот же номер у pc02),
`sheet-x2.png`, `diff-vs-01.png` (что изменилось относительно 01: у кадров выражений вне лица должно быть темно),
`anim-blink/talk/no/yes/dodge/damage/wake/look.gif` с таймингами игры (единица — 1/16 с: моргание и кадры «нет»/«да»
идут по 125 мс, поэтому любой скачок размера заметен), `report.txt`.

## 5. Порядок работы

Рабочая папка: `portraits/med01/v2/` → `raw/` (всё, что вернул генератор: `NN-a.png`, `NN-b.png` …),
`final/` (01–56 и `landmarks.json`), `prompts.jsonl` (номер кадра, попытка, вложения, промпт, score, решение),
`review.md` (раздел 7).

### Шаг 1. Мастер (кадр 01) — единственная остановка для пользователя

1. Сгенерировать 4 кандидата: промпт M (ниже), вложения — `x4/pc02-01.png` и `x4/pc12-01.png` (как образец стиля,
   окна и шеи) и `templates/layout-guide-944x1264.png` (только пропорции). Если пользователь назвал основу (например,
   `master-v2/variant-06.png`), приложить её как образ лица.
2. Каждого кандидата поставить на холст: `grid` → координаты зрачков → `compose --kind master`.
3. Показать пользователю лист из 4 кандидатов в размере 118×158 и ×2 рядом с `pc02-01` и `pc12-01`, с числами
   яркости и заполнения окна. **Ждать выбора.** Если пользователь заранее разрешил выбирать самому — взять кандидата
   с лучшим сходством со стилем MM8, яркостью 100–125 и ровно пятью змеями, записать выбор в `review.md`.
4. Для выбранного: `final/landmarks.json` по `grid`; `regions` — области не должны задевать волосы и змей;
   `qa final --partial` — FAIL 0.

Промпт M:

```
Create ONE image: frame 01 (the MASTER) of a 56-frame RPG party portrait set. Every later frame is made from it.
[CHARACTER LOCK]
[STYLE LOCK]
Expression: calm neutral face, relaxed closed lips, eyes looking straight at the viewer, alert and confident.
Snakes calm.
Attachments: the original game portraits show ONLY the rendering style, the tall oval head framing that fills the
image and how a short neck sits under the chin; do not copy their faces or hair. The grey layout guide shows only
proportions (pupil line, nose, mouth, chin); never draw its lines.
Do not: [NEGATIVE]
```

### Шаг 2. Ракурсы героини (не кадры, а образцы для поз)

Четыре изображения с мастером во вложении: голова повёрнута на 35° вправо по изображению, на 35° влево, поднята
на 15°, опущена на 25° (вид на макушку). Только для вложений к кадрам «pose»: в набор не входят.

### Шаг 3. Кадры выражений и цвета (37 шт.)

Для каждого кадра с видом `eyes`, `mouth`, `face`, `head` (таблица раздела 6):

1. Промпт E, вложения: `final/01.png` (мастер) и `x4/pc02-NN.png` (образец силы выражения, не лица).
2. `compose RAW --kind <вид> --master final/01.png --out final/NN.png`.
3. Если `registration score` < 0,60 — генератор изменил причёску или наклон: повторить, добавив «the head, hair and
   snakes must be pixel-identical to the attached master», или сузить вид (`face` → `eyes` + `mouth` двумя проходами:
   сначала глаза в мастер, затем рот в результат, передав его как `--master`). Тогда `landmarks.json` положить рядом
   с промежуточным файлом.
4. Посмотреть кадр ×2 и в размере игры рядом с `pc02-NN`; выражение должно читаться на 118×158.

Промпт E:

```
Edit the attached master portrait. Return the SAME image: same person, same head position, size and angle, same
hair and the same five snakes, same lighting and transparent background. Change ONLY the facial expression:
<CHANGE из таблицы>.
The second attachment is an original game portrait showing ONLY how strong this expression should be; do not copy
its face.
[CHARACTER LOCK]
Do not: [NEGATIVE]
```

Для `head` (08, 09, 12, 54) вместо «Change ONLY the facial expression» — «Change the colour and surface of the whole
head as described, keep the outline». Для 12 — вся голова, волосы и змеи из камня.

### Шаг 4. Кадры поз (18 шт.)

1. Промпт P, вложения: `final/01.png`, подходящий ракурс из шага 2, `x4/pc02-NN.png` (образец позы).
2. `compose RAW --kind pose --master final/01.png --frame NN --out final/NN.png`.
3. Последовательности делать подряд и сразу проверять анимацией: 25–29 (`anim-no.gif`), 30–33 (`anim-yes.gif`),
   34–36 (`anim-dodge.gif`). Крайние кадры (25/29, 30/33) — зеркальны по силе; 26/28 — ровно посередине.
4. 36 = тот же сгенерированный исходник, что для 35, собранный с `--frame 36` (видна только макушка, как у оригиналов).
   Если окно открывает лоб — сгенерировать голову, опущенную сильнее (вид на макушку из шага 2).

Промпт P:

```
Create ONE image: frame NN of the same character's portrait set. The first attachment is the master frame of this
exact character: the same person, the same render style, lighting and head size.
[CHARACTER LOCK]
[STYLE LOCK]
Pose change (the only difference from the master): <CHANGE из таблицы>. The head stays the same size and stays
inside the same tall oval framing; only its angle changes. The original game portrait attached shows ONLY the pose
and its strength; do not copy its face.
Do not: [NEGATIVE]
```

### Шаг 5. Проверка и самооценка

1. `qa portraits/med01/v2/final --reference portraits/reference/mm` → **FAIL 0**. WARN разобрать в `review.md`
   (исправлено / принято и почему).
2. Посмотреть `sheet-game-size.png`, `sheet-x2.png`, `diff-vs-01.png` и все `anim-*.gif`; ответить на вопросы
   раздела 7 в `review.md`.
3. Переделать каждый кадр, где ответ «нет». На кадр — не больше 4 попыток; если всё ещё «нет» — лучший вариант
   в набор, кадр в список «на доработку» в `review.md`.
4. `python3 tools/import_portraits.py portraits/med01/v2/final --dry-run`. Сам импорт в пакет, коммит и сборка — только
   по слову пользователя.

## 6. Таблица кадров

Вид: `eyes`/`mouth`/`face` — вклейка области в мастер; `head` — цвет всей головы; `pose` — новая поза. Направления —
**по изображению**, как видит зритель. Образец — `pc02-NN` (для 17–20 смотреть также `pc05-NN`).

| № | Движок | Вид | CHANGE (EN, в промпт) | Проверить |
|---|---|---|---|---|
| 01 | Normal | master | (промпт M) | Раздел 2; яркость 100–125 |
| 02 | Cursed | face | gloomy cursed look: heavy half-lowered eyelids, eyes looking down, slight frown, faint grey shadows under the eyes | Взгляд вниз читается |
| 03 | Weak | face | exhausted and weak: eyelids almost closed, sad drooping brows, mouth slightly open and slack | — |
| 04 | Sleep | pose | asleep: eyes fully closed, face relaxed, lips slightly parted; head rolled about 15° so the crown leans to the LEFT side of the image, chin slightly down; snakes asleep on the hair | Как pc02-04 |
| 05 | Fear | face | terrified: eyes wide open, eyebrows raised high, mouth open in a gasp; snakes tense | — |
| 06 | Drunk | face | tipsy: lopsided silly half-smile, unfocused half-closed eyes, light pink flush on the cheeks | — |
| 07 | Insane | face | manic: wide toothy grin, wild staring eyes, brows raised unevenly | — |
| 08 | Poisoned | head | poisoned: sickly yellow-green skin clearly yellower than normal, sweaty sheen, nauseous half-closed eyes, mouth slightly open | `qa`: желтее 01 |
| 09 | Diseased | head | diseased: red inflamed blotches and small pustules on the forehead and cheeks, puffy skin, one eye squinting, miserable | `qa`: краснее 01 |
| 10 | Paralyzed | face | paralyzed: frozen blank stare, eyes wide open and fixed, face completely slack | — |
| 11 | Unconscious | pose | unconscious: same head roll as frame 04, eyes closed, mouth slack, dark purple bruise around her right eye (the eye on the LEFT side of the image) | Как pc02-11 |
| 12 | Petrified | head | the whole head — skin, hair and all five snakes — is matte grey granite, no colour, eyes closed, serene | `qa`: насыщенность ≤ 0,12 |
| 13 | Blink | eyes | both eyes closed naturally, nothing else changes | Только веки |
| 14 | Wink | face | her right eye (LEFT side of the image) closed in a wink, faint playful smile at one mouth corner | — |
| 15 | MouthOpenRandom | mouth | lips slightly parted | — |
| 16 | PurseLipsRandom | mouth | lips pressed together and slightly pursed | — |
| 17 | LookUp | eyes | eyes looking up, upper eyelids raised, head unchanged | Как pc05-17 |
| 18 | LookRight | pose | head turned about 15° toward the RIGHT side of the image, eyes looking further RIGHT | Вправо по изображению (pc05-18) |
| 19 | LookLeft | pose | head turned about 15° toward the LEFT side of the image, eyes looking further LEFT | Влево по изображению (pc05-19) |
| 20 | LookDown | eyes | eyes looking down, upper lids lowered, pupils still visible (eyes NOT closed) | Не путать с морганием |
| 21 | Talk | mouth | speaking, mouth slightly open as for "eh" | Кадр 125 мс: отличие от 01 только во рту |
| 22 | MouthOpenWide | mouth | speaking, mouth open as for "ah" | — |
| 23 | MouthOpenA | mouth | speaking with a slight smile, mouth open as for "ee", upper teeth visible | — |
| 24 | MouthOpenO | mouth | speaking, lips rounded as for "oo" | — |
| 25 | No, крайний | pose | head turned (yaw) about 35° toward the RIGHT side of the image, mild disapproval, mouth closed | Как pc02-25 |
| 26 | No | pose | head turned about 15° toward the RIGHT side of the image, mild disapproval | Посередине между 27 и 25 |
| 27 | No, центр | mouth | slight disapproving press of the lips | Голова = мастер |
| 28 | No | pose | head turned about 15° toward the LEFT side of the image, mild disapproval | Зеркально 26 |
| 29 | No, крайний | pose | head turned about 35° toward the LEFT side of the image, mild disapproval | Зеркально 25 |
| 30 | Yes, вниз | pose | head nodded DOWN about 12° (forehead toward the viewer), eyes still on the viewer, pleasant agreeable look | Как pc02-30 |
| 31 | Yes | pose | head nodded down about 5°, pleasant agreeable look | Между 01 и 30 |
| 32 | Yes | pose | chin raised about 3°, pleasant agreeable look | — |
| 33 | Yes, вверх | pose | chin raised about 8°, pleasant agreeable look | Как pc02-33 |
| 34 | AvoidDamage | pose | dodging: head pulled back and turned about 20° toward the RIGHT side of the image, brows knitted, mouth open | Как pc02-34 |
| 35 | AvoidDamage | pose | ducking: head bowed forward about 25°, eyes open glaring up from under the brows | `--frame 35`: окно на 25 % ниже |
| 36 | AvoidDamage | pose | исходник кадра 35 (см. шаг 4) | `--frame 36`: видна только макушка |
| 37 | DamageReceivedMinor | pose | hit: head knocked about 25° toward the LEFT side of the image and tilted, eyes squeezed, mouth open in a grimace, a little blood at the lip corner | Как pc02-37 |
| 38 | DamageReceivedModerate | pose | hit hard: head knocked down and toward the RIGHT side of the image, eyes shut tight, bruise on the cheek, blood from the nose and lips | Как pc02-38 |
| 39 | DamageReceivedMajor | pose | severe hit: head thrown back about 20°, mouth open in pain, purple bruises around one eye and the cheek, blood at the mouth | Как pc02-39; голова не выходит из окна |
| 40 | Smile | face | warm closed-mouth smile, friendly eyes | — |
| 41 | WideSmile | face | wide happy open smile showing upper teeth, eyes crinkled | — |
| 42 | Sad | face | displeased and sad: brows drawn together and down, mouth turned down, eyes lowered slightly | — |
| 43 | CastSpell | face | concentrating on a spell: eyes closed, brows slightly knitted, lips calm | — |
| 44 | Portrait41 | face | shocked pain: eyes wide, brows raised, mouth open in "ah!" | — |
| 45 | Portrait42 | face | wincing "ooh": lips pushed forward, brows raised, eyes half-closed | — |
| 46 | Portrait43 | face | puzzled: one eyebrow raised, the other lowered, lips pressed to one side | — |
| 47 | Portrait44 | face | pleading: eyes closed, brows raised in the middle, sad soft mouth | — |
| 48 | Portrait45 | face | smug: confident closed-mouth smirk, eyelids slightly lowered | — |
| 49 | Scared | face | alarmed shout: brows drawn down and together, eyes wide, mouth wide open yelling | — |
| 50 | Portrait47 | face | proud triumph: big bright open smile, eyes shining | — |
| 51 | Portrait48 | face | annoyed disappointment: scowl, brows knitted, mouth tight | — |
| 52 | Portrait49 | face | skeptical: eyes glancing toward the RIGHT side of the image, one eyebrow raised | — |
| 53 | Portrait50 | face | angry glare: brows low, eyes narrowed, lips tight | — |
| 54 | Portrait51 | head | straining with effort: face flushed red, teeth clenched and bared, eyes squeezed nearly shut | `qa`: покраснение |
| 55 | Portrait52 | face | cheerfully drunk laugh: big open laughing smile, happy eyes, light pink cheeks | Голова прямо (как pc02-55) |
| 56 | Portrait53 | face | surprised awe: eyes wide, brows high, mouth open round "oh!" | — |

Итого: master — 1; eyes — 3 (13, 17, 20); mouth — 7 (15, 16, 21–24, 27); face — 23; head — 4 (08, 09, 12, 54);
pose — 17 (04, 11, 18, 19, 25, 26, 28–35, 37–39) + 36 из исходника 35.

## 7. Визуальная самопроверка (`review.md`)

Ответить «да/нет» с номерами кадров; каждое «нет» — переделка (шаг 5.3).

1. На `sheet-game-size.png` все 56 кадров — одна и та же героиня (форма лица, глаза, тон кожи, чешуя, причёска)?
2. Ровно пять змей на тех же местах во всех кадрах, кроме поз, где часть закрыта поворотом?
3. Каждое выражение читается в 118×158 так же уверенно, как у `pc02` под ним?
4. `anim-blink`, `anim-talk`: при смене кадров двигаются только веки или рот, без вспышек и сдвигов?
5. `anim-no`: голова плавно ходит вправо-влево без скачков размера, крайние положения равны?
6. `anim-yes`: плавный кивок, лицо то же, что в 01?
7. `anim-dodge`: голова уходит вниз за край окна и возвращается без рывка вбок?
8. `anim-damage`: урон заметно сильнее от 37 к 39, голова не выходит за окно?
9. 18 смотрит вправо по изображению, 19 — влево; 52 косится вправо?
10. Нет шва по краю вклейки (`sheet-x2.png`): ни ореола, ни ступеньки тона у бровей и вокруг рта?
11. Нигде не видно плеч, ключиц, одежды, фона, текста, линий схемы; низ — мягкий край окна?
12. Тон 01 близок к оригиналам: лицо не темнее pc02 и не теряется на тёмной рамке HUD?

## 8. Готово, когда

- `qa` без `--partial`: **FAIL 0**; все WARN разобраны в `review.md`.
- Ответы раздела 7 — «да», или кадр внесён в список на доработку с причиной.
- `import_portraits.py --dry-run` проходит.
- В `portraits/med01/v2/` есть `raw/`, `final/`, `prompts.jsonl`, `review.md`, `final/qa/`. В коммит не попадает
  `portraits/reference/`.
