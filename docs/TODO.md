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
- [x] Windows CI `medusa-windows.yml`, патч `Project-Medusa-Alpha-0.1-Windows-Patch.zip`
- [ ] **Игровая проверка у пользователя** (чек-лист в `README-MEDUSA-RU.txt` патча): вкладки 16:9/4:3, карточка,
      создание партии, старт, движение, сохранение/загрузка, кукла и экипировка, Standard и MAW без изменений
- [ ] Длинное тире в «Project Medusa — Prologue» в шрифте меню (если не рисуется — заменить в `ruleset.yml`)
- [ ] Поведение стражи Нигона (Water Warlock, группа 55) к партии 1 уровня

## Alpha 0.2 — кандидаты

- [ ] Финальные 56 кадров героини → `tools/import_portraits.py` (формат: [portraits.md](design/portraits.md))
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
