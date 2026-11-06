# Героиня-полумедуза

Статус: концепция, изображений ещё нет.

## Образ

- Молодая взрослая женщина, анатомия человеческая: две руки, две ноги.
- Выразительное, привлекательное, преимущественно человеческое лицо.
- Кожа слегка зеленоватая; небольшие участки чешуи у висков, на скулах и шее.
- Волосы: живые змеи, частично вплетённые в обычную причёску. Число и расположение крупных змей фиксируются
  эталоном (например, 5 крупных: по две у висков и одна над лбом) и одинаковы во всех кадрах.
- Глаза: человеческие, с золотисто-янтарной радужкой, без «взгляда-окаменения» (способности отложены).
- Стиль: живописная фэнтези-иллюстрация в духе портретов Might and Magic VI–VIII (тёплый боковой свет, тёмный
  нейтральный фон, погрудный ракурс, лицо почти анфас).
- Не превращать в рептилоида: без змеиного хвоста, без морды, без раздвоенного языка в обычных кадрах.

## Игровые данные v1

| Поле | Значение | Почему |
|---|---|---|
| Строка `character_data.txt` | новая, через append ruleset Medusa (id 79 или первый свободный) | Не трогать таблицу движка |
| Префикс лица | `med01-` | 56 кадров |
| Тип куклы | 1 (человек-женщина) | Броня, анкеры, экипировка уже есть |
| Тело и руки | ресурсы существующей героини (`pc02*`, уточнить по виду) | Без новой брони |
| Голова на кукле | временно чужая; позже одна картинка Medusa | Голова — отдельный ресурс |
| Раса | 0 (Human) | Расовые механики отложены |
| Голос | существующий женский | — |
| Класс по умолчанию | уточнить (например Druid или Sorcerer) | — |

## Промпт для эталона (внешний генератор)

> Bust portrait of a young adult half-medusa woman, mostly human face, attractive and expressive, faint green tint to
> the skin, small patches of fine scales at the temples, cheekbones and neck, hair partly braided with five living
> slender snakes (two at each temple, one above the forehead), amber eyes, calm neutral expression, facing the viewer
> almost frontally, warm soft key light from the left, dark neutral background, painterly classic fantasy RPG portrait
> style of late-1990s computer role-playing games, head and shoulders, centered, no text, no frame.

Отрицательный промпт: full snake body, reptile face, monster, extra limbs, horror, gore, text, watermark, frame,
photorealistic.

Технические требования к эталону: ≥ 944×1264, соотношение 59:79, голова занимает около 60 % высоты, глаза примерно
на 40 % от верха. Кадры B и C делаются от этого изображения (img2img или inpaint), а не с нуля.
