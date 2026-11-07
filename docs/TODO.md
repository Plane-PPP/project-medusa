# TODO

Обновлено: 2026-11-06. Подробности: [интеграция](integration.md), [сборка и установка](build-and-install.md),
[решения](DECISIONS.md).

## Фазы A–B — организация и аудит (выполнены)

- [x] Worktree `openyamm-medusa`, ветка `feature/project-medusa` от `feature/minotaur-rebalance` @ `0c172ed`
- [x] Аудит движка ([аудит](research/medusa-engine-audit.md)); решения пользователя: ruleset-пакет, старт Mount Nighon
- [x] Документы Medusa живут только здесь (в `openyamm-medusa/docs` не копируются)

## Alpha 0.1 — первый играбельный старт

- [x] Публичный `Plane-PPP/project-medusa`, ветка `feature/project-medusa` в `Plane-PPP/openyamm`
- [x] `newGame.starts` в `ruleset.yml` + разбор + тесты; карточки в `NewGameScreen`; без «Rules…» без опций
- [x] Старт `out10.odm` у площадки Town Portal (3114, −11055, 513) через строку 2 `continent_settings`
- [x] Героиня: строка 79 `character_data`, кукла `pc02*`, Sorcerer, голос 1; 56 TEMP-кадров; иконки ruleset в движке
- [x] Тесты: разбор карточек, сломанный пакет, иконки ruleset, состав пакета и таблиц, сохранение героини
- [x] Windows CI `medusa-windows.yml`, патч `Project-Medusa-Alpha-0.1-Windows-Patch.zip`, prerelease `medusa-alpha-0.1`
- [ ] **Игровая проверка у пользователя** (чек-лист в `README-MEDUSA-RU.txt` патча): вкладки 16:9/4:3, карточка,
      создание партии, старт, движение, сохранение/загрузка, кукла и экипировка, Standard и MAW без изменений
- [ ] Длинное тире в «Project Medusa — Prologue» в шрифте меню (если не рисуется — заменить в `ruleset.yml`)
- [ ] Поведение стражи Нигона (Water Warlock, группа 55) к партии 1 уровня

## Alpha 0.2 — кандидаты

- [x] Исправлено: Alpha 0.1 не запускалась («app\current is missing») — имя версии 41 символ при лимите 32;
      CI теперь называет версию `minotaur-medusa-<sha8>-<run>-<attempt>` (движок `b572b956`)
- [x] Черновые 56 кадров героини (шесть листов ChatGPT, шея сохранена) → `tools/import_portraits.py`, 2026-11-07
- [ ] **Игровая проверка Alpha 0.2**: запуск, кадры героини (моргание, речь, «нет»/«да», уклонение, урон, состояния)
- [ ] Доработка кадров: 18 (направление взгляда), 32–33 (другое лицо в кивке), 21–33 (скачок стиля и размера
      к 01), 12 (край камня); решить, остаётся ли листовой 01 или отдельный утверждённый мастер
- [ ] ТЗ и `tools/make_portrait_prompts.py`: убрать требование «no neck» (шея обязательна)
- [ ] `finish_patch.py`: пересчитывать SHA256 в отчёте `*.json` после добавления README Medusa
- [ ] Своя картинка куклы `med01bod.png` 166×594 (голова Medusa на кукле) → колонка 9 в `character_data.append.txt`
- [ ] Своя иллюстрация карточки 120×120 (`illustration` в `ruleset.yml`), вместо карты MM7 `out10`
- [ ] Первые объекты и NPC Medusa на Нигоне (QBits/topics 20000–20999), изоляция выходов при необходимости
- [ ] Своя стартовая точка/безопасная зона, если стража или спавны мешают тестам
- [ ] Обратный патч или инструкция возврата на чистый Minotaur после первого удачного старта (если понадобится)
- [ ] Новые базисы: после успешной установки взять `minotaur-baseline.json` из артефакта metadata в
      `packaging/minotaur/bases/` ветки Medusa, чтобы следующие патчи ставились поверх Medusa 0.1

## Фаза E — своя карта (после Нигона)

- [ ] Сборка компилятора indoor-карт и его тестов в `openyamm-medusa/build`
- [ ] Итерация 1 башни ([план](design/first-map.md)); исправление старта на indoor-карте (аудит §1), если понадобится
