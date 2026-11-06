# ТЗ: лицо героини-полумедузы (56 кадров портрета)

Версия 1, 2026-11-06. Для генерации в ChatGPT (GPT-image), Midjourney, Stable Diffusion/ComfyUI и т. п.
Данные о формате сверены с игрой (OpenYAMM `feature/project-medusa` @ `2c1ae60`): **[проверено]** — по файлам игры.

---

## 1. Что требует игра

| Параметр | Значение | Источник |
|---|---|---|
| Число кадров | **56**, номера `01`…`56` | `portrait_frame_data.txt` (текстуры 1–56) **[проверено]** |
| Размер кадра в игре | **118×158 px** (×2 к оригинальным 59×79), пропорция **59:79 = 0,747** | `pc02-01.png`, `faces_pc02.yml` **[проверено]** |
| Формат | PNG, **RGBA**, 8 бит; фон **прозрачный** | `pc02-01.png` **[проверено]** |
| Альфа | внутри 252–253, край растушёван на 2–4 px | гистограмма альфы `pc02-01` **[проверено]** |
| Хранение у оригиналов | `engine/icons_x2/pcNN-01.png … -56.png` + атлас `faces_pcNN.oytex/.yml` (8 колонок) | **[проверено]** |
| Хранение у Medusa | `content/engine/rulesets/medusa/icons_x2/med01-01.png … med01-56.png`; атлас не нужен | **[проверено]** тестом |
| Запрещённые цвета | чистые `#FF00FF` и `#00FFFF` (движок делает их прозрачными) | `GameplayHudCommon.cpp` **[код]** |
| Смерть / стирание | **не рисовать**: общие картинки `DEAD`/`ERADCATE` для всех героев | `GameplayUiRuntime.cpp` **[код]** |

**Сдавать:** 56 файлов `01.png … 56.png`, **944×1264 px** (×8) или любой больший размер той же пропорции 59:79,
RGBA с прозрачным фоном (если генератор не умеет — ровный серый `#808080`, без тени и градиента).
Дальше `python3 tools/import_portraits.py <папка>` уменьшит до 118×158 и положит в игру.

## 2. Кадрирование (одинаково во всех кадрах, кроме отмеченных «поза»)

Измерено по оригиналам; шаблон: `portraits/templates/guide-944x1264.png` (прозрачная накладка для редактора) и
`guide-944x1264-on-grey.png` (то же на сером — вложение для генератора).

| Линия | % высоты (от верха) | px на 944×1264 |
|---|---|---|
| Верх волос/змей | 2,5 % | 32 |
| Линия волос на лбу | 20 % | 253 |
| Брови | 42 % | 531 |
| **Линия зрачков** | **49 %** | **620** |
| Кончик носа | 63 % | 796 |
| Линия рта | 74 % | 935 |
| Подбородок | 96 % | 1213 |

- Голова **без шеи и плеч**: вырезана по контуру волос и линии подбородка, как «парящая» голова (см. оригиналы).
- Силуэт головы (волосы со змеями) — овал от 5 % до 97 % ширины; ничего не выходит за края кадра.
- Нос на вертикальной оси (50 % ширины); зрачки на 35 % и 66 % ширины.
- Ракурс — **почти анфас**, взгляд в зрителя; свет студийный мягкий, ключевой сверху-слева, без жёстких теней.

## 3. Персонаж (неизменная часть — копировать в каждый запрос дословно)

Блок **CHARACTER LOCK** (англ., для генератора):

```
CHARACTER LOCK — identical in every image:
Young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face:
oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with
amber-gold irises and normal round human pupils, dark well-shaped arched eyebrows.
Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores.
Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer
cheekbones; the same shape and size on both sides in every image. No scales on the nose, lips or forehead centre.
Hair: very dark green-black hair with deep bottle-green highlights, pulled back from the face, close to the head,
ending at jaw level; no fringe; the forehead is free.
Snakes: exactly FIVE slender living snakes grow from the hair and are part of the hairstyle: two at the left
temple, two at the right temple, one coiled on the crown. Snakes are emerald green with a pale gold belly and a
thin black stripe; small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or
the face. Same count and placement in every image.
No jewellery, no makeup effects, no clothing, no neck, no shoulders.
```

Блок **STYLE & FRAME LOCK**:

```
STYLE & FRAME LOCK — identical in every image:
Late-1990s Might and Magic VII/VIII party portrait, remastered: semi-realistic 3D CG render, soft studio light
from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline.
Head only: cut out along the hair silhouette and under the chin, no neck, no shoulders, floating head on a fully
transparent background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient).
Portrait canvas 944x1264 (ratio 59:79). Front view, camera at eye level, straight on.
Exact framing: top of the hair/snakes at 2.5% of the height, eye line (pupils) at 49%, nose tip at 63%, mouth at
74%, chin at 96%. Nose on the vertical centre line. Pupils at 35% and 66% of the width. The head silhouette spans
5–97% of the width. Same head size and position as the reference master image.
No text, no frame, no border, no watermark, no background objects, no guide lines.
```

**NEGATIVE** (для систем с отрицательным промптом; в ChatGPT — фразой «Do not …»):

```
reptile face, snake eyes, slit pupils, fangs, forked tongue, monster, full snake body, tail, extra snakes,
snakes covering face, horns, extra eyes, extra limbs, neck, shoulders, clothing, jewellery, crown, background
scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon, anime, painterly, sketch,
different hairstyle, different face, changed head size, changed head position, cropped head, tilted camera
```

## 4. Таблица кадров (полная, по данным игры)

Колонки: **№** — номер файла; **Движок** — `PortraitId` из `portrait_frame_data.txt`; **Когда** — состояние или
события из `face_animations.txt`; **Метод** — как генерировать (раздел 5): **М** — правка маски лица на мастере
(поза и размер не меняются), **Ц** — правка цвета/фактуры всей головы, **П** — новая поза (полная генерация +
выравнивание). Повороты: «влево/вправо» — **по изображению** (как видит зритель).

### 4.1 Состояния (держатся, пока действует состояние)

Приоритет показа, если состояний несколько: Petrified → Unconscious → Paralyzed → Asleep → Insane → Fear → Disease
→ Poison → Weak → Cursed → Drunk (смерть и стирание — общие картинки). **[код]** `GameMechanics::displayedCondition`.

| № | Движок | Когда | Что нарисовать (EN, вставлять в «CHANGE ONLY») | Метод |
|---|---|---|---|---|
| 01 | Normal | Обычное лицо; первый кадр уклонения | **MASTER.** Calm neutral expression, relaxed lips closed, eyes looking straight at the viewer, alert and confident. Snakes calm. | мастер |
| 02 | Cursed | Проклятие | Gloomy cursed look: heavy half-lowered eyelids, eyes looking down, slight frown, dull tired skin with faint grey shadows under the eyes. | М |
| 03 | Weak | Слабость (в т. ч. от усталости без отдыха) | Exhausted and weak: eyelids almost closed, sad drooping brows, mouth slightly slack, head lowered about 5°. Snakes droop. | М |
| 04 | Sleep | Сон | Asleep: eyes fully closed, face totally relaxed, lips slightly parted; head tilted about 20° toward the right side of the image and lowered a little. Snakes asleep, resting on the hair. | П |
| 05 | Fear | Страх; первый кадр пробуждения (05→19→18) | Terrified: eyes wide open, eyebrows raised high, mouth open in a gasp. Snakes reared up and tense (still inside the silhouette). | М |
| 06 | Drunk | Опьянение | Tipsy: lopsided silly half-smile, unfocused half-closed eyes, cheeks slightly flushed pink, head tilted about 8°. | М |
| 07 | Insane | Безумие | Manic: wide toothy grin, wild staring eyes, eyebrows raised unevenly. | М |
| 08 | Poisoned | Отравление (все степени) | Poisoned: sickly yellow-green skin, clearly yellower and darker than her normal sage tint, sweaty sheen, nauseous half-closed eyes, mouth slightly open. | Ц+М |
| 09 | Diseased | Болезнь (все степени); при болезни+отравлении показывается он | Diseased: red inflamed blotches and small pustules on the forehead and cheeks, puffy skin, one eye squinting, miserable expression. | Ц+М |
| 10 | Paralyzed | Паралич | Paralyzed: frozen blank stare, eyes wide open and fixed, face completely slack, faint bluish-grey pallor. | М |
| 11 | Unconscious | Без сознания и HP ≤ 0 | Unconscious: eyes closed, mouth slack, dark bruise around one eye; head lolled about 25° toward the right side of the image and slightly down. Snakes limp. | П |
| 12 | Petrified | Окаменение | Petrified: the whole head — skin, hair and all five snakes — turned into matte grey granite stone, no colour at all, eyes closed, serene face. Same silhouette. | Ц |

«Усталость» отдельного кадра не имеет: состояние Weak = кадр 03, событие Tired = 42 или 51.

### 4.2 Холостые движения и речь (короткие кадры)

| № | Движок | Когда | Что нарисовать | Метод |
|---|---|---|---|---|
| 13 | Blink | Моргание (очень короткий кадр) | Exactly the master, both eyes closed naturally. Nothing else changes. | М |
| 14 | Wink | Случайно | Exactly the master, her right eye (left side of the image) closed in a wink, faint playful smile at one corner. | М |
| 15 | MouthOpenRandom | Случайно | Master expression, lips slightly parted. | М |
| 16 | PurseLipsRandom | Случайно | Master expression, lips pressed together and slightly pursed. | М |
| 17 | LookUp | Взгляд вверх (событие LookUp) | Eyes looking up, chin raised about 5°. | М |
| 18 | LookRight | Взгляд в сторону; 3-й кадр пробуждения | Eyes turned to the LEFT side of the image, head turned about 10° the same way. | М |
| 19 | LookLeft | Взгляд в сторону; 2-й кадр пробуждения | Head turned about 25° toward the RIGHT side of the image, eyes looking the same way. | П |
| 20 | LookDown | Взгляд вниз | Eyes looking down, eyelids lowered, head unchanged. | М |
| 21 | Talk, PurseLips1–3, Portrait54 | Речь; вход/выход из подземелья, пожертвование | Speaking, mouth slightly open as for "eh", relaxed. | М |
| 22 | MouthOpenWide, Portrait55 | Речь | Speaking, mouth open as for "ah". | М |
| 23 | MouthOpenA, Portrait56 | Речь | Speaking with a slight smile, mouth open as for "ee", upper teeth visible. | М |
| 24 | MouthOpenO, Portrait57 | Речь | Speaking, lips rounded as for "oo". | М |

### 4.3 Покачивание «нет» (25–29) и кивок «да» (30–33)

Последовательность «нет» в игре: 27, 26, 25, 26, 27, 28, 29, 28, 27 (магазин закрыт, нельзя нести, дверь заперта,
не хватает золота, нельзя отдыхать и т. д.). «Да»: 32, 33, 32, 31, 30, 31 (выучено заклинание, поездка).
Лицо во всех — то же спокойное, рот закрыт; меняется только поворот головы. Размер головы — как у мастера.

| № | Что нарисовать | Метод |
|---|---|---|
| 25 | Head turned (yaw) about 25° toward the LEFT side of the image, mild disapproval. | П |
| 26 | Head turned about 12° toward the LEFT side of the image. | П |
| 27 | Head straight (= master pose), slight disapproving press of the lips. | М |
| 28 | Head turned about 12° toward the RIGHT side of the image. | П |
| 29 | Head turned about 25° toward the RIGHT side of the image. | П |
| 30 | Chin raised about 10° (head tilted back), pleasant agreeable look. | П |
| 31 | Chin raised about 4°, pleasant agreeable look. | П |
| 32 | Chin lowered about 6°, pleasant agreeable look. | П |
| 33 | Chin lowered about 15°, eyes still on the viewer from under the brows. | П |

### 4.4 Уклонение и урон

Уклонение: 01, 34, 35, 36, 35, 34 — голова уходит вниз и в сторону от удара.

| № | Движок | Когда | Что нарисовать | Метод |
|---|---|---|---|---|
| 34 | AvoidDamage | Уклонение | Dodging: head jerked about 20° toward the RIGHT side of the image and slightly down, eyes squinting. | П |
| 35 | AvoidDamage | Уклонение | Ducking: head dropped about 15% of the frame height lower and turned about 30° to the right, eyes shut. | П |
| 36 | AvoidDamage | Уклонение | Deep duck: only the top of the head (hair and snakes) visible in the lower-left part of the frame; the face is below the frame. | П |
| 37 | DamageReceivedMinor | Лёгкий урон | Hit: head knocked about 15° toward the RIGHT side of the image, eyes closed in a wince, small bruise on one cheek. | П |
| 38 | DamageReceivedModerate | Средний урон | Hit hard: head knocked down about 15° and to the right, eyes shut tight, bruise and a small cut on the cheek. | П |
| 39 | DamageReceivedMajor | Сильный урон | Severe hit: head thrown back about 20° and turned, teeth clenched in a pained grimace, bruising on cheek and eye. | П |

### 4.5 Эмоции и реакции

| № | Движок | Когда (события игры) | Что нарисовать | Метод |
|---|---|---|---|---|
| 40 | Smile | Приветствие, удачный удар, находка, покупка/продажа, рост навыка, найм, выпивка, угроза | Warm closed-mouth smile, eyes friendly. | М |
| 41 | WideSmile | То же + награда, квест, зелье, ремонт, лечение | Wide happy open smile showing upper teeth, eyes crinkled. | М |
| 42 | Sad | Усталость, провал заклинания, неудачный ремонт, нехватка маны, грубый торговец, выстрел | Displeased and sad: brows drawn together and down, mouth turned down, eyes lowered slightly. | М |
| 43 | CastSpell | Каст заклинания | Concentrating on a spell: eyes closed, brows slightly knitted, lips closed and calm. | М |
| 44 | Portrait41 | Взрыв ловушки, урон всей партии, взорвалось зелье, предмет сломан/украден, угроза не удалась | Shocked pain: eyes wide, brows raised, mouth open in "ah!". | М |
| 45 | Portrait42 | Те же события (второй вариант) | Wincing "ooh": lips pushed forward, brows raised, eyes half-closed. | М |
| 46 | Portrait43 | Не удалось опознать предмет/монстра | Puzzled: one eyebrow raised, the other lowered, lips pressed to one side. | М |
| 47 | Portrait44 | Просьба (Beg), в тюрьме | Pleading: eyes closed, brows raised in the middle, sad soft mouth. | М |
| 48 | Portrait45 | Убийство слабого врага, рост навыка, угроза, покупка/продажа, чаевые | Smug: confident closed-mouth smirk, eyelids slightly lowered. | М |
| 49 | Scared | Старение, почти мертва, крик | Alarmed shout: brows drawn down and together, eyes wide, mouth wide open yelling. (В вашем референсе здесь высунутый язык; движок использует кадр для испуга и крика.) | М |
| 50 | Portrait47 | Уровень, большое убийство, обезвреживание, удачное опознание, новый навык, зелье, рост характеристики | Proud triumph: big bright open smile, eyes shining, chin slightly up. | М |
| 51 | Portrait48 | Промах, провал, усталость, голод, последний живой, грубый/не тот магазин, отказ NPC | Annoyed disappointment: scowl, brows knitted, mouth tight. | М |
| 52 | Portrait49 | Чтение свитка, промах, опознание в лавке, вклад в банк | Skeptical: sideways glance toward the right side of the image, one eyebrow raised. | М |
| 53 | Portrait50 | Промах атаки | Angry glare: brows low, eyes narrowed, lips tight. | М |
| 54 | Portrait51 | «Не поддаётся» (дверь/предмет) | Straining with effort: face flushed red, teeth clenched and bared, eyes squeezed nearly shut. | Ц+М |
| 55 | Portrait52 | Напилась в таверне | Cheerfully drunk: laughing open smile, head tilted about 8°, eyes happy and unfocused, cheeks pink. | М |
| 56 | Portrait53 | Ночное приветствие, большое убийство | Surprised awe: eyes wide, brows high, mouth open round "oh!". | М |

## 5. Порядок генерации (почему «плывёт» и как этого избежать)

Причины дрейфа: (1) генератор пересоздаёт всё изображение при каждой правке; (2) несколько лиц на одном листе
влияют друг на друга; (3) длинный диалог накапливает изменения. Правила:

1. **Один кадр — один запрос.** Не генерировать лист из 56 (или 8) лиц и не править «одно лицо на листе».
2. **Новый чат для каждой группы**, а лучше для каждого кадра. Всегда прикладывать **один и тот же мастер (кадр 01)**.
3. **Кадры «М» и «Ц» — только правкой по маске** (в ChatGPT: открыть изображение → «Выделить/Select» → закрасить
   только глаза+брови+рот, для «Ц» — всю голову по контуру). Невыделенные пиксели не меняются, значит размер и
   положение головы сохраняются точно. Это главный способ остановить «плавание».
4. **Кадры «П»** (поворот, наклон, уклон, удар) — полная генерация с мастером во вложении, затем выравнивание по
   шаблону `guide-944x1264.png` в редакторе (Photopea/GIMP/Photoshop): масштаб так, чтобы размер головы совпал
   с мастером; глаза — на красной линии, если поза это позволяет.
5. Сначала сделать **разворот персонажа** (front, 3/4 left, 3/4 right, profile) отдельными изображениями — это
   «паспорт» для кадров «П».
6. Нумеровать файлы сразу (`01.png`…) и вести список «утверждено/переделать».

### 5.1 Запрос 1 — мастер (кадр 01)

Вложения: `guide-944x1264-on-grey.png` (только как схема кадрирования); референс-лист — только для понимания
формата (что это «голова без шеи в овале»), не для копирования лица.

```
Create ONE image: frame 01 (MASTER) of a 56-frame RPG party portrait set.
[CHARACTER LOCK]
[STYLE & FRAME LOCK]
Expression: calm neutral expression, relaxed closed lips, eyes looking straight at the viewer, alert and
confident. Snakes calm.
The attached grey guide shows only the framing proportions: follow the eye line, chin line and head oval,
but do NOT draw any lines. The attached sprite sheet shows the format only (a floating head cut out without
neck, front view); do not copy its face.
Do not: [NEGATIVE]
```

Сделать 4–8 вариантов, выбрать один, мелкие правки — только маской. Утвердить → это `01.png` и мастер для всех.

### 5.2 Запрос для кадров «М» / «Ц» (правка по маске)

Вложение: мастер `01.png`. Выделение: глаза, брови, рот (для «Ц» — вся голова по контуру).

```
Edit the selected area only. This is frame NN of the same character's portrait set.
KEEP EXACTLY: the identity, face shape, skin tint, scales, hair, the five snakes, lighting, head size, head
position, framing and transparent background. Change nothing outside the selection.
CHANGE ONLY: <текст из колонки «Что нарисовать» для кадра NN>
Do not: [NEGATIVE]
```

### 5.3 Запрос для кадров «П» (новая поза)

Вложения: мастер `01.png` (+ подходящий ракурс из разворота).

```
Create ONE image: frame NN of the same character's portrait set. The attached image is the master frame of
this exact character — same person, same identity.
[CHARACTER LOCK]
[STYLE & FRAME LOCK]
Pose change (the only difference from the master): <текст кадра NN>.
Keep the head the same size as in the master; the head may move only as described.
Do not: [NEGATIVE]
```

### 5.4 Другие системы

- **Stable Diffusion / ComfyUI** (лучшая согласованность): мастер → IP-Adapter FaceID/InstantID для лица;
  ControlNet (Depth/OpenPose-face) по позам; кадры «М» — inpaint по маске лица с denoise 0,35–0,55; фиксированный
  seed и тот же размер 944×1264.
- **Midjourney**: мастер как `--cref` (или omni-reference) с высоким весом, `--sref` на мастер для стиля,
  `--ar 59:79`; кадры «М» — Vary (Region) по лицу.

## 6. Приёмка кадра (чек-лист)

- [ ] 944×1264 (или больше, 59:79), PNG RGBA, фон прозрачный (или ровный `#808080` без тени).
- [ ] Наложение `guide-944x1264.png`: зрачки на красной линии ±10 px, нос на оси, подбородок на нижней оранжевой
      линии (кроме кадров «П»); силуэт внутри белого овала.
- [ ] Та же героиня: форма лица, янтарные глаза с круглыми зрачками, оттенок кожи, чешуя на висках.
- [ ] Ровно пять змей на тех же местах; не закрывают лицо; не выходят за кадр.
- [ ] Нет шеи, плеч, одежды, украшений, текста, рамки, линий шаблона.
- [ ] Нет чистых `#FF00FF` и `#00FFFF`.
- [ ] Читается в уменьшенном виде 118×158: выражение понятно издалека.
- [ ] Кадры последовательностей (25–29, 30–33, 34–36) — плавный ряд без скачков размера.

## 7. После генерации

```sh
python3 tools/import_portraits.py путь/к/папке --dry-run   # проверка набора и пропорций
python3 tools/import_portraits.py путь/к/папке             # 118x158 RGBA в пакет Medusa
```

Затем коммит и сборка Windows CI (`docs/build-and-install.md`). C++ не пересобирается по смыслу изменений — меняется
только пак `engine.rulesets`.
