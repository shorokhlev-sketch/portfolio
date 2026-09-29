import { chromium } from 'playwright';
const BASE = 'http://localhost:8791/';
const OUT = './_review-site/';
const only = process.argv[2] || 'all';
const browser = await chromium.launch();
const report = {};

async function scrollAll(page) {
  await page.evaluate(async () => {
    const h = () => document.documentElement.scrollHeight;
    for (let y = 0; y < h(); y += 400) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
    window.scrollTo(0, h()); await new Promise(r => setTimeout(r, 400));
  });
  await page.waitForLoadState('networkidle');
  await page.evaluate(() => Promise.race([new Promise(r => setTimeout(r, 3000)), Promise.all([...document.images].filter(i => i.src && !i.complete && i.offsetParent).map(i => new Promise(r => { i.onload = i.onerror = r; })))]));
}

const runs = [
  { name: 'desktop', w: 1440, h: 900, mobile: false },
  { name: 'mobile', w: 390, h: 844, mobile: true },
];
for (const r of runs) {
  if (only !== 'all' && only !== r.name) continue;
  for (const lang of ['en', 'ru']) {
    const ctx = await browser.newContext({ viewport: { width: r.w, height: r.h }, deviceScaleFactor: 1, isMobile: r.mobile, hasTouch: r.mobile });
    const page = await ctx.newPage();
    const errors = []; const external = [];
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    page.on('pageerror', e => errors.push(String(e)));
    page.on('request', q => { if (!q.url().startsWith(BASE)) external.push(q.url()); });
    await page.goto(BASE + (lang === 'ru' ? '?lang=ru' : ''), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    await page.screenshot({ path: `${OUT}${r.name}-${lang}-viewport.png` });
    const firstScene = await page.evaluate(() => { const s = document.querySelector('.project'); return s ? Math.round(s.getBoundingClientRect().top) : null; });
    await scrollAll(page);
    const weight = await page.evaluate(() => performance.getEntriesByType('resource').reduce((a, e) => a + (e.transferSize || e.encodedBodySize || 0), 0) + (performance.getEntriesByType('navigation')[0]?.transferSize || 0));
    const hscroll = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(200);
    await page.screenshot({ path: `${OUT}${r.name}-${lang}-full.png`, fullPage: true });
    report[`${r.name}-${lang}`] = { firstSceneTop: firstScene, weightKB: Math.round(weight / 1024), hscroll, errors, external, lang: await page.evaluate(() => document.documentElement.lang), title: await page.title() };
    await ctx.close();
  }
}
// share preview: the first screen at 1200 x 630, EN, rebuilt with the site (node site-shoot.mjs og)
if (only === 'all' || only === 'og') {
  const ctx = await browser.newContext({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  await page.goto(BASE + '?lang=en', { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  await page.screenshot({ path: './site/assets/img/og.jpg', type: 'jpeg', quality: 85 });
  await ctx.close();
}
console.log(JSON.stringify(report, null, 1));
await browser.close();
