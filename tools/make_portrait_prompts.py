#!/usr/bin/env python3
"""Writes docs/design/portrait-prompts.md: 56 self-contained ChatGPT prompts for the heroine's portrait frames.

The frame list, locks and methods follow docs/design/portrait-generation-brief.md (sections 3-5); edit them here and
re-run, so the prompts and the brief stay in step. Every prompt is pasted alone into a NEW chat.

Methods:
  master  frame 01: full generation
  mask    edit of the master with only the eyes/brows/mouth selected (ChatGPT "Select" tool)
  colour  edit of the master with the whole head selected (skin/hair colour or texture changes)
  pose    full generation with the master attached, then alignment on the framing guide

    python3 tools/make_portrait_prompts.py
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "docs/design/portrait-prompts.md"

CHARACTER = (
    "CHARACTER (identical in every image): young adult half-medusa woman, about 25 years old, human anatomy. "
    "Attractive, expressive, mostly human face: oval face, defined high cheekbones, straight slim nose, full lips in "
    "muted rose-mauve, almond-shaped eyes with amber-gold irises and normal ROUND human pupils, dark well-shaped "
    "arched eyebrows. Skin: pale with a faint sage-green tint (about #B8C4A2), smooth, natural pores. Scales: small "
    "symmetric patches of fine emerald-green scales at both temples, continuing thinly along the outer cheekbones; "
    "no scales on the nose, lips or centre of the forehead. Hair: very dark green-black with deep bottle-green "
    "highlights, pulled back from the face, close to the head, ending at jaw level, no fringe, forehead free. "
    "Snakes: exactly FIVE slender living snakes grow from the hair as part of the hairstyle - two at the left "
    "temple, two at the right temple, one coiled on the crown; emerald green with a pale gold belly and a thin black "
    "stripe, small heads, closed mouths; they stay inside the head silhouette and never cover the eyes or the face. "
    "No jewellery, no clothing, no neck, no shoulders."
)

STYLE = (
    "STYLE AND FRAMING (identical in every image): late-1990s Might and Magic VII/VIII party portrait, remastered - "
    "semi-realistic 3D CG render, soft studio light from the upper left, natural skin shading, high detail, no "
    "painterly brush strokes, no outline. HEAD ONLY: cut out along the hair silhouette and just under the chin, no "
    "neck, no shoulders, a floating head on a fully TRANSPARENT background (if transparency is impossible: flat "
    "uniform #808080 grey, no shadow, no gradient). Portrait canvas 944x1264 pixels, ratio 59:79, vertical. Camera "
    "at eye level, straight on. Framing: top of the hair and snakes at 2.5% of the image height, pupils on a "
    "horizontal line at 49% of the height, nose tip at 63%, mouth at 74%, chin at 96%; nose on the vertical centre "
    "line; pupils at 35% and 66% of the width; the head silhouette spans 5-97% of the width; nothing touches or "
    "leaves the left, right or top edge."
)

NEGATIVE = (
    "Do NOT add: reptile face, slit pupils, snake eyes, fangs, forked tongue, monster features, a snake body or tail, "
    "extra snakes, snakes over the face, horns, extra eyes, neck, shoulders, clothing, jewellery, crown, any "
    "background scene, vignette, drop shadow, text, watermark, frame, border, guide lines, cartoon or anime style, "
    "painterly style. Do NOT change the hairstyle, the face, the head size or the head position unless asked. "
    "Do NOT use pure magenta #FF00FF or pure cyan #00FFFF anywhere."
)

KEEP_COLOUR = (
    "KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape and features, the shape of "
    "the temple scales, the hairstyle shape, all five snakes with their count and placement, lighting direction, "
    "head size, head position, silhouette, framing, canvas size 944x1264 and the transparent background. Colours "
    "and surface change ONLY as described below. Change nothing outside the selected area."
)

KEEP = (
    "KEEP EXACTLY AS IN THE ATTACHED MASTER: the same person and identity, face shape, eye colour and round pupils, "
    "skin tint, temple scales, hair, all five snakes and their placement, lighting, head size, head position, "
    "framing, canvas size 944x1264 and the transparent background. Change nothing outside the selected area."
)

# number, engine name, when shown (RU), method, selection (RU, for mask/colour), change (EN), acceptance hint (RU)
FRAMES = [
    (1, "Normal", "обычное лицо; первый кадр уклонения", "master", "",
     "Calm neutral expression, relaxed closed lips, eyes looking straight at the viewer, alert and confident. "
     "Snakes calm and relaxed.", "мастер для всех остальных кадров; утверждать особенно тщательно"),
    (2, "Cursed", "проклятие", "mask", "глаза, брови, рот",
     "Gloomy cursed look: heavy half-lowered eyelids, eyes looking down, a slight frown, faint grey shadows under the "
     "eyes, dull tired look.", "веки опущены наполовину, взгляд вниз"),
    (3, "Weak", "слабость (в т. ч. от недосыпа)", "mask", "глаза, брови, рот",
     "Exhausted and weak: eyelids almost closed, sad drooping eyebrows, mouth slightly slack and open a little, "
     "a worn-out look.", "почти закрытые глаза, грустные брови"),
    (4, "Sleep", "сон", "pose", "",
     "Asleep: eyes fully closed, face completely relaxed, lips slightly parted; the head tilted (rolled) about 20 "
     "degrees toward the RIGHT side of the image and lowered a little. The snakes are asleep, resting on the hair.",
     "голова наклонена вправо по изображению ~20°, размер головы как у мастера"),
    (5, "Fear", "страх; первый кадр пробуждения (05→19→18)", "mask", "глаза, брови, рот, змеи",
     "Terrified: eyes wide open showing white around the irises, eyebrows raised high, mouth open in a gasp. The "
     "snakes are reared up and tense but stay inside the head silhouette.", "широко открытые глаза, открытый рот"),
    (6, "Drunk", "опьянение", "mask", "глаза, брови, рот, щёки",
     "Tipsy: a lopsided silly half-smile, unfocused half-closed eyes, cheeks slightly flushed pink.",
     "кривая полуулыбка, румянец"),
    (7, "Insane", "безумие", "mask", "глаза, брови, рот",
     "Manic insanity: a wide toothy grin, wild staring eyes, eyebrows raised unevenly.", "безумная широкая улыбка"),
    (8, "Poisoned", "отравление (все степени)", "colour", "вся голова по контуру",
     "Poisoned: sickly yellow-green skin, clearly yellower and darker than her normal faint sage tint, a sweaty "
     "sheen, nauseous half-closed eyes, mouth slightly open. Hair and snakes keep their colours.",
     "кожа заметно жёлто-зелёная, отличима от обычного оттенка"),
    (9, "Diseased", "болезнь (все степени); показывается и при болезни с отравлением", "colour",
     "вся голова по контуру",
     "Diseased: red inflamed blotches and small pustules on the forehead and cheeks, slightly puffy skin, one eye "
     "squinting, a miserable expression.", "красные пятна и гнойнички хорошо видны в 118×158"),
    (10, "Paralyzed", "паралич", "mask", "глаза, брови, рот, щёки",
     "Paralyzed: a frozen blank stare, eyes wide open and fixed straight ahead, the face completely slack, a faint "
     "bluish-grey pallor.", "застывший пустой взгляд"),
    (11, "Unconscious", "без сознания; также при HP ≤ 0", "pose", "",
     "Unconscious: eyes closed, mouth slack, a dark bruise around her left eye (right side of the image); the head "
     "lolled about 25 degrees toward the RIGHT side of the image and slightly down. The snakes hang limp.",
     "голова завалилась вправо ~25°, синяк у глаза"),
    (12, "Petrified", "окаменение", "colour", "вся голова по контуру",
     "Petrified: the whole head - skin, hair and all five snakes - turned into matte grey granite stone with a fine "
     "stone grain, no colour at all, eyes closed, a serene face. The silhouette stays exactly the same.",
     "полностью серый камень, силуэт как у мастера"),
    (13, "Blink", "моргание (очень короткий кадр)", "mask", "только глаза",
     "Both eyes closed naturally, as in the middle of a blink. Nothing else changes.",
     "должен совпадать с 01 всем, кроме век"),
    (14, "Wink", "случайный холостой кадр", "mask", "глаза, рот",
     "A wink: her right eye (on the LEFT side of the image) closed, the other eye open, a faint playful smile at "
     "one corner of the mouth.", "закрыт глаз слева по изображению"),
    (15, "MouthOpenRandom", "случайный холостой кадр", "mask", "рот",
     "The master expression with the lips slightly parted.", "почти как 01, губы чуть разомкнуты"),
    (16, "PurseLipsRandom", "случайный холостой кадр", "mask", "рот",
     "The master expression with the lips pressed together and slightly pursed.", "губы сжаты"),
    (17, "LookUp", "взгляд вверх", "mask", "глаза, брови",
     "Eyes looking up toward the top of the image, eyebrows slightly raised.", "зрачки вверху глаз"),
    (18, "LookRight", "взгляд в сторону; третий кадр пробуждения", "mask", "глаза, брови",
     "Eyes turned toward the LEFT side of the image (her right), the head unchanged.", "зрачки смещены влево по изображению"),
    (19, "LookLeft", "взгляд в сторону; второй кадр пробуждения", "pose", "",
     "The head turned (yaw) about 25 degrees toward the RIGHT side of the image, eyes looking the same way.",
     "поворот вправо ~25°, размер головы как у мастера"),
    (20, "LookDown", "взгляд вниз", "mask", "глаза, брови",
     "Eyes looking down, eyelids lowered, the head unchanged.", "взгляд вниз"),
    (21, "Talk (PurseLips1-3, Portrait54)", "речь; вход/выход из подземелья, пожертвование в храме", "mask", "рот",
     "Speaking: mouth slightly open as when saying \"eh\", relaxed face.", "рот чуть приоткрыт"),
    (22, "MouthOpenWide (Portrait55)", "речь", "mask", "рот",
     "Speaking: mouth open as when saying \"ah\".", "рот открыт «а»"),
    (23, "MouthOpenA (Portrait56)", "речь", "mask", "рот",
     "Speaking with a slight smile: mouth open as when saying \"ee\", upper teeth visible.", "видны верхние зубы"),
    (24, "MouthOpenO (Portrait57)", "речь", "mask", "рот",
     "Speaking: lips rounded as when saying \"oo\".", "губы трубочкой"),
    (25, "No (крайний поворот)", "покачивание «нет»: 27,26,25,26,27,28,29,28,27", "pose", "",
     "Shaking the head \"no\": the head turned (yaw) about 25 degrees toward the LEFT side of the image, mild "
     "disapproval, mouth closed.", "поворот влево ~25°; размер головы как у мастера"),
    (26, "No (средний поворот)", "покачивание «нет»", "pose", "",
     "Shaking the head \"no\": the head turned about 12 degrees toward the LEFT side of the image, mild "
     "disapproval, mouth closed.", "поворот влево ~12°"),
    (27, "No (центр)", "покачивание «нет»", "mask", "рот, брови",
     "Head straight as in the master, a slight disapproving press of the lips, mild disapproval.",
     "поза как у мастера"),
    (28, "No (средний поворот)", "покачивание «нет»", "pose", "",
     "Shaking the head \"no\": the head turned about 12 degrees toward the RIGHT side of the image, mild "
     "disapproval, mouth closed.", "поворот вправо ~12°"),
    (29, "No (крайний поворот)", "покачивание «нет»", "pose", "",
     "Shaking the head \"no\": the head turned about 25 degrees toward the RIGHT side of the image, mild "
     "disapproval, mouth closed.", "поворот вправо ~25°"),
    (30, "Yes (вверх)", "кивок «да»: 32,33,32,31,30,31", "pose", "",
     "Nodding \"yes\": chin raised about 10 degrees (head tilted back), a pleasant agreeable look, mouth closed.",
     "подбородок поднят ~10°"),
    (31, "Yes (чуть вверх)", "кивок «да»", "pose", "",
     "Nodding \"yes\": chin raised about 4 degrees, a pleasant agreeable look, mouth closed.", "почти как мастер"),
    (32, "Yes (чуть вниз)", "кивок «да»", "pose", "",
     "Nodding \"yes\": chin lowered about 6 degrees, a pleasant agreeable look, mouth closed.", "подбородок опущен ~6°"),
    (33, "Yes (вниз)", "кивок «да»", "pose", "",
     "Nodding \"yes\": chin lowered about 15 degrees, eyes still on the viewer from under the brows, mouth closed.",
     "подбородок опущен ~15°"),
    (34, "AvoidDamage (1)", "уклонение: 01,34,35,36,35,34", "pose", "",
     "Dodging a blow: the head jerked about 20 degrees toward the RIGHT side of the image and slightly down, eyes "
     "squinting.", "рывок вправо ~20°"),
    (35, "AvoidDamage (2)", "уклонение", "pose", "",
     "Ducking a blow: the head dropped about 15% of the image height lower than in the master and turned about 30 "
     "degrees toward the RIGHT side of the image, eyes shut. The top of the head stays inside the image.",
     "голова ниже на ~15% и повёрнута"),
    (36, "AvoidDamage (3)", "уклонение (глубокий нырок)", "pose", "",
     "A deep duck: the head has dropped almost out of the image - only the top of the head (hair and snakes, seen "
     "from above) is visible in the lower-left part of the image; the face is below the bottom edge. The rest of "
     "the image is empty transparent background.", "видна только макушка внизу слева"),
    (37, "DamageReceivedMinor", "лёгкий урон", "pose", "",
     "Hit by a light blow: the head knocked about 15 degrees toward the RIGHT side of the image, eyes closed in a "
     "wince, a small bruise on one cheek.", "наклон вправо, зажмурилась"),
    (38, "DamageReceivedModerate", "средний урон", "pose", "",
     "Hit hard: the head knocked down about 15 degrees and toward the RIGHT side of the image, eyes shut tight, a "
     "bruise and a small cut on the cheek.", "голова вниз-вправо, ссадина"),
    (39, "DamageReceivedMajor", "сильный урон", "pose", "",
     "A severe hit: the head thrown back about 20 degrees and turned, teeth clenched in a pained grimace, bruising "
     "on the cheek and around one eye.", "голова запрокинута, гримаса боли"),
    (40, "Smile", "приветствие, удачный удар, находка, торговля, рост навыка, найм, угроза", "mask",
     "глаза, рот, щёки", "A warm closed-mouth smile, friendly eyes.", "улыбка без зубов"),
    (41, "WideSmile", "то же + награда, квест, зелье, ремонт, лечение", "mask", "глаза, рот, щёки",
     "A wide happy open smile showing the upper teeth, eyes crinkled with joy.", "широкая улыбка с зубами"),
    (42, "Sad", "усталость, провал заклинания или ремонта, нет маны, грубый торговец", "mask", "глаза, брови, рот",
     "Displeased and sad: eyebrows drawn together and down, the corners of the mouth turned down, eyes lowered "
     "slightly.", "грустная, уголки рта вниз"),
    (43, "CastSpell", "каст заклинания", "mask", "глаза, брови, рот",
     "Concentrating on casting a spell: eyes closed, eyebrows slightly knitted, lips closed and calm.",
     "сосредоточенность, глаза закрыты"),
    (44, "Portrait41", "взрыв ловушки, урон партии, взорвалось зелье, предмет сломан/украден", "mask",
     "глаза, брови, рот", "Shocked pain: eyes wide, eyebrows raised, mouth open in a sharp \"ah!\".",
     "шок, открытый рот"),
    (45, "Portrait42", "те же события, второй вариант", "mask", "глаза, брови, рот",
     "Wincing \"ooh\": lips pushed forward, eyebrows raised, eyes half-closed.", "губы вперёд «у-у»"),
    (46, "Portrait43", "не удалось опознать предмет или монстра", "mask", "глаза, брови, рот",
     "Puzzled: one eyebrow raised and the other lowered, lips pressed to one side.", "недоумение, брови разные"),
    (47, "Portrait44", "просьба (Beg), в тюрьме", "mask", "глаза, брови, рот",
     "Pleading: eyes closed, eyebrows raised in the middle, a sad soft mouth.", "мольба, глаза закрыты"),
    (48, "Portrait45", "убийство слабого врага, рост навыка, угроза, торговля", "mask", "глаза, рот",
     "Smug: a confident closed-mouth smirk, eyelids slightly lowered.", "самодовольная ухмылка"),
    (49, "Scared", "старение, почти мертва, крик", "mask", "глаза, брови, рот",
     "An alarmed shout: eyebrows drawn down and together, eyes wide, mouth wide open yelling.",
     "кричит в тревоге (не язык, как в чужом референсе)"),
    (50, "Portrait47", "новый уровень, большое убийство, обезвреживание, удачное опознание, новый навык", "mask",
     "глаза, брови, рот", "Proud triumph: a big bright open smile, shining eyes, chin raised slightly.",
     "торжество, большая улыбка"),
    (51, "Portrait48", "промах, провал, усталость, голод, последний живой, отказ NPC", "mask", "глаза, брови, рот",
     "Annoyed disappointment: a scowl, eyebrows knitted, mouth tight.", "раздражение"),
    (52, "Portrait49", "чтение свитка, промах, опознание в лавке, вклад в банк", "mask", "глаза, брови, рот",
     "Skeptical: a sideways glance toward the RIGHT side of the image, one eyebrow raised, lips closed.",
     "скептический взгляд вбок"),
    (53, "Portrait50", "промах атаки", "mask", "глаза, брови, рот",
     "An angry glare: eyebrows low, eyes narrowed, lips tight.", "злой прищур"),
    (54, "Portrait51", "«не поддаётся» (дверь, предмет)", "colour", "лицо и уши (без волос и змей)",
     "Straining with great effort: the face flushed red, teeth clenched and bared, eyes squeezed nearly shut.",
     "красное от натуги лицо, стиснутые зубы"),
    (55, "Portrait52", "напилась в таверне", "pose", "",
     "Cheerfully drunk: a laughing open smile, the head tilted about 8 degrees, happy unfocused eyes, pink cheeks.",
     "весёлая, голова слегка наклонена"),
    (56, "Portrait53", "ночное приветствие, большое убийство", "mask", "глаза, брови, рот",
     "Surprised awe: eyes wide, eyebrows high, mouth open round in \"oh!\".", "удивление «о!»"),
]

METHOD_RU = {
    "master": "новая генерация (это мастер)",
    "mask": "правка мастера по выделению",
    "colour": "правка мастера по выделению всей головы",
    "pose": "новая генерация с мастером во вложении + выравнивание по шаблону",
}


def prompt(number, change, method):
    if method == "master":
        return (
            f"Create ONE image: frame {number:02d} (the MASTER) of a 56-frame RPG party portrait set. Every later "
            f"frame will be made from this image, so follow every requirement exactly.\n\n{CHARACTER}\n\n{STYLE}\n\n"
            f"EXPRESSION: {change}\n\nThe attached grey guide image shows ONLY the framing proportions: put the "
            f"pupils on its red line, the nose on its dashed centre line, the chin on its lowest orange line and the "
            f"head inside its white oval - but do NOT draw any of its lines. If a sprite sheet of other faces is "
            f"attached, it only shows the format (a floating head without neck, front view) - do not copy its face "
            f"or hair.\n\n{NEGATIVE}"
        )
    if method in ("mask", "colour"):
        return (
            f"Edit ONLY the selected area of the attached image. This is frame {number:02d} of the same character's "
            f"56-frame portrait set; the attached image is the approved master (frame 01).\n\n"
            f"{KEEP_COLOUR if method == 'colour' else KEEP}\n\n"
            f"CHANGE ONLY: {change}\n\nThe result must still read clearly when shrunk to 118x158 pixels.\n\n"
            f"{NEGATIVE}"
        )
    return (
        f"Create ONE image: frame {number:02d} of the same character's 56-frame portrait set. The attached image is "
        f"the approved master (frame 01) of this exact character: the same person, the same identity, the same "
        f"render style, the same lighting and the same head size.\n\n{CHARACTER}\n\n{STYLE}\n\n"
        f"THE ONLY DIFFERENCE FROM THE MASTER: {change}\nThe head keeps the master's size; it moves only as "
        f"described, and no part of it is cut by the left, right or top edge unless described.\n\n{NEGATIVE}"
    )


def main():
    lines = [
        "# 56 промптов для ChatGPT: кадры портрета героини",
        "",
        "Сгенерировано `tools/make_portrait_prompts.py` по [ТЗ](portrait-generation-brief.md). Не править вручную:",
        "менять данные в скрипте и запускать его заново.",
        "",
        "## Как пользоваться",
        "",
        "1. **Каждый кадр — новый чат.** Вставлять один промпт целиком, ничего не добавляя к нему.",
        "2. **Кадр 01 (мастер)** — первым. Вложение: `portraits/templates/guide-944x1264-on-grey.png`. Сделать",
        "   4–8 вариантов, выбрать один, мелкие правки — только выделением. Сохранить как `01.png`.",
        "3. **Метод «правка мастера по выделению»** (37 кадров, из них 4 — выделение всей головы): загрузить `01.png`, открыть его, нажать «Выделить»",
        "   (Select), закрасить **только указанную область**, вставить промпт. Всё невыделенное не меняется,",
        "   поэтому размер и положение головы остаются точными.",
        "4. **Метод «новая генерация с мастером»** (18 кадров с другой позой): приложить `01.png`, вставить промпт.",
        "   Потом в редакторе (Photopea, GIMP) наложить `portraits/templates/guide-944x1264.png` и подогнать",
        "   масштаб, чтобы голова была того же размера, что у мастера.",
        "5. Сохранять как `NN.png` (944×1264, прозрачный фон или ровный серый `#808080`). Сверять по чек-листу ТЗ.",
        "6. Если результат «поплыл», не уточнять в том же чате: начать новый чат с тем же промптом.",
        "",
        "Направления «LEFT/RIGHT side of the image» — как видит зритель.",
        "",
        "| № | Состояние | Метод |",
        "|---|---|---|",
    ]
    for number, engine, when, method, selection, change, check in FRAMES:
        lines.append(f"| [{number:02d}](#кадр-{number:02d}) | {engine} — {when} | {METHOD_RU[method]} |")
    lines.append("")
    for number, engine, when, method, selection, change, check in FRAMES:
        lines += [f"## Кадр {number:02d}", "",
                  f"- **Движок:** {engine}. **Показывается:** {when}.",
                  f"- **Метод:** {METHOD_RU[method]}."]
        if method == "master":
            lines.append("- **Вложения:** `guide-944x1264-on-grey.png` (можно также лист-референс формата).")
        elif method == "pose":
            lines.append("- **Вложения:** `01.png` (мастер).")
        else:
            lines.append(f"- **Вложения:** `01.png` (мастер). **Выделить:** {selection}.")
        lines += [f"- **Проверить:** {check}.", "", "```text", prompt(number, change, method), "```", ""]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    counts = {m: sum(1 for f in FRAMES if f[3] == m) for m in METHOD_RU}
    assert [f[0] for f in FRAMES] == list(range(1, 57))
    print(f"Wrote {len(FRAMES)} prompts to {OUT}: {counts}")


if __name__ == "__main__":
    main()
