# Portfolio content: single source of truth

Every number here is verified against code, data or Lev's own statement. Builders use this text as is.
Do not add claims, adjectives or slogans. Style: short, active voice, numbers, no dashes (neither em nor en dash, not even in titles), no emoji, no explainer notes.

Language: English is the default. Russian is a full alternative set, switched by an EN / RU control; the page remembers the choice (?lang=ru also works).

---

## Header

EN
- Name: Lev Skorokhodov
- Role: AI engineer
- Line: I build LLM agents and the harness around Claude and Codex, and ship them to production.
- Contact action: Telegram

RU
- Name: Лев Скороходов
- Role: AI-инженер
- Line: Строю LLM-агентов и харнесс вокруг Claude и Codex и довожу их до продакшна.
- Contact action: Telegram

## What I do (3 items)

EN
1. Agents and harness. Parallel Claude and Codex subagents, instruction files per task type, acceptance by diff, tests and render checks.
2. Prototype to production. VPS, nginx, systemd, CI, snapshots before every deploy. 7 services live on one server.
3. Web and visual. Interfaces, design systems, AI images and video.

RU
1. Агенты и харнесс. Параллельные сабагенты Claude и Codex, файл-инструкция на каждый тип задачи, приёмка по диффу, тестам и проверке рендера.
2. От прототипа до продакшна. VPS, nginx, systemd, CI, снапшот перед каждым деплоем. 7 сервисов живут на одном сервере.
3. Веб и визуал. Интерфейсы, дизайн-системы, AI-изображения и видео.

---

## Projects (order is fixed)

### 01 Floor plan pipeline

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

### 02 Trade System

EN
- Kind: Accounting system and OCR bot, in production
- Result: Runs trips, purchases, stock and settlements for a produce import business. Invoices go in by photo.
- Facts:
  - 9 modules: sales, AI inbox, purchases, trips, FIFO warehouse, deliveries, price list, settlements, catalogs.
  - Telegram bot reads photos of handwritten invoices with Claude Sonnet on AWS Bedrock, matches lines to the live catalog and queues them for approval. The public demo bot runs the same flow on GPT-4o Vision.
  - 10 to 30 invoices a day, peak 60.
  - Built solo from scratch with Claude Code on Opus 4.8. MVP in 3 to 4 weeks.
  - Reverse proxy in Moscow keeps the offshore server reachable for staff in Russia.
  - The client bought out the code, so it is not public. I walk through the architecture on request.
- Stack: React 18, Vite, Node.js, Express, PostgreSQL, Claude on AWS Bedrock, OpenAI API (demo), Telegram Bot API.
- Links: Demo https://lab.prfo.design/trade/ | OCR bot https://t.me/formagicowbot

RU
- Kind: Учётная система и OCR-бот, в продакшне
- Result: Ведёт рейсы, закупки, склад и взаиморасчёты импортёра овощей и фруктов. Накладные заходят фотографией.
- Facts:
  - 9 модулей: продажи, AI-инбокс, закупки, рейсы, склад по FIFO, доставки, прайс-лист, взаиморасчёты, справочники.
  - Telegram-бот читает фото рукописных накладных через Claude Sonnet на AWS Bedrock, сопоставляет строки с живым каталогом и ставит в очередь на подтверждение. Публичный демо-бот повторяет этот путь на GPT-4o Vision.
  - 10-30 накладных в день, пик 60.
  - Собрал один с нуля в Claude Code на Opus 4.8. MVP за 3-4 недели.
  - Реверс-прокси в Москве держит зарубежный сервер доступным для сотрудников в России.
  - Код выкуплен клиентом, поэтому не публикуется. Архитектуру и устройство расскажу по запросу.
- Stack: same as EN.
- Links: Демо | OCR-бот

### 03 Telegram store

EN
- Kind: Telegram Mini App and bot, client project in progress
- Result: A shop for used Apple devices inside Telegram. The seller fills in one bot wizard and the lot goes to the channel, the Mini App and the website at once. A sale removes it everywhere.
- Facts:
  - One React app runs as a Telegram Mini App and as a website. Mini App requests are checked by HMAC of Telegram initData.
  - Bot wizard: photos, nested model picker, condition, price, then a 1:1 preview of the channel post.
  - 340 tests run offline in 11 seconds. A guard test fails on any emoji in bot texts.
  - Built by an agent loop: Sonnet subagents write routine parts, Opus the complex logic, acceptance by diff, pytest and curl on staging. 51 commits in 5 working days.
- Stack: Python 3.12, FastAPI, aiogram 3, SQLAlchemy 2, SQLite, Alembic, React 18, Vite, TypeScript, Tailwind.
- Links: Code https://github.com/shorokhlev-sketch/telegram-store

RU
- Kind: Telegram Mini App и бот, клиентский проект в работе
- Result: Магазин б/у техники Apple внутри Telegram. Продавец заполняет один мастер в боте, и лот сразу появляется в канале, в Mini App и на сайте. После продажи лот исчезает везде.
- Facts:
  - Одно React-приложение работает как Telegram Mini App и как сайт. Запросы Mini App проверяются по HMAC от initData Telegram.
  - Мастер в боте: фото, вложенный выбор модели, состояние, цена и превью поста в канале один в один.
  - 340 тестов проходят офлайн за 11 секунд. Тест-сторож падает на любом эмодзи в текстах бота.
  - Собран агентным циклом: сабагенты Sonnet пишут рутину, Opus сложную логику, приёмка по диффу, pytest и curl на стейджинге. 51 коммит за 5 рабочих дней.
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
- Kind: Sales site and CRM, client project
- Result: Sells apartments in a 26 floor residential tower in Batumi and tracks every lead to its source.
- Facts:
  - Apartment picker over 279 units: 3D, floor plans, a sales grid and a PDF plan for every unit.
  - CRM with agent referral links, 90 day first touch attribution, UTM and click ID tracking, CPL, CAC and ROAS.
  - Lead dedupe by phone or Telegram. Apartment statuses sync back to the site.
  - CRM v0.1 went from schema to production in 2 hours 40 minutes.
- Stack: JavaScript, Node.js, Fastify, SQLite, nginx.
- Links: Site https://lab.prfo.design/maisi/ | Site code https://github.com/shorokhlev-sketch/apartment-picker | CRM code https://github.com/shorokhlev-sketch/realestate-crm

RU
- Kind: Сайт продаж и CRM, клиентский проект
- Result: Продаёт квартиры в 26-этажной башне в Батуми и ведёт каждую заявку до источника.
- Facts:
  - Подбор по 279 квартирам: 3D, планы этажей, шахматка и PDF-план на каждую квартиру.
  - CRM: реферальные ссылки агентов, атрибуция по первому касанию на 90 дней, UTM и click ID, CPL, CAC и ROAS.
  - Дедупликация заявок по телефону или Telegram. Статусы квартир синхронизируются с сайтом.
  - CRM v0.1 прошла путь от схемы до продакшна за 2 часа 40 минут.
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
- Links: Visuals https://prfo.design | Code https://github.com/shorokhlev-sketch/ai-video-pipeline

RU
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

Labels of the mode switch in each project scene, in segment order. Desktop = 600 px and wider; Phone = capsule below 600 px.

01 Floor plan pipeline
- EN desktop: Floor plan, 2BR 2201, Studio 1005, PDF layers, Unit editor | EN phone: Floor plan, 2BR 2201, Studio 1005
- RU desktop: План этажа, 2BR 2201, Студия 1005, Слои PDF, Редактор квартиры | RU phone: План этажа, 2BR 2201, Студия 1005

02 Trade System
- EN desktop: Sales, AI inbox, Trip, Price list | EN phone: Settlements, Sales
- RU desktop: Продажи, AI-инбокс, Рейс, Прайс-лист | RU phone: Взаиморасчёты, Продажи

03 Telegram store
- EN desktop: Catalog, Search, Lot, Design board | EN phone: Catalog, Filters, Lot, Request
- RU desktop: Каталог, Поиск, Лот, Доска дизайна | RU phone: Каталог, Фильтры, Лот, Заявка

04 Content Factory
- EN desktop: Scenes, Subtitles, Clips, Trim | EN phone: Scenes, Subtitles, Clips
- RU desktop: Сцены, Субтитры, Клипы, Обрезка | RU phone: Сцены, Субтитры, Клипы

05 26 MAISI
- EN desktop: 3D, Floor plans, Grid, Unit, CRM | EN phone: 3D, Floor plans, Unit
- RU desktop: 3D, Планы этажей, Шахматка, Квартира, CRM | RU phone: 3D, Планы этажей, Квартира

06 AI video production
- EN desktop: Copper, Stone, Porcelain, Technics, Storyboard | EN phone: Copper, Stone, Porcelain
- RU desktop: Медь, Камень, Фарфор, Technics, Раскадровка | RU phone: Медь, Камень, Фарфор

07 matscout
- EN desktop: Result, Agent steps, Table, Diagram, 3D | EN phone: Result, 3D
- RU desktop: Результат, Шаги агента, Таблица, Диаграмма, 3D | RU phone: Результат, 3D

---

## Stack block

EN / RU same list:
Claude Code, Codex, Claude and OpenAI APIs, MCP, Python, TypeScript, React, Node.js, FastAPI, Fastify, aiogram, Telegram Mini Apps, PostgreSQL, SQLite, Playwright, Figma, Higgsfield, nginx, systemd, Docker.

## Contacts

EN
- Telegram @prfowax https://t.me/prfowax
- GitHub https://github.com/shorokhlev-sketch

RU
- Telegram @prfowax
- GitHub

## Screenshots

Folder shots/<project>/ (not in this repo) with index.json in each (file, url, viewport, shows, quality_notes).
Projects map: floor plans -> shots/floorplans (unit-2201-plan-*, unit-1005-plan-* for the apartment modes), trade -> shots/trade, telegram store -> shots/tgstore (do not use desktop-04-lot-gallery: watermarked press photo), content factory -> shots/factory, 26 MAISI -> shots/maisi and shots/maisi-crm, AI video -> shots/aivisual (Technics audio has no music rights: stills only), matscout -> shots/matscout.
