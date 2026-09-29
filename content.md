# Portfolio content: single source of truth

Every number here is verified against code, data or Lev's own statement. Builders use this text as is.
Do not add claims, adjectives or slogans. Style: short, active voice, numbers, no dashes (neither em nor en dash, not even in titles), no emoji, no explainer notes.

Language: Russian for a browser set to Russian, English otherwise. Russian is a full alternative set, switched by an EN / RU control; the page remembers the choice (?lang=ru and ?lang=en also work).

Audience: business owners who want manual work automated (Lev, 2026-09-30). Engineering detail stays in the facts, not in the header.

---

## Header

EN
- Name: Lev Skorokhodov
- Role: AI engineer
- Line: I build AI systems that take manual work off a business: invoices read from photos, stock and settlements, sales sites with CRM, shops in Telegram.
- Contact action: Telegram

RU
- Name: Лев Скороходов
- Role: AI-инженер
- Line: Делаю ИИ-системы, которые снимают с бизнеса ручную работу: читают накладные по фото, ведут склад и взаиморасчёты, собирают заявки в CRM, продают через Telegram.
- Contact action: Telegram

## What I do (3 items)

EN
1. Documents to data. A bot reads photos of invoices and forms, matches every line to your catalog and sends unclear ones to a person.
2. Accounting and sales. Stock, settlements and leads in one system. Every lead is tracked to its source.
3. Launch and upkeep. Server, domain, a backup before every update. 7 services run on one server today.

RU
1. Документы в данные. Бот читает фото накладных и бланков, сопоставляет каждую строку с вашим каталогом, а неясные отдаёт человеку.
2. Учёт и продажи. Склад, взаиморасчёты и заявки в одной системе. У каждой заявки виден источник.
3. Запуск и сопровождение. Сервер, домен, бэкап перед каждым обновлением. 7 сервисов сейчас работают на одном сервере.

---

## Projects (order is fixed: Trade System first for the business buyer, Lev 2026-09-30)

RU titles: a project without a RU Title line keeps its EN title in Russian.

### 01 Trade System

EN
- Kind: Accounting system and OCR bot, client project
- Result: Ran trips, purchases, stock and settlements for a produce import business. Invoices went in by photo.
- Facts:
  - Telegram bot read photos of handwritten invoices with Claude Sonnet on AWS Bedrock, matched lines to the live catalog and queued them for approval. The public demo bot runs the same flow on GPT-4o Vision.
  - The bot handled 10 to 30 invoices a day, peak 60.
  - The client bought out the code. The AI part is rewritten from scratch as a public repo: extraction, catalog matching, approval queue, eval on synthetic invoices.
  - 0 wrong catalog matches on 124 lines of 20 synthetic invoices: an unreadable name goes to review instead of a guess. $0.003 to $0.026 per invoice across 3 models.
  - 9 modules: sales, AI inbox, purchases, trips, FIFO warehouse, deliveries, price list, settlements, catalogs.
  - Built solo. MVP in 5 days from scratch.
  - Reverse proxy in Moscow kept the offshore server reachable for staff in Russia.
- Stack: React 18, Vite, Node.js, Express, PostgreSQL, Claude on AWS Bedrock, OpenAI API (demo), Telegram Bot API.
- Links: Demo https://lab.prfo.design/trade/ | OCR bot https://t.me/formagicowbot | OCR code https://github.com/shorokhlev-sketch/invoice-ocr

RU
- Kind: Учётная система и OCR-бот, клиентский проект
- Result: Вела рейсы, закупки, склад и взаиморасчёты импортёра овощей и фруктов. Накладные заходили фотографией.
- Facts:
  - Telegram-бот читал фото рукописных накладных через Claude Sonnet на AWS Bedrock, сопоставлял строки с живым каталогом и ставил в очередь на подтверждение. Публичный демо-бот повторяет этот путь на GPT-4o Vision.
  - Бот обрабатывал 10-30 накладных в день, пик 60.
  - Код выкуплен клиентом. AI-часть переписана с нуля в публичный репозиторий: распознавание, сопоставление с каталогом, очередь подтверждения, eval на синтетических накладных.
  - 0 ошибочных сопоставлений с каталогом на 124 строках 20 синтетических накладных: нечитаемое название уходит на проверку, а не угадывается. $0.003-0.026 за накладную на 3 моделях.
  - 9 модулей: продажи, AI-инбокс, закупки, рейсы, склад по FIFO, доставки, прайс-лист, взаиморасчёты, справочники.
  - Собрал один. MVP за 5 дней с нуля.
  - Реверс-прокси в Москве держал зарубежный сервер доступным для сотрудников в России.
- Stack: same as EN.
- Links: Демо | OCR-бот | Код OCR

### 02 Floor plan pipeline

EN
- Kind: Agent pipeline, client project
- Result: Turns a 114 page architectural PDF into clean vector plans for 279 apartments on 25 floors.
- Facts:
  - Reads PDF layers instead of guessing by color: 39k objects per floor down to 1.9k.
  - Areas match the official schedule within 0.05 m².
  - 5 Sonnet agents in parallel close 25 floors in about 2 minutes.
  - Manual edits in Figma are diffed by object ID and become batch rules for the next run.
  - Every write passes a 3 second Playwright render check. Snapshot at every stage.
- Stack: Python, PyMuPDF, shapely, Figma MCP, Playwright, Claude Code subagents.
- Links: Floors live https://lab.prfo.design/maisi/select.html#/floors | Code https://github.com/shorokhlev-sketch/floorplan-pipeline

RU
- Title: Конвейер планировок
- Kind: Агентный конвейер, клиентский проект
- Result: Превращает архитектурный PDF на 114 страниц в чистые векторные планы 279 квартир на 25 этажах.
- Facts:
  - Читает слои PDF вместо угадывания по цвету: 39 тыс. объектов на этаж сжимаются до 1,9 тыс.
  - Площади сходятся с официальной экспликацией до 0,05 м².
  - 5 агентов Sonnet параллельно закрывают 25 этажей примерно за 2 минуты.
  - Ручные правки в Figma сравниваются по ID объектов и становятся пакетными правилами для следующего прогона.
  - Каждая запись проходит 3-секундную проверку рендера в Playwright. Снапшот на каждой стадии.
- Stack: same as EN.
- Links: Этажи вживую | Код

### 03 Telegram store

EN
- Kind: Telegram Mini App and bot, client project in progress
- Result: A shop for used Apple devices inside Telegram. The seller fills in one bot wizard and the lot goes to the channel, the Mini App and the website at once. A sale removes it everywhere.
- Facts:
  - One React app runs as a Telegram Mini App and as a website. Mini App requests are checked by HMAC of Telegram initData.
  - Bot wizard: photos, nested model picker, condition, price, then a 1:1 preview of the channel post.
  - 340 tests run offline in under 20 seconds.
  - Built by an agent loop: Sonnet subagents write routine parts, Opus the complex logic, acceptance by diff, pytest and curl on staging.
- Stack: Python 3.12, FastAPI, aiogram 3, SQLAlchemy 2, SQLite, Alembic, React 18, Vite, TypeScript, Tailwind.
- Links: Code https://github.com/shorokhlev-sketch/telegram-store

RU
- Title: Магазин в Telegram
- Kind: Telegram Mini App и бот, клиентский проект в работе
- Result: Магазин б/у техники Apple внутри Telegram. Продавец заполняет один мастер в боте, и лот сразу появляется в канале, в Mini App и на сайте. После продажи лот исчезает везде.
- Facts:
  - Одно React-приложение работает как Telegram Mini App и как сайт. Запросы Mini App проверяются по HMAC от initData Telegram.
  - Мастер в боте: фото, вложенный выбор модели, состояние, цена и превью поста в канале один в один.
  - 340 тестов проходят офлайн меньше чем за 20 секунд.
  - Собран агентным циклом: сабагенты Sonnet пишут рутину, Opus сложную логику, приёмка по диффу, pytest и curl на стейджинге.
- Stack: same as EN.
- Links: Код

### 04 Content Factory

EN
- Kind: LLM video pipeline
- Result: Cuts a 23 minute episode into 5 to 7 vertical clips with burned subtitles for about $0.27 in API cost.
- Facts:
  - 6 stages: Whisper word timestamps, typo check, GPT-4o scene picking, punctuation, FFmpeg render.
  - Content hash cache: a repeated upload costs nothing.
  - Transcription is half the cost: $0.14 of $0.27, measured on 10 episodes.
  - Review UI with live logs over SSE, trim handles, banner editor, render queue, Telegram publishing.
- Stack: Python, FastAPI, SSE, OpenAI API, FFmpeg, ASS subtitles.
- Links: Live demo https://factory.prfo.design | Code https://github.com/shorokhlev-sketch/clip-factory

RU
- Kind: LLM-конвейер для видео
- Result: Режет 23-минутную серию на 5-7 вертикальных клипов с вшитыми субтитрами примерно за $0,27 на API.
- Facts:
  - 6 стадий: пословные таймкоды Whisper, проверка опечаток, выбор сцен GPT-4o, пунктуация, рендер FFmpeg.
  - Кеш по хешу файла: повторная загрузка ничего не стоит.
  - Половина стоимости уходит на транскрипцию: $0,14 из $0,27, замер на 10 сериях.
  - Интерфейс ревью: живые логи по SSE, ручки обрезки, редактор баннера, очередь рендера, публикация в Telegram.
- Stack: same as EN.
- Links: Живое демо | Код

### 05 26 MAISI

EN
- Kind: Sales site and CRM, client project in progress
- Result: Apartment picker and lead tracking for a 26 floor residential tower in Batumi, before sales start.
- Facts:
  - Apartment picker over 279 units: 3D, floor plans, a sales grid and a PDF plan for every unit.
  - CRM with agent referral links, 90 day first touch attribution, UTM and click ID tracking, CPL, CAC and ROAS.
  - Lead dedupe by phone or Telegram. Apartment statuses sync back to the site.
- Stack: JavaScript, Node.js, Fastify, SQLite, nginx.
- Links: Site https://lab.prfo.design/maisi/ | Site code https://github.com/shorokhlev-sketch/apartment-picker | CRM code https://github.com/shorokhlev-sketch/realestate-crm

RU
- Kind: Сайт продаж и CRM, клиентский проект в работе
- Result: Подбор квартир и учёт заявок для 26-этажной башни в Батуми, до старта продаж.
- Facts:
  - Подбор по 279 квартирам: 3D, планы этажей, шахматка и PDF-план на каждую квартиру.
  - CRM: реферальные ссылки агентов, атрибуция по первому касанию на 90 дней, UTM и click ID, CPL, CAC и ROAS.
  - Дедупликация заявок по телефону или Telegram. Статусы квартир синхронизируются с сайтом.
- Stack: same as EN.
- Links: Сайт | Код сайта | Код CRM

### 06 AI video production

EN
- Kind: AI images and video on Higgsfield
- Result: Fashion and product films without the plastic AI look. Claude generates frames and clips, and I approve every frame on a live storyboard before any video is made.
- Facts:
  - 6 campaigns, 103 planned shots, 244 generated frames, 47 clips.
  - Technics SB-MX200 spec film: 27 seconds cut from 38 generated clips. The choice between Seedance and Kling is settled by measured motion, not taste.
  - Storyboard with a job bus: a button on a shot wakes Claude, which picks up the job. After 16 operator rules, credit waste fell from about a third to zero.
- Stack: Higgsfield CLI, Nano Banana Pro, Seedream 5, Seedance 2.0 and 2.5, Kling 3.0, Palmier over MCP, Claude Code skills, Node.js.
- Links: Visuals https://prfo.design/visual/ | Code https://github.com/shorokhlev-sketch/ai-video-pipeline

RU
- Title: AI-видеопродакшн
- Kind: AI-изображения и видео на Higgsfield
- Result: Фэшн- и продуктовые ролики без пластикового AI-вида. Claude генерирует кадры и клипы, а я принимаю каждый кадр на живой раскадровке до генерации видео.
- Facts:
  - 6 кампаний, 103 кадра в раскадровках, 244 сгенерированных кадра, 47 клипов.
  - Spec-ролик Technics SB-MX200: 27 секунд из 38 сгенерированных клипов. Выбор между Seedance и Kling решают замеры движения, а не вкус.
  - Раскадровка с шиной задач: кнопка на кадре будит Claude, и он забирает задачу. После 16 правил оператора потери кредитов упали примерно с трети до нуля.
- Stack: same as EN.
- Links: Визуал | Код

### 07 matscout

EN
- Kind: Personal project, university course paper
- Result: MCP server and research agent over materials databases, built for a course paper in materials science.
- Facts:
  - 25 tools behind one MCP server. The web agent, Claude Desktop and Claude Code call the same endpoint.
  - Two phase agent: discovery on 11 tools, analysis on 17.
  - 75 tests, mypy strict in CI. Built in 4 days.
- Stack: Python, FastMCP, OpenAI Responses API, FastAPI, SQLite, pymatgen.
- Links: Live https://matscout.prfo.design | Code https://github.com/shorokhlev-sketch/matscout | MCP endpoint https://matscout.prfo.design/mcp/http/

RU
- Kind: Личный проект, курсовая
- Result: MCP-сервер и исследовательский агент поверх баз данных материалов, сделан под курсовую по материаловедению.
- Facts:
  - 25 инструментов за одним MCP-сервером. Веб-агент, Claude Desktop и Claude Code ходят в один эндпоинт.
  - Агент в две фазы: поиск на 11 инструментах, анализ на 17.
  - 75 тестов, mypy strict в CI. Собран за 4 дня.
- Stack: same as EN.
- Links: Живая версия | Код | MCP-эндпоинт

---

## Scene modes

Labels of the mode switch in each project scene, in segment order. Phones show the same captures and labels in a capsule below 600 px.

01 Trade System
- EN desktop: AI inbox, Sales, Trip, Price list
- RU desktop: AI-инбокс, Продажи, Рейс, Прайс-лист

02 Floor plan pipeline
- EN desktop: Floor plan, 2BR 2201, Studio 1005, PDF layers, Unit editor
- RU desktop: План этажа, 2BR 2201, Студия 1005, Слои PDF, Редактор квартиры

03 Telegram store
- EN desktop: Catalog, Search, Lot, Design board
- RU desktop: Каталог, Поиск, Лот, Доска дизайна

04 Content Factory
- EN desktop: Scenes, Subtitles, Clips, Trim
- RU desktop: Сцены, Субтитры, Клипы, Обрезка

05 26 MAISI
- EN desktop: Floor plans, Grid, Unit, CRM, 3D
- RU desktop: Планы этажей, Шахматка, Квартира, CRM, 3D

06 AI video production
- EN desktop: Copper, Stone, Porcelain, Technics, Storyboard
- RU desktop: Медь, Камень, Фарфор, Technics, Раскадровка

07 matscout
- EN desktop: Result, Agent steps, Table, Diagram, 3D
- RU desktop: Результат, Шаги агента, Таблица, Диаграмма, 3D

---

## Stack block

EN / RU same list:
Claude Code, Codex, Claude and OpenAI APIs, MCP, Python, TypeScript, React, Node.js, FastAPI, Fastify, aiogram, Telegram Mini Apps, PostgreSQL, SQLite, Playwright, Figma, Higgsfield, nginx, systemd, Docker.

## Contacts

EN
- Telegram @prfowax https://t.me/prfowax
- Email levsk@icloud.com mailto:levsk@icloud.com
- GitHub https://github.com/shorokhlev-sketch

RU
- Telegram @prfowax
- Email levsk@icloud.com
- GitHub

## Screenshots

Folder shots/<project>/ (not in this repo) with index.json in each (file, url, viewport, shows, quality_notes).
Projects map: floor plans -> shots/floorplans (unit-2201-plan-*, unit-1005-plan-* for the apartment modes), trade -> shots/trade, telegram store -> shots/tgstore (do not use desktop-04-lot-gallery: watermarked press photo), content factory -> shots/factory, 26 MAISI -> shots/maisi and shots/maisi-crm, AI video -> shots/aivisual (Technics audio has no music rights: stills only), matscout -> shots/matscout.
