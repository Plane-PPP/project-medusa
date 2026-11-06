# 56 промптов для ChatGPT: кадры портрета героини

Сгенерировано `tools/make_portrait_prompts.py` по [ТЗ](portrait-generation-brief.md). Не править вручную:
менять данные в скрипте и запускать его заново.

## Как пользоваться

1. **Каждый кадр — новый чат.** Вставлять один промпт целиком, ничего не добавляя к нему.
2. **Кадр 01 (мастер)** — первым. Вложение: `portraits/templates/guide-944x1264-on-grey.png`. Сделать
   4–8 вариантов, выбрать один, мелкие правки — только выделением. Сохранить как `01.png`.
3. **Метод «правка мастера по выделению»** (37 кадров, из них 4 — выделение всей головы): загрузить `01.png`, открыть его, нажать «Выделить»
   (Select), закрасить **только указанную область**, вставить промпт. Всё невыделенное не меняется,
   поэтому размер и положение головы остаются точными.
4. **Метод «новая генерация с мастером»** (18 кадров с другой позой): приложить `01.png`, вставить промпт.
   Потом в редакторе (Photopea, GIMP) наложить `portraits/templates/guide-944x1264.png` и подогнать
   масштаб, чтобы голова была того же размера, что у мастера.
5. Сохранять как `NN.png` (944×1264, прозрачный фон или ровный серый `#808080`). Сверять по чек-листу ТЗ.
6. Если результат «поплыл», не уточнять в том же чате: начать новый чат с тем же промптом.

Направления «LEFT/RIGHT side of the image» — как видит зритель.

| № | Состояние | Метод |
|---|---|---|
| [01](#кадр-01) | Normal — обычное лицо; первый кадр уклонения | новая генерация (это мастер) |
| [02](#кадр-02) | Cursed — проклятие | правка мастера по выделению |
| [03](#кадр-03) | Weak — слабость (в т. ч. от недосыпа) | правка мастера по выделению |
| [04](#кадр-04) | Sleep — сон | новая генерация с мастером во вложении + выравнивание по шаблону |
| [05](#кадр-05) | Fear — страх; первый кадр пробуждения (05→19→18) | правка мастера по выделению |
| [06](#кадр-06) | Drunk — опьянение | правка мастера по выделению |
| [07](#кадр-07) | Insane — безумие | правка мастера по выделению |
| [08](#кадр-08) | Poisoned — отравление (все степени) | правка мастера по выделению всей головы |
| [09](#кадр-09) | Diseased — болезнь (все степени); показывается и при болезни с отравлением | правка мастера по выделению всей головы |
| [10](#кадр-10) | Paralyzed — паралич | правка мастера по выделению |
| [11](#кадр-11) | Unconscious — без сознания; также при HP ≤ 0 | новая генерация с мастером во вложении + выравнивание по шаблону |
| [12](#кадр-12) | Petrified — окаменение | правка мастера по выделению всей головы |
| [13](#кадр-13) | Blink — моргание (очень короткий кадр) | правка мастера по выделению |
| [14](#кадр-14) | Wink — случайный холостой кадр | правка мастера по выделению |
| [15](#кадр-15) | MouthOpenRandom — случайный холостой кадр | правка мастера по выделению |
| [16](#кадр-16) | PurseLipsRandom — случайный холостой кадр | правка мастера по выделению |
| [17](#кадр-17) | LookUp — взгляд вверх | правка мастера по выделению |
| [18](#кадр-18) | LookRight — взгляд в сторону; третий кадр пробуждения | правка мастера по выделению |
| [19](#кадр-19) | LookLeft — взгляд в сторону; второй кадр пробуждения | новая генерация с мастером во вложении + выравнивание по шаблону |
| [20](#кадр-20) | LookDown — взгляд вниз | правка мастера по выделению |
| [21](#кадр-21) | Talk (PurseLips1-3, Portrait54) — речь; вход/выход из подземелья, пожертвование в храме | правка мастера по выделению |
| [22](#кадр-22) | MouthOpenWide (Portrait55) — речь | правка мастера по выделению |
| [23](#кадр-23) | MouthOpenA (Portrait56) — речь | правка мастера по выделению |
| [24](#кадр-24) | MouthOpenO (Portrait57) — речь | правка мастера по выделению |
| [25](#кадр-25) | No (крайний поворот) — покачивание «нет»: 27,26,25,26,27,28,29,28,27 | новая генерация с мастером во вложении + выравнивание по шаблону |
| [26](#кадр-26) | No (средний поворот) — покачивание «нет» | новая генерация с мастером во вложении + выравнивание по шаблону |
| [27](#кадр-27) | No (центр) — покачивание «нет» | правка мастера по выделению |
| [28](#кадр-28) | No (средний поворот) — покачивание «нет» | новая генерация с мастером во вложении + выравнивание по шаблону |
| [29](#кадр-29) | No (крайний поворот) — покачивание «нет» | новая генерация с мастером во вложении + выравнивание по шаблону |
| [30](#кадр-30) | Yes (вверх) — кивок «да»: 32,33,32,31,30,31 | новая генерация с мастером во вложении + выравнивание по шаблону |
| [31](#кадр-31) | Yes (чуть вверх) — кивок «да» | новая генерация с мастером во вложении + выравнивание по шаблону |
| [32](#кадр-32) | Yes (чуть вниз) — кивок «да» | новая генерация с мастером во вложении + выравнивание по шаблону |
| [33](#кадр-33) | Yes (вниз) — кивок «да» | новая генерация с мастером во вложении + выравнивание по шаблону |
| [34](#кадр-34) | AvoidDamage (1) — уклонение: 01,34,35,36,35,34 | новая генерация с мастером во вложении + выравнивание по шаблону |
| [35](#кадр-35) | AvoidDamage (2) — уклонение | новая генерация с мастером во вложении + выравнивание по шаблону |
| [36](#кадр-36) | AvoidDamage (3) — уклонение (глубокий нырок) | новая генерация с мастером во вложении + выравнивание по шаблону |
| [37](#кадр-37) | DamageReceivedMinor — лёгкий урон | новая генерация с мастером во вложении + выравнивание по шаблону |
| [38](#кадр-38) | DamageReceivedModerate — средний урон | новая генерация с мастером во вложении + выравнивание по шаблону |
| [39](#кадр-39) | DamageReceivedMajor — сильный урон | новая генерация с мастером во вложении + выравнивание по шаблону |
| [40](#кадр-40) | Smile — приветствие, удачный удар, находка, торговля, рост навыка, найм, угроза | правка мастера по выделению |
| [41](#кадр-41) | WideSmile — то же + награда, квест, зелье, ремонт, лечение | правка мастера по выделению |
| [42](#кадр-42) | Sad — усталость, провал заклинания или ремонта, нет маны, грубый торговец | правка мастера по выделению |
| [43](#кадр-43) | CastSpell — каст заклинания | правка мастера по выделению |
| [44](#кадр-44) | Portrait41 — взрыв ловушки, урон партии, взорвалось зелье, предмет сломан/украден | правка мастера по выделению |
| [45](#кадр-45) | Portrait42 — те же события, второй вариант | правка мастера по выделению |
| [46](#кадр-46) | Portrait43 — не удалось опознать предмет или монстра | правка мастера по выделению |
| [47](#кадр-47) | Portrait44 — просьба (Beg), в тюрьме | правка мастера по выделению |
| [48](#кадр-48) | Portrait45 — убийство слабого врага, рост навыка, угроза, торговля | правка мастера по выделению |
| [49](#кадр-49) | Scared — старение, почти мертва, крик | правка мастера по выделению |
| [50](#кадр-50) | Portrait47 — новый уровень, большое убийство, обезвреживание, удачное опознание, новый навык | правка мастера по выделению |
| [51](#кадр-51) | Portrait48 — промах, провал, усталость, голод, последний живой, отказ NPC | правка мастера по выделению |
| [52](#кадр-52) | Portrait49 — чтение свитка, промах, опознание в лавке, вклад в банк | правка мастера по выделению |
| [53](#кадр-53) | Portrait50 — промах атаки | правка мастера по выделению |
| [54](#кадр-54) | Portrait51 — «не поддаётся» (дверь, предмет) | правка мастера по выделению всей головы |
| [55](#кадр-55) | Portrait52 — напилась в таверне | новая генерация с мастером во вложении + выравнивание по шаблону |
| [56](#кадр-56) | Portrait53 — ночное приветствие, большое убийство | правка мастера по выделению |

## Кадр 01

- **Движок:** Normal. **Показывается:** обычное лицо; первый кадр уклонения.
- **Метод:** новая генерация (это мастер).
- **Вложения:** `guide-944x1264-on-grey.png` (можно также лист-референс формата).
- **Проверить:** мастер для всех остальных кадров; утверждать особенно тщательно.

```text
Create ONE image: frame 01 (the MASTER) of a 56-frame RPG party portrait set. Every later frame will be made from this image, so follow every requirement exactly.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

EXPRESSION: Calm neutral expression, relaxed closed lips, eyes looking straight at the viewer, alert and confident. Snakes calm and relaxed.

The attached grey guide image shows ONLY the framing proportions: put the pupils on its red line, the nose on its dashed centre line, the chin on its lowest orange line and the head inside its white oval - but do NOT draw any of its lines. If a sprite sheet of other faces is attached, it only shows the format (a floating head without neck, front view) - do not copy its face or hair.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 02

- **Движок:** Cursed. **Показывается:** проклятие.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** веки опущены наполовину, взгляд вниз.

```text
Edit ONLY the selected area of the attached image. This is frame 02 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Gloomy cursed look: heavy half-lowered eyelids, eyes looking down, a slight frown, faint grey shadows under the eyes, dull tired look.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 03

- **Движок:** Weak. **Показывается:** слабость (в т. ч. от недосыпа).
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** почти закрытые глаза, грустные брови.

```text
Edit ONLY the selected area of the attached image. This is frame 03 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Exhausted and weak: eyelids almost closed, sad drooping eyebrows, mouth slightly slack and open a little, a worn-out look.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 04

- **Движок:** Sleep. **Показывается:** сон.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** голова наклонена вправо по изображению ~20°, размер головы как у мастера.

```text
Create ONE image: frame 04 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Asleep: eyes fully closed, face completely relaxed, lips slightly parted; the head tilted (rolled) about 20 degrees toward the RIGHT side of the image and lowered a little. The snakes are asleep, resting on the hair.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 05

- **Движок:** Fear. **Показывается:** страх; первый кадр пробуждения (05→19→18).
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот, змеи.
- **Проверить:** широко открытые глаза, открытый рот.

```text
Edit ONLY the selected area of the attached image. This is frame 05 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Terrified: eyes wide open showing white around the irises, eyebrows raised high, mouth open in a gasp. The snakes are reared up and tense but stay inside the head silhouette.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 06

- **Движок:** Drunk. **Показывается:** опьянение.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот, щёки.
- **Проверить:** кривая полуулыбка, румянец.

```text
Edit ONLY the selected area of the attached image. This is frame 06 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Tipsy: a lopsided silly half-smile, unfocused half-closed eyes, cheeks slightly flushed pink.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 07

- **Движок:** Insane. **Показывается:** безумие.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** безумная широкая улыбка.

```text
Edit ONLY the selected area of the attached image. This is frame 07 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Manic insanity: a wide toothy grin, wild staring eyes, eyebrows raised unevenly.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 08

- **Движок:** Poisoned. **Показывается:** отравление (все степени).
- **Метод:** правка мастера по выделению всей головы.
- **Вложения:** `01.png` (мастер). **Выделить:** вся голова по контуру.
- **Проверить:** кожа заметно жёлто-зелёная, отличима от обычного оттенка.

```text
Edit ONLY the selected area of the attached image. This is frame 08 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape and features, the shape of the temple scales, the hairstyle shape, all five snakes with their count and placement, lighting direction, head size, head position, silhouette, framing, canvas size 944x1264 and the transparent background. Colours and surface change ONLY as described below. Change nothing outside the selected area.

CHANGE ONLY: Poisoned: sickly yellow-green skin, clearly yellower and darker than her normal faint sage tint, a sweaty sheen, nauseous half-closed eyes, mouth slightly open. Hair and snakes keep their colours.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 09

- **Движок:** Diseased. **Показывается:** болезнь (все степени); показывается и при болезни с отравлением.
- **Метод:** правка мастера по выделению всей головы.
- **Вложения:** `01.png` (мастер). **Выделить:** вся голова по контуру.
- **Проверить:** красные пятна и гнойнички хорошо видны в 118×158.

```text
Edit ONLY the selected area of the attached image. This is frame 09 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape and features, the shape of the temple scales, the hairstyle shape, all five snakes with their count and placement, lighting direction, head size, head position, silhouette, framing, canvas size 944x1264 and the transparent background. Colours and surface change ONLY as described below. Change nothing outside the selected area.

CHANGE ONLY: Diseased: red inflamed blotches and small pustules on the forehead and cheeks, slightly puffy skin, one eye squinting, a miserable expression.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 10

- **Движок:** Paralyzed. **Показывается:** паралич.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот, щёки.
- **Проверить:** застывший пустой взгляд.

```text
Edit ONLY the selected area of the attached image. This is frame 10 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Paralyzed: a frozen blank stare, eyes wide open and fixed straight ahead, the face completely slack, a faint bluish-grey pallor.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 11

- **Движок:** Unconscious. **Показывается:** без сознания; также при HP ≤ 0.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** голова завалилась вправо ~25°, синяк у глаза.

```text
Create ONE image: frame 11 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Unconscious: eyes closed, mouth slack, a dark bruise around her left eye (right side of the image); the head lolled about 25 degrees toward the RIGHT side of the image and slightly down. The snakes hang limp.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 12

- **Движок:** Petrified. **Показывается:** окаменение.
- **Метод:** правка мастера по выделению всей головы.
- **Вложения:** `01.png` (мастер). **Выделить:** вся голова по контуру.
- **Проверить:** полностью серый камень, силуэт как у мастера.

```text
Edit ONLY the selected area of the attached image. This is frame 12 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape and features, the shape of the temple scales, the hairstyle shape, all five snakes with their count and placement, lighting direction, head size, head position, silhouette, framing, canvas size 944x1264 and the transparent background. Colours and surface change ONLY as described below. Change nothing outside the selected area.

CHANGE ONLY: Petrified: the whole head - skin, hair and all five snakes - turned into matte grey granite stone with a fine stone grain, no colour at all, eyes closed, a serene face. The silhouette stays exactly the same.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 13

- **Движок:** Blink. **Показывается:** моргание (очень короткий кадр).
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** только глаза.
- **Проверить:** должен совпадать с 01 всем, кроме век.

```text
Edit ONLY the selected area of the attached image. This is frame 13 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Both eyes closed naturally, as in the middle of a blink. Nothing else changes.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 14

- **Движок:** Wink. **Показывается:** случайный холостой кадр.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, рот.
- **Проверить:** закрыт глаз слева по изображению.

```text
Edit ONLY the selected area of the attached image. This is frame 14 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: A wink: her right eye (on the LEFT side of the image) closed, the other eye open, a faint playful smile at one corner of the mouth.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 15

- **Движок:** MouthOpenRandom. **Показывается:** случайный холостой кадр.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** рот.
- **Проверить:** почти как 01, губы чуть разомкнуты.

```text
Edit ONLY the selected area of the attached image. This is frame 15 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: The master expression with the lips slightly parted.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 16

- **Движок:** PurseLipsRandom. **Показывается:** случайный холостой кадр.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** рот.
- **Проверить:** губы сжаты.

```text
Edit ONLY the selected area of the attached image. This is frame 16 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: The master expression with the lips pressed together and slightly pursed.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 17

- **Движок:** LookUp. **Показывается:** взгляд вверх.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови.
- **Проверить:** зрачки вверху глаз.

```text
Edit ONLY the selected area of the attached image. This is frame 17 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Eyes looking up toward the top of the image, eyebrows slightly raised.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 18

- **Движок:** LookRight. **Показывается:** взгляд в сторону; третий кадр пробуждения.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови.
- **Проверить:** зрачки смещены влево по изображению.

```text
Edit ONLY the selected area of the attached image. This is frame 18 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Eyes turned toward the LEFT side of the image (her right), the head unchanged.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 19

- **Движок:** LookLeft. **Показывается:** взгляд в сторону; второй кадр пробуждения.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** поворот вправо ~25°, размер головы как у мастера.

```text
Create ONE image: frame 19 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: The head turned (yaw) about 25 degrees toward the RIGHT side of the image, eyes looking the same way.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 20

- **Движок:** LookDown. **Показывается:** взгляд вниз.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови.
- **Проверить:** взгляд вниз.

```text
Edit ONLY the selected area of the attached image. This is frame 20 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Eyes looking down, eyelids lowered, the head unchanged.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 21

- **Движок:** Talk (PurseLips1-3, Portrait54). **Показывается:** речь; вход/выход из подземелья, пожертвование в храме.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** рот.
- **Проверить:** рот чуть приоткрыт.

```text
Edit ONLY the selected area of the attached image. This is frame 21 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Speaking: mouth slightly open as when saying "eh", relaxed face.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 22

- **Движок:** MouthOpenWide (Portrait55). **Показывается:** речь.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** рот.
- **Проверить:** рот открыт «а».

```text
Edit ONLY the selected area of the attached image. This is frame 22 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Speaking: mouth open as when saying "ah".

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 23

- **Движок:** MouthOpenA (Portrait56). **Показывается:** речь.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** рот.
- **Проверить:** видны верхние зубы.

```text
Edit ONLY the selected area of the attached image. This is frame 23 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Speaking with a slight smile: mouth open as when saying "ee", upper teeth visible.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 24

- **Движок:** MouthOpenO (Portrait57). **Показывается:** речь.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** рот.
- **Проверить:** губы трубочкой.

```text
Edit ONLY the selected area of the attached image. This is frame 24 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Speaking: lips rounded as when saying "oo".

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 25

- **Движок:** No (крайний поворот). **Показывается:** покачивание «нет»: 27,26,25,26,27,28,29,28,27.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** поворот влево ~25°; размер головы как у мастера.

```text
Create ONE image: frame 25 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Shaking the head "no": the head turned (yaw) about 25 degrees toward the LEFT side of the image, mild disapproval, mouth closed.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 26

- **Движок:** No (средний поворот). **Показывается:** покачивание «нет».
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** поворот влево ~12°.

```text
Create ONE image: frame 26 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Shaking the head "no": the head turned about 12 degrees toward the LEFT side of the image, mild disapproval, mouth closed.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 27

- **Движок:** No (центр). **Показывается:** покачивание «нет».
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** рот, брови.
- **Проверить:** поза как у мастера.

```text
Edit ONLY the selected area of the attached image. This is frame 27 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Head straight as in the master, a slight disapproving press of the lips, mild disapproval.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 28

- **Движок:** No (средний поворот). **Показывается:** покачивание «нет».
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** поворот вправо ~12°.

```text
Create ONE image: frame 28 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Shaking the head "no": the head turned about 12 degrees toward the RIGHT side of the image, mild disapproval, mouth closed.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 29

- **Движок:** No (крайний поворот). **Показывается:** покачивание «нет».
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** поворот вправо ~25°.

```text
Create ONE image: frame 29 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Shaking the head "no": the head turned about 25 degrees toward the RIGHT side of the image, mild disapproval, mouth closed.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 30

- **Движок:** Yes (вверх). **Показывается:** кивок «да»: 32,33,32,31,30,31.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** подбородок поднят ~10°.

```text
Create ONE image: frame 30 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Nodding "yes": chin raised about 10 degrees (head tilted back), a pleasant agreeable look, mouth closed.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 31

- **Движок:** Yes (чуть вверх). **Показывается:** кивок «да».
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** почти как мастер.

```text
Create ONE image: frame 31 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Nodding "yes": chin raised about 4 degrees, a pleasant agreeable look, mouth closed.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 32

- **Движок:** Yes (чуть вниз). **Показывается:** кивок «да».
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** подбородок опущен ~6°.

```text
Create ONE image: frame 32 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Nodding "yes": chin lowered about 6 degrees, a pleasant agreeable look, mouth closed.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 33

- **Движок:** Yes (вниз). **Показывается:** кивок «да».
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** подбородок опущен ~15°.

```text
Create ONE image: frame 33 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Nodding "yes": chin lowered about 15 degrees, eyes still on the viewer from under the brows, mouth closed.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 34

- **Движок:** AvoidDamage (1). **Показывается:** уклонение: 01,34,35,36,35,34.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** рывок вправо ~20°.

```text
Create ONE image: frame 34 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Dodging a blow: the head jerked about 20 degrees toward the RIGHT side of the image and slightly down, eyes squinting.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 35

- **Движок:** AvoidDamage (2). **Показывается:** уклонение.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** голова ниже на ~15% и повёрнута.

```text
Create ONE image: frame 35 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Ducking a blow: the head dropped about 15% of the image height lower than in the master and turned about 30 degrees toward the RIGHT side of the image, eyes shut. The top of the head stays inside the image.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 36

- **Движок:** AvoidDamage (3). **Показывается:** уклонение (глубокий нырок).
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** видна только макушка внизу слева.

```text
Create ONE image: frame 36 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: A deep duck: the head has dropped almost out of the image - only the top of the head (hair and snakes, seen from above) is visible in the lower-left part of the image; the face is below the bottom edge. The rest of the image is empty transparent background.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 37

- **Движок:** DamageReceivedMinor. **Показывается:** лёгкий урон.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** наклон вправо, зажмурилась.

```text
Create ONE image: frame 37 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Hit by a light blow: the head knocked about 15 degrees toward the RIGHT side of the image, eyes closed in a wince, a small bruise on one cheek.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 38

- **Движок:** DamageReceivedModerate. **Показывается:** средний урон.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** голова вниз-вправо, ссадина.

```text
Create ONE image: frame 38 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Hit hard: the head knocked down about 15 degrees and toward the RIGHT side of the image, eyes shut tight, a bruise and a small cut on the cheek.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 39

- **Движок:** DamageReceivedMajor. **Показывается:** сильный урон.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** голова запрокинута, гримаса боли.

```text
Create ONE image: frame 39 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: A severe hit: the head thrown back about 20 degrees and turned, teeth clenched in a pained grimace, bruising on the cheek and around one eye.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 40

- **Движок:** Smile. **Показывается:** приветствие, удачный удар, находка, торговля, рост навыка, найм, угроза.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, рот, щёки.
- **Проверить:** улыбка без зубов.

```text
Edit ONLY the selected area of the attached image. This is frame 40 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: A warm closed-mouth smile, friendly eyes.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 41

- **Движок:** WideSmile. **Показывается:** то же + награда, квест, зелье, ремонт, лечение.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, рот, щёки.
- **Проверить:** широкая улыбка с зубами.

```text
Edit ONLY the selected area of the attached image. This is frame 41 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: A wide happy open smile showing the upper teeth, eyes crinkled with joy.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 42

- **Движок:** Sad. **Показывается:** усталость, провал заклинания или ремонта, нет маны, грубый торговец.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** грустная, уголки рта вниз.

```text
Edit ONLY the selected area of the attached image. This is frame 42 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Displeased and sad: eyebrows drawn together and down, the corners of the mouth turned down, eyes lowered slightly.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 43

- **Движок:** CastSpell. **Показывается:** каст заклинания.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** сосредоточенность, глаза закрыты.

```text
Edit ONLY the selected area of the attached image. This is frame 43 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Concentrating on casting a spell: eyes closed, eyebrows slightly knitted, lips closed and calm.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 44

- **Движок:** Portrait41. **Показывается:** взрыв ловушки, урон партии, взорвалось зелье, предмет сломан/украден.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** шок, открытый рот.

```text
Edit ONLY the selected area of the attached image. This is frame 44 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Shocked pain: eyes wide, eyebrows raised, mouth open in a sharp "ah!".

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 45

- **Движок:** Portrait42. **Показывается:** те же события, второй вариант.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** губы вперёд «у-у».

```text
Edit ONLY the selected area of the attached image. This is frame 45 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Wincing "ooh": lips pushed forward, eyebrows raised, eyes half-closed.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 46

- **Движок:** Portrait43. **Показывается:** не удалось опознать предмет или монстра.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** недоумение, брови разные.

```text
Edit ONLY the selected area of the attached image. This is frame 46 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Puzzled: one eyebrow raised and the other lowered, lips pressed to one side.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 47

- **Движок:** Portrait44. **Показывается:** просьба (Beg), в тюрьме.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** мольба, глаза закрыты.

```text
Edit ONLY the selected area of the attached image. This is frame 47 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Pleading: eyes closed, eyebrows raised in the middle, a sad soft mouth.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 48

- **Движок:** Portrait45. **Показывается:** убийство слабого врага, рост навыка, угроза, торговля.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, рот.
- **Проверить:** самодовольная ухмылка.

```text
Edit ONLY the selected area of the attached image. This is frame 48 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Smug: a confident closed-mouth smirk, eyelids slightly lowered.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 49

- **Движок:** Scared. **Показывается:** старение, почти мертва, крик.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** кричит в тревоге (не язык, как в чужом референсе).

```text
Edit ONLY the selected area of the attached image. This is frame 49 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: An alarmed shout: eyebrows drawn down and together, eyes wide, mouth wide open yelling.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 50

- **Движок:** Portrait47. **Показывается:** новый уровень, большое убийство, обезвреживание, удачное опознание, новый навык.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** торжество, большая улыбка.

```text
Edit ONLY the selected area of the attached image. This is frame 50 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Proud triumph: a big bright open smile, shining eyes, chin raised slightly.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 51

- **Движок:** Portrait48. **Показывается:** промах, провал, усталость, голод, последний живой, отказ NPC.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** раздражение.

```text
Edit ONLY the selected area of the attached image. This is frame 51 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Annoyed disappointment: a scowl, eyebrows knitted, mouth tight.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 52

- **Движок:** Portrait49. **Показывается:** чтение свитка, промах, опознание в лавке, вклад в банк.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** скептический взгляд вбок.

```text
Edit ONLY the selected area of the attached image. This is frame 52 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Skeptical: a sideways glance toward the RIGHT side of the image, one eyebrow raised, lips closed.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 53

- **Движок:** Portrait50. **Показывается:** промах атаки.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** злой прищур.

```text
Edit ONLY the selected area of the attached image. This is frame 53 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: An angry glare: eyebrows low, eyes narrowed, lips tight.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 54

- **Движок:** Portrait51. **Показывается:** «не поддаётся» (дверь, предмет).
- **Метод:** правка мастера по выделению всей головы.
- **Вложения:** `01.png` (мастер). **Выделить:** лицо и уши (без волос и змей).
- **Проверить:** красное от натуги лицо, стиснутые зубы.

```text
Edit ONLY the selected area of the attached image. This is frame 54 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape and features, the shape of the temple scales, the hairstyle shape, all five snakes with their count and placement, lighting direction, head size, head position, silhouette, framing, canvas size 944x1264 and the transparent background. Colours and surface change ONLY as described below. Change nothing outside the selected area.

CHANGE ONLY: Straining with great effort: the face flushed red, teeth clenched and bared, eyes squeezed nearly shut.

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 55

- **Движок:** Portrait52. **Показывается:** напилась в таверне.
- **Метод:** новая генерация с мастером во вложении + выравнивание по шаблону.
- **Вложения:** `01.png` (мастер).
- **Проверить:** весёлая, голова слегка наклонена.

```text
Create ONE image: frame 55 of the same character's 56-frame portrait set. The attached image is the approved master (frame 01) of this exact character: the same person, the same identity, the same render style, the same lighting and the same head size.

CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. No jewellery, no clothing, no neck, no shoulders.

STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or leaves the left, right or top edge.

THE ONLY DIFFERENCE FROM THE MASTER: Cheerfully drunk: a laughing open smile, the head tilted about 8 degrees, happy unfocused eyes, pink cheeks.
The head keeps the master's size; it moves only as described, and no part of it is cut by the left, right or top edge unless described.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```

## Кадр 56

- **Движок:** Portrait53. **Показывается:** ночное приветствие, большое убийство.
- **Метод:** правка мастера по выделению.
- **Вложения:** `01.png` (мастер). **Выделить:** глаза, брови, рот.
- **Проверить:** удивление «о!».

```text
Edit ONLY the selected area of the attached image. This is frame 56 of the same character's 56-frame portrait set; the attached image is the approved master (frame 01).

KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area.

CHANGE ONLY: Surprised awe: eyes wide, eyebrows high, mouth open round in "oh!".

The result must still read clearly when shrunk to 118x158 pixels.

Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere.
```
