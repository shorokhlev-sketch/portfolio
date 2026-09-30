# Generates site/index.html and assets/js/i18n.js from one data table.
# Copy is verbatim from ./content.md. **x** marks a number token rendered bold.
import json, os, re, subprocess, html, sys

ROOT = './site'
IMG = ROOT + '/assets/img'

def dims(path):
    out = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', path], capture_output=True, text=True).stdout
    w = int(re.search(r'pixelWidth: (\d+)', out).group(1)); h = int(re.search(r'pixelHeight: (\d+)', out).group(1))
    return w, h

def md(s):
    """escape and turn **x** into <b>x</b>"""
    s = html.escape(s, quote=False)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)

def plain(s):
    return s.replace('**', '')

SITE = {
    'en': {
        'name': 'Lev Skorokhodov', 'role': 'AI engineer',
        'line': 'I build AI systems that take manual work off a business: invoices read from photos, stock and settlements, sales sites with CRM, shops in Telegram.',
        'cta': 'Telegram',
        'do': [
            ('Documents to data.', 'A bot reads photos of invoices and forms, matches every line to your catalog and sends unclear ones to a person.'),
            ('Accounting and sales.', 'Stock, settlements and leads in one system. Every lead is tracked to its source.'),
            ('Launch and upkeep.', 'Server, domain, a backup before every update. **7** services run on one server today.'),
        ],
        'tg': 'Telegram @prfowax', 'mail': 'levsk@icloud.com', 'gh': 'GitHub',
        'close': 'Close', 'prev': 'Previous', 'next': 'Next',
    },
    'ru': {
        'name': 'Лев Скороходов', 'role': 'AI-инженер',
        'line': 'Делаю ИИ-системы, которые снимают с бизнеса ручную работу: читают накладные по фото, ведут склад и взаиморасчёты, собирают заявки в CRM, продают через Telegram.',
        'cta': 'Telegram',
        'do': [
            ('Документы в данные.', 'Бот читает фото накладных и бланков, сопоставляет каждую строку с вашим каталогом, а неясные отдаёт человеку.'),
            ('Учёт и продажи.', 'Склад, взаиморасчёты и заявки в одной системе. У каждой заявки виден источник.'),
            ('Запуск и сопровождение.', 'Сервер, домен, бэкап перед каждым обновлением. **7** сервисов сейчас работают на одном сервере.'),
        ],
        'tg': 'Telegram @prfowax', 'mail': 'levsk@icloud.com', 'gh': 'GitHub',
        'close': 'Закрыть', 'prev': 'Назад', 'next': 'Далее',
    },
}
STACK_ALL = 'Claude Code, Codex, Claude and OpenAI APIs, MCP, Python, TypeScript, React, Node.js, FastAPI, Fastify, aiogram, Telegram Mini Apps, PostgreSQL, SQLite, Playwright, Figma, Higgsfield, nginx, systemd, Docker.'

PROJECTS = [
    {
        'n': '01', 'slug': 'trade', 'title': 'Trade System',
        'kind': {'en': 'Accounting system and OCR bot, client project', 'ru': 'Учётная система и OCR-бот, клиентский проект'},
        'result': {'en': 'Ran trips, purchases, stock and settlements for a produce import business. Invoices went in by photo.',
                   'ru': 'Вела рейсы, закупки, склад и взаиморасчёты импортёра овощей и фруктов. Накладные заходили фотографией.'},
        'facts': {'en': [
            'Telegram bot read photos of handwritten invoices with Claude Sonnet on AWS Bedrock, matched lines to the live catalog and queued them for approval. The public demo bot runs the same flow on GPT-4o Vision.',
            'The bot handled **10 to 30** invoices a day, peak **60**.',
            'The client bought out the code. The AI part is rewritten from scratch as a public repo: extraction, catalog matching, approval queue, eval on synthetic invoices.',
            '**0** wrong catalog matches on **124** lines of **20** synthetic invoices: an unreadable name goes to review instead of a guess. **$0.003 to $0.026** per invoice across 3 models.',
            '**9** modules: sales, AI inbox, purchases, trips, FIFO warehouse, deliveries, price list, settlements, catalogs.',
            'Built solo. MVP in **5** days from scratch.',
            'Reverse proxy in Moscow kept the offshore server reachable for staff in Russia.'],
            'ru': [
            'Telegram-бот читал фото рукописных накладных через Claude Sonnet на AWS Bedrock, сопоставлял строки с живым каталогом и ставил в очередь на подтверждение. Публичный демо-бот повторяет этот путь на GPT-4o Vision.',
            'Бот обрабатывал **10-30** накладных в день, пик **60**.',
            'Код выкуплен клиентом. AI-часть переписана с нуля в публичный репозиторий: распознавание, сопоставление с каталогом, очередь подтверждения, eval на синтетических накладных.',
            '**0** ошибочных сопоставлений с каталогом на **124** строках **20** синтетических накладных: нечитаемое название уходит на проверку, а не угадывается. **$0.003-0.026** за накладную на 3 моделях.',
            '**9** модулей: продажи, AI-инбокс, закупки, рейсы, склад по FIFO, доставки, прайс-лист, взаиморасчёты, справочники.',
            'Собрал один. MVP за **5** дней с нуля.',
            'Реверс-прокси в Москве держал зарубежный сервер доступным для сотрудников в России.']},
        'stack': 'React 18, Vite, Node.js, Express, PostgreSQL, Claude on AWS Bedrock, OpenAI API (demo), Telegram Bot API.',
        'links': [
            {'href': 'https://lab.prfo.design/trade/', 'label': {'en': 'Demo', 'ru': 'Демо'}},
            {'href': 'https://t.me/formagicowbot', 'label': {'en': 'OCR bot', 'ru': 'OCR-бот'}},
            {'href': 'https://github.com/shorokhlev-sketch/invoice-ocr', 'label': {'en': 'OCR code', 'ru': 'Код OCR'}},
        ],
        # AI inbox first: the raw name to catalog match is the proof a business buyer looks for
        'desk': [('ai-inbox', 'AI inbox', 'AI-инбокс'), ('sales', 'Sales', 'Продажи'),
                 ('trip', 'Trip', 'Рейс'), ('pricelist', 'Price list', 'Прайс-лист')],
        'mob': [('settlements', 'Settlements', 'Взаиморасчёты'), ('sales', 'Sales', 'Продажи')],
    },
    {
        'n': '02', 'slug': 'maisi', 'title': '26 MAISI',
        'kind': {'en': 'Sales site and CRM, client project in progress', 'ru': 'Сайт продаж и CRM, клиентский проект в работе'},
        'result': {'en': 'Apartment picker and lead tracking for a **26** floor residential tower in Batumi, before sales start.',
                   'ru': 'Подбор квартир и учёт заявок для **26**-этажной башни в Батуми, до старта продаж.'},
        'facts': {'en': [
            'Apartment picker over **279** units: 3D, floor plans, a sales grid and a PDF plan for every unit.',
            'CRM with agent referral links, **90** day first touch attribution, UTM and click ID tracking, CPL, CAC and ROAS.',
            'Lead dedupe by phone or Telegram. Apartment statuses sync back to the site.'],
            'ru': [
            'Подбор по **279** квартирам: 3D, планы этажей, шахматка и PDF-план на каждую квартиру.',
            'CRM: реферальные ссылки агентов, атрибуция по первому касанию на **90** дней, UTM и click ID, CPL, CAC и ROAS.',
            'Дедупликация заявок по телефону или Telegram. Статусы квартир синхронизируются с сайтом.']},
        'stack': 'JavaScript, Node.js, Fastify, SQLite, nginx.',
        'links': [
            {'href': 'https://lab.prfo.design/maisi/', 'label': {'en': 'Site', 'ru': 'Сайт'}},
            {'href': 'https://github.com/shorokhlev-sketch/apartment-picker', 'label': {'en': 'Site code', 'ru': 'Код сайта'}},
            {'href': 'https://github.com/shorokhlev-sketch/realestate-crm', 'label': {'en': 'CRM code', 'ru': 'Код CRM'}},
        ],
        # 3D view: the AI tower frames carry a PLACEHOLDER lattice until the architect's model arrives
        # 3D last (Lev 2026-09-30): its frames carry the PLACEHOLDER lattice, a buyer sees the real plans first
        'desk': [('floorplan-status', 'Floor plans', 'Планы этажей'), ('grid', 'Grid', 'Шахматка'),
                 ('unit-detail', 'Unit', 'Квартира'), ('crm', 'CRM', 'CRM'), ('3d', '3D', '3D')],
        'mob': [('3d', '3D', '3D'), ('floorplan', 'Floor plans', 'Планы этажей'), ('unit-detail', 'Unit', 'Квартира')],
    },
    {
        'n': '03', 'slug': 'floorplans', 'title': 'Floor plan pipeline', 'title_ru': 'Конвейер планировок',
        'kind': {'en': 'Agent pipeline, client project', 'ru': 'Агентный конвейер, клиентский проект'},
        'result': {'en': 'Turns a **114** page architectural PDF into clean vector plans for **279** apartments on **25** floors.',
                   'ru': 'Превращает архитектурный PDF на **114** страниц в чистые векторные планы **279** квартир на **25** этажах.'},
        'facts': {'en': [
            'Reads PDF layers instead of guessing by color: **39k** objects per floor down to **1.9k**.',
            'Areas match the official schedule within **0.05 m²**.',
            '**5** Sonnet agents in parallel close **25** floors in about **2** minutes.',
            'Manual edits in Figma are diffed by object ID and become batch rules for the next run.',
            'Every write passes a **3** second Playwright render check. Snapshot at every stage.'],
            'ru': [
            'Читает слои PDF вместо угадывания по цвету: **39 тыс.** объектов на этаж сжимаются до **1,9 тыс.**',
            'Площади сходятся с официальной экспликацией до **0,05 м²**.',
            '**5** агентов Sonnet параллельно закрывают **25** этажей примерно за **2** минуты.',
            'Ручные правки в Figma сравниваются по ID объектов и становятся пакетными правилами для следующего прогона.',
            'Каждая запись проходит **3**-секундную проверку рендера в Playwright. Снапшот на каждой стадии.']},
        'stack': 'Python, PyMuPDF, shapely, Figma MCP, Playwright, Claude Code subagents.',
        'links': [
            # #/floors opens the floor plans view; the bare picker URL opens its 3D view (the generated tower)
            {'href': 'https://lab.prfo.design/maisi/select.html#/floors', 'label': {'en': 'Floors live', 'ru': 'Этажи вживую'}},
            {'href': 'https://github.com/shorokhlev-sketch/floorplan-pipeline', 'label': {'en': 'Code', 'ru': 'Код'}},
        ],
        'desk': [('floor-10-vector', 'Floor plan', 'План этажа'), ('unit-2201', '2BR 2201', '2BR 2201'),
                 ('unit-1005', 'Studio 1005', 'Студия 1005'), ('raw-layers', 'PDF layers', 'Слои PDF'),
                 ('unit-editor', 'Unit editor', 'Редактор квартиры')],
        'mob': [('floor-10-vector', 'Floor plan', 'План этажа'), ('unit-2201', '2BR 2201', '2BR 2201'),
                ('unit-1005', 'Studio 1005', 'Студия 1005')],
        # plan drawings on the scene grey: the phone frames sit in the middle of the scene, not at its top
        'mpos': 'center',
    },
    {
        'n': '04', 'slug': 'tgstore', 'title': 'Telegram store', 'title_ru': 'Магазин в Telegram',
        'kind': {'en': 'Telegram Mini App and bot, client project in progress', 'ru': 'Telegram Mini App и бот, клиентский проект в работе'},
        'result': {'en': 'A shop for used Apple devices inside Telegram. The seller fills in one bot wizard and the lot goes to the channel, the Mini App and the website at once. A sale removes it everywhere.',
                   'ru': 'Магазин б/у техники Apple внутри Telegram. Продавец заполняет один мастер в боте, и лот сразу появляется в канале, в Mini App и на сайте. После продажи лот исчезает везде.'},
        'facts': {'en': [
            'One React app runs as a Telegram Mini App and as a website. Mini App requests are checked by HMAC of Telegram initData.',
            'Bot wizard: photos, nested model picker, condition, price, then a 1:1 preview of the channel post.',
            '**340** tests run offline in under **20** seconds.',
            'Built by an agent loop: Sonnet subagents write routine parts, Opus the complex logic, acceptance by diff, pytest and curl on staging.'],
            'ru': [
            'Одно React-приложение работает как Telegram Mini App и как сайт. Запросы Mini App проверяются по HMAC от initData Telegram.',
            'Мастер в боте: фото, вложенный выбор модели, состояние, цена и превью поста в канале один в один.',
            '**340** тестов проходят офлайн меньше чем за **20** секунд.',
            'Собран агентным циклом: сабагенты Sonnet пишут рутину, Opus сложную логику, приёмка по диффу, pytest и curl на стейджинге.']},
        'stack': 'Python 3.12, FastAPI, aiogram 3, SQLAlchemy 2, SQLite, Alembic, React 18, Vite, TypeScript, Tailwind.',
        'links': [
            # no live storefront link: its page title carries the shop name that the captures blur
            {'href': 'https://github.com/shorokhlev-sketch/telegram-store', 'label': {'en': 'Code', 'ru': 'Код'}},
        ],
        # shop name blurred in every capture; desktop-04-lot-gallery (watermarked press photo) is never used
        'desk': [('catalog', 'Catalog', 'Каталог'), ('search', 'Search', 'Поиск'), ('lot', 'Lot', 'Лот'),
                 ('board', 'Design board', 'Доска дизайна')],
        'mob': [('catalog', 'Catalog', 'Каталог'), ('filters', 'Filters', 'Фильтры'), ('lot', 'Lot', 'Лот'),
                ('request', 'Request', 'Заявка')],
    },
    {
        'n': '05', 'slug': 'factory', 'title': 'Content Factory',
        'kind': {'en': 'LLM video pipeline', 'ru': 'LLM-конвейер для видео'},
        'result': {'en': 'Cuts a **23** minute episode into **5 to 7** vertical clips with burned subtitles for about **$0.27** in API cost.',
                   'ru': 'Режет **23**-минутную серию на **5-7** вертикальных клипов с вшитыми субтитрами примерно за **$0,27** на API.'},
        'facts': {'en': [
            '**6** stages: Whisper word timestamps, typo check, GPT-4o scene picking, punctuation, FFmpeg render.',
            'Content hash cache: a repeated upload costs nothing.',
            'Transcription is half the cost: **$0.14** of **$0.27**, measured on **10** episodes.',
            'Review UI with live logs over SSE, trim handles, banner editor, render queue, Telegram publishing.'],
            'ru': [
            '**6** стадий: пословные таймкоды Whisper, проверка опечаток, выбор сцен GPT-4o, пунктуация, рендер FFmpeg.',
            'Кеш по хешу файла: повторная загрузка ничего не стоит.',
            'Половина стоимости уходит на транскрипцию: **$0,14** из **$0,27**, замер на **10** сериях.',
            'Интерфейс ревью: живые логи по SSE, ручки обрезки, редактор баннера, очередь рендера, публикация в Telegram.']},
        'stack': 'Python, FastAPI, SSE, OpenAI API, FFmpeg, ASS subtitles.',
        'links': [
            {'href': 'https://factory.prfo.design', 'label': {'en': 'Live demo', 'ru': 'Живое демо'}},
            {'href': 'https://github.com/shorokhlev-sketch/clip-factory', 'label': {'en': 'Code', 'ru': 'Код'}},
        ],
        'desk': [('scenes', 'Scenes', 'Сцены'), ('subtitles', 'Subtitles', 'Субтитры'),
                 ('clips', 'Clips', 'Клипы'), ('trim', 'Trim', 'Обрезка')],
        'mob': [('scenes', 'Scenes', 'Сцены'), ('subtitles', 'Subtitles', 'Субтитры'), ('clips', 'Clips', 'Клипы')],
    },
    {
        'n': '06', 'slug': 'aivisual', 'title': 'AI video production', 'title_ru': 'AI-видеопродакшн',
        'kind': {'en': 'AI images and video on Higgsfield', 'ru': 'AI-изображения и видео на Higgsfield'},
        'result': {'en': 'Fashion and product films without the plastic AI look. Claude generates frames and clips, and I approve every frame on a live storyboard before any video is made.',
                   'ru': 'Фэшн- и продуктовые ролики без пластикового AI-вида. Claude генерирует кадры и клипы, а я принимаю каждый кадр на живой раскадровке до генерации видео.'},
        'facts': {'en': [
            '**6** campaigns, **103** planned shots, **244** generated frames, **47** clips.',
            'Technics SB-MX200 spec film: **27** seconds cut from **38** generated clips. The choice between Seedance and Kling is settled by measured motion, not taste.',
            'Storyboard with a job bus: a button on a shot wakes Claude, which picks up the job. After **16** operator rules, credit waste fell from about a third to zero.'],
            'ru': [
            '**6** кампаний, **103** кадра в раскадровках, **244** сгенерированных кадра, **47** клипов.',
            'Spec-ролик Technics SB-MX200: **27** секунд из **38** сгенерированных клипов. Выбор между Seedance и Kling решают замеры движения, а не вкус.',
            'Раскадровка с шиной задач: кнопка на кадре будит Claude, и он забирает задачу. После **16** правил оператора потери кредитов упали примерно с трети до нуля.']},
        'stack': 'Higgsfield CLI, Nano Banana Pro, Seedream 5, Seedance 2.0 and 2.5, Kling 3.0, Palmier over MCP, Claude Code skills, Node.js.',
        'links': [
            {'href': 'https://prfo.design/visual/', 'label': {'en': 'Visuals', 'ru': 'Визуал'}},
            {'href': 'https://github.com/shorokhlev-sketch/ai-video-pipeline', 'label': {'en': 'Code', 'ru': 'Код'}},
        ],
        # stills fill the scene edge to edge ('bleed'); the storyboard is a UI capture and stays whole inside the scene inset
        'desk': [('copper', 'Copper', 'Медь', 'bleed'), ('stone', 'Stone', 'Камень', 'bleed'),
                 ('porcelain', 'Porcelain', 'Фарфор', 'bleed'), ('technics', 'Technics', 'Technics', 'bleed'),
                 ('storyboard', 'Storyboard', 'Раскадровка')],
        'mob': [('copper', 'Copper', 'Медь'), ('stone', 'Stone', 'Камень'), ('porcelain', 'Porcelain', 'Фарфор')],
    },
    {
        'n': '07', 'slug': 'matscout', 'title': 'matscout',
        'kind': {'en': 'Personal project, university course paper', 'ru': 'Личный проект, курсовая'},
        'result': {'en': 'MCP server and research agent over materials databases, built for a course paper in materials science.',
                   'ru': 'MCP-сервер и исследовательский агент поверх баз данных материалов, сделан под курсовую по материаловедению.'},
        'facts': {'en': [
            '**25** tools behind one MCP server. The web agent, Claude Desktop and Claude Code call the same endpoint.',
            'Two phase agent: discovery on **11** tools, analysis on **17**.',
            '**75** tests, mypy strict in CI. Built in **4** days.'],
            'ru': [
            '**25** инструментов за одним MCP-сервером. Веб-агент, Claude Desktop и Claude Code ходят в один эндпоинт.',
            'Агент в две фазы: поиск на **11** инструментах, анализ на **17**.',
            '**75** тестов, mypy strict в CI. Собран за **4** дня.']},
        'stack': 'Python, FastMCP, OpenAI Responses API, FastAPI, SQLite, pymatgen.',
        'links': [
            {'href': 'https://matscout.prfo.design', 'label': {'en': 'Live', 'ru': 'Живая версия'}},
            {'href': 'https://github.com/shorokhlev-sketch/matscout', 'label': {'en': 'Code', 'ru': 'Код'}},
            # the endpoint answers a browser GET with a JSON-RPC error, so it is shown as selectable text, not a link
            {'text': 'https://matscout.prfo.design/mcp/http/', 'label': {'en': 'MCP endpoint', 'ru': 'MCP-эндпоинт'}},
        ],
        'desk': [('result', 'Result', 'Результат'), ('trace', 'Agent steps', 'Шаги агента'), ('table', 'Table', 'Таблица'),
                 ('diagram', 'Diagram', 'Диаграмма'), ('structure-3d', '3D', '3D')],
        'mob': [('result', 'Result', 'Результат'), ('structure-3d', '3D', '3D')],
    },
]
# phones show the same captures as desktop (Lev, 2026-09-29): no separate phone set
for _p in PROJECTS:
    _p['mob'] = []


# ---------- dictionary ----------
D = {'en': {}, 'ru': {}}
for L in ('en', 'ru'):
    s = SITE[L]; d = D[L]
    d['name'] = s['name']; d['role'] = s['role']; d['line'] = s['line']; d['cta'] = s['cta']
    d['title'] = s['name'] + ' | ' + s['role']
    for i, (a, b) in enumerate(s['do'], 1):
        d[f'do{i}.h'] = md(a); d[f'do{i}.t'] = md(b)
    d['contacts.tg'] = s['tg']; d['contacts.mail'] = s['mail']; d['contacts.gh'] = s['gh']
    d['a11y.close'] = s['close']; d['a11y.prev'] = s['prev']; d['a11y.next'] = s['next']
    for p in PROJECTS:
        k = 'p' + p['n']
        d[k + '.title'] = p.get('title_ru', p['title']) if L == 'ru' else p['title']
        d[k + '.kind'] = p['kind'][L]
        d[k + '.result'] = md(p['result'][L])
        for i, f in enumerate(p['facts'][L], 1):
            d[f'{k}.fact{i}'] = md(f)
        if 'data' in p:
            d[k + '.data'] = p['data'][L]
        for i, ln in enumerate(p['links'], 1):
            d[f'{k}.link{i}'] = ln['label'][L]
        # scene modes: segment labels, checked below against the content.md "Scene modes" block
        for set_key in ('desk', 'mob'):
            for i, (_, en_label, ru_label, *_f) in enumerate(p[set_key], 1):
                label = en_label if L == 'en' else ru_label
                d[f'{k}.mode.{set_key[0]}{i}'] = label
                d[f'{k}.alt.{set_key[0]}{i}'] = f"{p['title']}: {label}"

# ---------- markup helpers ----------
def e(s):
    return html.escape(s, quote=True)

ICON = {
    'left': 'M15 6l-6 6 6 6', 'right': 'M9 6l6 6-6 6', 'up': 'M6 15l6-6 6 6', 'down': 'M6 9l6 6 6-6',
    'fs': 'M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5', 'close': 'M6 6l12 12M18 6L6 18',
}
def svg(name, size, cls='ico'):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            f'<path d="{ICON[name]}"/></svg>')

en = D['en']
PRELOAD = []

def img_tags(p, set_key):
    k = 'p' + p['n']; out = []
    names = p[set_key]
    for i, (nm, _, _, *flags) in enumerate(names, 1):
        alt = en[f'{k}.alt.{set_key[0]}{i}']
        akey = f'{k}.alt.{set_key[0]}{i}'
        mkey = f'data-mode="{k}.mode.{set_key[0]}{i}"'
        first = (i == 1)
        cls = 'shot' + (' shot--bleed' if 'bleed' in flags else '') + (' is-on' if first else '')
        if set_key == 'desk':
            f12 = f"assets/img/{p['slug']}/{nm}-1200.webp"; f24 = f"assets/img/{p['slug']}/{nm}-2400.webp"
            if os.path.exists(os.path.join(ROOT, f24)):
                w, h = dims(os.path.join(ROOT, f24)); w12, _ = dims(os.path.join(ROOT, f12))
                srcset = f'{f12} {w12}w, {f24} {w}w'; big = f24
            else:
                w, h = dims(os.path.join(ROOT, f12)); srcset = f'{f12} {w}w'; big = f12
            sizes = '(min-width: 1200px) calc(100vw - 522px), 100vw'
            if first:
                # lazy for all: on phones the desktop stack is display:none and must not download.
                # The first frame of project 01 is preloaded from 600 px up in <head> (PRELOAD below).
                load = 'loading="lazy"'
                if p['n'] == '01':
                    PRELOAD.append(f'<link rel="preload" as="image" href="{f12}" imagesrcset="{srcset}" imagesizes="{sizes}" media="(min-width: 600px)" fetchpriority="high">')
                out.append(f'<img class="{cls}" src="{f12}" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{e(alt)}" data-i18n-alt="{akey}" {mkey} data-big="{big}" {load} decoding="async">')
            else:
                out.append(f'<img class="{cls}" data-src="{f12}" data-srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{e(alt)}" data-i18n-alt="{akey}" {mkey} data-big="{big}" decoding="async">')
        else:
            fm = f"assets/img/{p['slug']}/{nm}-m.webp"; big = fm
            if not os.path.exists(os.path.join(ROOT, fm)):
                # every frame in the phone stack needs its own phone capture; a cropped desktop capture is never shown
                sys.exit(f'missing phone capture {fm}: add it to tools/site-images.sh or drop the frame from mob')
            w, h = dims(os.path.join(ROOT, big))
            if first:
                out.append(f'<img class="{cls}" src="{fm}" width="{w}" height="{h}" alt="{e(alt)}" data-i18n-alt="{akey}" {mkey} data-big="{big}" loading="lazy" decoding="async">')
            else:
                out.append(f'<img class="{cls}" data-src="{fm}" width="{w}" height="{h}" alt="{e(alt)}" data-i18n-alt="{akey}" {mkey} data-big="{big}" decoding="async">')
    return '\n          '.join(out)

def project_html(p, idx):
    k = 'p' + p['n']; n = p['n']
    has_m = bool(p['mob'])
    nd = len(p['desk'])
    shape = 'portrait' if has_m else 'landscape'
    # box aspect follows the project's first desktop capture, so the box never changes size while switching
    f0 = os.path.join(ROOT, f"assets/img/{p['slug']}/{p['desk'][0][0]}-1200.webp")
    aw, ah = dims(f0)
    # labeled mode switch R-APP-16: radiogroup with a roving tabindex, arrows move and select
    seg = ''.join(
        # data-label: a hidden bold copy of the label reserves the checked width, so no segment moves on selection
        f'<button type="button" class="seg__btn" role="radio" aria-checked="{"true" if i == 1 else "false"}" tabindex="{"0" if i == 1 else "-1"}" data-i="{i-1}" data-i18n="{k}.mode.d{i}" data-label="{e(en[f"{k}.mode.d{i}"])}">{e(en[f"{k}.mode.d{i}"])}</button>'
        for i in range(1, nd + 1))
    facts = '\n          '.join(f'<li data-i18n="{k}.fact{i}">{en[f"{k}.fact{i}"]}</li>' for i in range(1, len(p['facts']['en']) + 1))
    meta = ''
    if 'data' in p:
        meta += f'\n        <p class="meta" data-i18n="{k}.data">{e(en[k + ".data"])}</p>'
    meta += f'\n        <p class="meta{" meta--solo" if "data" not in p else ""}">{e(p["stack"])}</p>'
    rows = []
    for i, ln in enumerate(p['links'], 1):
        wide = ' lrow--wide' if ln.get('wide') else ''
        if 'text' in ln:
            # plain text row: label, then the literal URL to select and copy
            cell = f'<p class="lplain"><span data-i18n="{k}.link{i}">{e(ln["label"]["en"])}</span> <code>{e(ln["text"])}</code></p>'
        else:
            cell = f'<a class="link" href="{e(ln["href"])}" target="_blank" rel="noopener" data-i18n="{k}.link{i}">{e(ln["label"]["en"])}</a>'
        rows.append(f'<div class="lrow{wide}">{cell}</div>')
    links_html = '\n          '.join(rows)
    count_m = len(p['mob']) if has_m else nd
    capsule = ''
    if count_m > 1:
        capsule = (f'<div class="capsule">'
                   f'<button type="button" class="capsule__btn" data-step="-1" aria-label="{e(en["a11y.prev"])}" data-i18n-aria="a11y.prev">{svg("left", 24)}</button>'
                   f'<span class="capsule__label" aria-live="polite">{e(en[f"{k}.mode.{"m" if has_m else "d"}1"])}</span>'
                   f'<button type="button" class="capsule__btn" data-step="1" aria-label="{e(en["a11y.next"])}" data-i18n-aria="a11y.next">{svg("right", 24)}</button>'
                   f'</div>')
    mstack = ''
    if has_m:
        mstack = f'''
          <span class="stack stack--m" data-set="m">
          {img_tags(p, 'mob')}
          </span>'''
    extra = ''
    if any('bleed' in t[3:] for t in p['desk']):
        extra += ' data-bleed'
    if p.get('mpos'):
        extra += f' data-mpos="{p["mpos"]}"'
    seg_html = f'<div class="seg" role="radiogroup" aria-label="{e(p["title"])}">{seg}</div>' if nd > 1 else ''
    return f'''
    <section class="project" data-theme="app" id="p-{n}" aria-labelledby="p-{n}-title" data-shape="{shape}"{extra}>
      <div class="phead">
        <div class="rail__head"><span class="badge badge--type" data-i18n="{k}.kind">{e(en[k + ".kind"])}</span><span class="badge badge--id">{n}</span></div>
        <h2 class="rail__title" id="p-{n}-title" data-i18n="{k}.title">{e(p["title"])}</h2>
        <p class="rail__result" data-i18n="{k}.result">{en[k + ".result"]}</p>
      </div>
      <div class="scene" style="--ar: {aw} / {ah}">
        <div class="scene__bar">
          <button type="button" class="fs" aria-haspopup="dialog" aria-label="{e(en[f"{k}.alt.d1"])}">{svg("fs", 24)}</button>
          {seg_html}
        </div>
        <div class="scene__box">
          <button type="button" class="scene__open" aria-haspopup="dialog" aria-label="{e(en[f"{k}.alt.d1"])}">
          <span class="stack stack--d" data-set="d">
          {img_tags(p, 'desk')}
          </span>{mstack}
          </button>
        </div>
        {capsule}
      </div>
      <div class="pbody">
        <ul class="facts">
          {facts}
        </ul>{meta}
        <div class="links">
          {links_html}
        </div>
      </div>
    </section>'''


do_items = '\n          '.join(
    f'<li><strong data-i18n="do{i}.h">{en[f"do{i}.h"]}</strong><span data-i18n="do{i}.t">{en[f"do{i}.t"]}</span></li>' for i in (1, 2, 3))

projects_html = ''.join(project_html(p, i) for i, p in enumerate(PROJECTS))

HEAD_SCRIPT = ("(function(){var d=document.documentElement,l=null;try{l=new URLSearchParams(location.search).get('lang');"
               "if(l!=='ru'&&l!=='en'){l=localStorage.getItem('lang')}}catch(x){}"
               "if(l!=='ru'&&l!=='en'){l=/^ru\\b/i.test(navigator.language||'')?'ru':'en'}"
               "d.lang=l;d.classList.add('js');if(l==='ru'){d.classList.add('i18n-wait');"
               "setTimeout(function(){d.classList.remove('i18n-wait')},2000)}})();")

URL = 'https://lab.prfo.design/portfolio/'

page = f'''<!doctype html>
<html lang="en" data-theme="landing-dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(en["title"])}</title>
<meta name="description" content="{e(en["line"])}">
<meta name="theme-color" content="#161616">
<link rel="canonical" href="{URL}">
<link rel="alternate" hreflang="en" href="{URL}?lang=en">
<link rel="alternate" hreflang="ru" href="{URL}?lang=ru">
<link rel="alternate" hreflang="x-default" href="{URL}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="{e(en["title"])}">
<meta property="og:description" content="{e(en["line"])}">
<meta property="og:image" content="{URL}assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(en["title"])}">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="ru_RU">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/nunito-sans-latin.woff2" as="font" type="font/woff2" crossorigin>
{chr(10).join(PRELOAD)}
<link rel="stylesheet" href="assets/css/tokens.css">
<link rel="stylesheet" href="assets/css/page.css">
<script>{HEAD_SCRIPT}</script>
<script src="assets/js/i18n.js" defer></script>
<script src="assets/js/page.js" defer></script>
</head>
<body>
<header class="hdr">
  <div class="container hdr__row">
    <a class="wordmark" href="#top" data-i18n="name">{e(en["name"])}</a>
    <div class="hdr__right">
      <div class="lang" role="group" aria-label="EN / RU">
        <button type="button" class="lang__btn" lang="en" data-lang="en" aria-pressed="true"><span>EN</span></button>
        <button type="button" class="lang__btn" lang="ru" data-lang="ru" aria-pressed="false"><span>RU</span></button>
      </div>
      <a class="btn-tg" href="https://t.me/prfowax" target="_blank" rel="noopener" data-i18n="cta">{e(en["cta"])}</a>
    </div>
  </div>
</header>
<main id="top">
  <section class="intro">
    <div class="container">
      <p class="eyebrow" data-i18n="role">{e(en["role"])}</p>
      <h1 class="display" data-i18n="name">{e(en["name"])}</h1>
      <p class="lead" data-i18n="line">{e(en["line"])}</p>
      <div class="sep" aria-hidden="true"></div>
      <ul class="do">
          {do_items}
      </ul>
    </div>
  </section>
  <div class="projects">{projects_html}
  </div>
  <section class="stackline">
    <div class="container">
      <p>{e(STACK_ALL)}</p>
    </div>
  </section>
</main>
<footer class="foot">
  <div class="container">
    <ul class="foot__links">
      <li><a class="foot__link" href="https://t.me/prfowax" target="_blank" rel="noopener" data-i18n="contacts.tg">{e(en["contacts.tg"])}</a></li>
      <li><a class="foot__link" href="mailto:levsk@icloud.com" data-i18n="contacts.mail">{e(en["contacts.mail"])}</a></li>
      <li><a class="foot__link" href="https://github.com/shorokhlev-sketch" target="_blank" rel="noopener" data-i18n="contacts.gh">{e(en["contacts.gh"])}</a></li>
    </ul>
  </div>
  <div class="mbar">
    <a class="mbar__btn" href="https://t.me/prfowax" target="_blank" rel="noopener" data-i18n="cta">{e(en["cta"])}</a>
  </div>
</footer>
<dialog class="viewer" data-theme="app">
  <div class="viewer__scroll"><img class="viewer__img" alt=""></div>
  <p class="viewer__meta" aria-live="polite"><span class="viewer__label"></span><span class="viewer__pos"></span></p>
  <button type="button" class="viewer__nav viewer__nav--prev" data-step="-1" aria-label="{e(en["a11y.prev"])}" data-i18n-aria="a11y.prev">{svg("left", 24)}</button>
  <button type="button" class="viewer__nav viewer__nav--next" data-step="1" aria-label="{e(en["a11y.next"])}" data-i18n-aria="a11y.next">{svg("right", 24)}</button>
  <button type="button" class="viewer__close" aria-label="{e(en["a11y.close"])}" data-i18n-aria="a11y.close">{svg("close", 21)}</button>
</dialog>
</body>
</html>
'''

# ---------- verification against content.md ----------
content = open('./content.md').read()
missing = []
for L in ('en', 'ru'):
    for key, val in D[L].items():
        # title is name | role, alt is project title: mode label, both built from checked parts;
        # the a11y labels are checked as whole lines below
        if key.startswith(('a11y.', 'title')) or '.alt.' in key:
            continue
        txt = re.sub(r'<[^>]+>', '', val)
        txt = html.unescape(txt)
        if txt not in content:
            missing.append((L, key, txt))
for p in PROJECTS:
    for ln in p['links']:
        if (ln.get('href') or ln.get('text')) not in content:
            missing.append(('url', p['n'], ln.get('href') or ln.get('text')))
    if p['stack'] not in content:
        missing.append(('stack', p['n'], p['stack']))
# field level checks: a short string can hide inside a longer one, so match whole lines
lines = set(content.splitlines())
for p in PROJECTS:
    for L in ('en', 'ru'):
        if '- Kind: ' + p['kind'][L] not in lines:
            missing.append((L, p['n'], 'Kind: ' + p['kind'][L]))
        if '- Result: ' + plain(p['result'][L]) not in lines:
            missing.append((L, p['n'], 'Result: ' + plain(p['result'][L])))
        for f in p['facts'][L]:
            if '  - ' + plain(f) not in lines:
                missing.append((L, p['n'], 'Fact: ' + plain(f)))
    if '- Stack: ' + p['stack'] not in lines:
        missing.append(('stack', p['n'], 'Stack: ' + p['stack']))
# scene modes: every label comes from the content.md "Scene modes" block, per project, in segment order.
# Block format, one heading line per project, then one line per language (the phone part only for a project with phone captures):
#   NN Title
#   - EN desktop: a, b, c | EN phone: a, b
#   - RU desktop: a, b, c | RU phone: a, b
mb = re.search(r'(?ms)^## Scene modes[^\n]*\n(.*?)(?=^## |^---|\Z)', content)
if not mb:
    missing.append(('modes', 'content.md has no "## Scene modes" block'))
else:
    labels = lambda s: [x.strip() for x in s.split(',')] if s else []
    rows = {}; cur = None
    for line in mb.group(1).splitlines():
        h = re.match(r'^(\d\d) (.+)$', line)
        if h:
            cur = h.group(1); rows[cur] = {'title': h.group(2).strip()}
            continue
        m = re.match(r'^- (EN|RU) desktop: (.+?)(?: \| \1 phone: (.+))?$', line)
        if m and cur:
            rows[cur][m.group(1).lower()] = {'desk': labels(m.group(2)), 'mob': labels(m.group(3))}
        elif line.startswith('- '):
            # a label line the checker cannot read would otherwise pass unchecked
            missing.append(('modes', cur, 'unreadable line', line))
    for n in rows:
        if n not in [p['n'] for p in PROJECTS]:
            missing.append(('modes', n, 'in the Scene modes block but not on the page'))
    for p in PROJECTS:
        row = rows.get(p['n'])
        if row is None:
            missing.append(('modes', p['n'], 'no entry in the Scene modes block'))
            continue
        if row['title'] != p['title']:
            missing.append(('modes', p['n'], 'title', p['title'], row['title']))
        for L, i in (('en', 1), ('ru', 2)):
            if L not in row:
                missing.append(('modes', p['n'], L, 'no desktop line'))
                continue
            for set_key in ('desk', 'mob'):
                have = [t[i] for t in p[set_key]]
                if have != row[L][set_key]:
                    missing.append(('modes', p['n'], L, set_key, have, row[L][set_key]))
# project order and numbering follow the "### NN Title" headings
heads = re.findall(r'(?m)^### (\d\d) (.+)$', content)
if [(p['n'], p['title']) for p in PROJECTS] != heads:
    missing.append(('order', [(p['n'], p['title']) for p in PROJECTS], heads))
# reverse check: every fact in content.md is on the page (a fact added to content.md fails the build until it is built in)
for m_ in re.finditer(r'(?ms)^### (\d\d) [^\n]*\n(.*?)(?=^### |^---|\Z)', content):
    pn = m_.group(1); body = m_.group(2)
    proj = next((p for p in PROJECTS if p['n'] == pn), None)
    if proj is None:
        continue
    for L, block in zip(('en', 'ru'), re.split(r'(?m)^RU$', body, maxsplit=1)):
        facts_md = re.findall(r'(?m)^  - (.+)$', block)
        on_page = [plain(f) for f in proj['facts'][L]]
        if facts_md != on_page:
            missing.append(('facts not on page', pn, L, [f for f in facts_md if f not in on_page]))
    # the stack line of each language: EN is the page stack, RU is the same list ('same as EN.')
    for L, block in zip(('en', 'ru'), re.split(r'(?m)^RU$', body, maxsplit=1)):
        md_stack = re.findall(r'(?m)^- Stack: (.+)$', block)
        if md_stack != [proj['stack']] and not (L == 'ru' and md_stack == ['same as EN.']):
            missing.append(('stack line', pn, L, md_stack, proj['stack']))
    # reverse check for links: the '- Links:' line of each language equals the page links, in order
    # (EN: label and URL per link, RU: labels only); a link added to content.md fails the build until it is built in
    for L, block in zip(('en', 'ru'), re.split(r'(?m)^RU$', body, maxsplit=1)):
        md_links = re.findall(r'(?m)^- Links: (.+)$', block)
        if L == 'en':
            want = ' | '.join(ln['label']['en'] + ' ' + (ln.get('href') or ln.get('text')) for ln in proj['links'])
        else:
            want = ' | '.join(ln['label']['ru'] for ln in proj['links'])
        if md_links != [want]:
            missing.append(('links differ from content.md', pn, L, md_links, want))
# stack block and contact URLs, whole lines
if STACK_ALL not in lines:
    missing.append(('stack block', STACK_ALL))
for url in ('https://t.me/prfowax', 'https://github.com/shorokhlev-sketch'):
    if url not in content:
        missing.append(('contact url', url))
for L in ('en', 'ru'):
    if '- Name: ' + SITE[L]['name'] not in lines:
        missing.append((L, 'Name: ' + SITE[L]['name']))
# names of the icon buttons (aria-label of previous, next, close), whole lines of a content.md "## Interface labels" block:
#   - EN: Previous, Next, Close
#   - RU: Назад, Далее, Закрыть
# Until content.md has that block the labels are not verified: they are printed as pending on every build (never skipped
# silently), and the build still writes. Once the block exists, a label that differs from it fails the build.
ib = re.search(r'(?ms)^## Interface labels[^\n]*\n(.*?)(?=^## |^---|\Z)', content)
a11y_rows = {L: '- ' + L.upper() + ': ' + ', '.join([SITE[L]['prev'], SITE[L]['next'], SITE[L]['close']]) for L in ('en', 'ru')}
pending = []
for L in ('en', 'ru'):
    if ib is None:
        pending.append(a11y_rows[L])
    elif a11y_rows[L] not in ib.group(1).splitlines():
        missing.append(('a11y', L, a11y_rows[L]))
# every scene image named in PROJECTS exists (desktop 1200 for every desk frame, -m for every phone frame)
for p in PROJECTS:
    for t in p['desk']:
        if not os.path.exists(f"{IMG}/{p['slug']}/{t[0]}-1200.webp"):
            missing.append(('image', p['n'], t[0] + '-1200.webp'))
print('NOT FOUND IN content.md:', missing if missing else 'none')
if pending:
    print('PENDING, not in content.md yet (no "## Interface labels" block), icon button names:', ' | '.join(r[2:] for r in pending))
i18n_js = '/* One dictionary for EN and RU. Keys are shared. Strings come from content.md. */\n' + 'window.I18N = ' + json.dumps(D, ensure_ascii=False, indent=1) + ';\n'
bad = [c for c in page + i18n_js if c in '\u2013\u2014']
print('dashes:', len(bad))
# a string that is not in content.md, or a dash, fails the build, and nothing is written: the last good build stays on disk
if missing or bad:
    sys.exit(1)

with open(ROOT + '/index.html', 'w') as f:
    f.write(page)

meta = {'en': {'title': D['en']['title'], 'desc': D['en']['line']}, 'ru': {'title': D['ru']['title'], 'desc': D['ru']['line']}}
with open(ROOT + '/assets/js/i18n.js', 'w') as f:
    f.write(i18n_js)

