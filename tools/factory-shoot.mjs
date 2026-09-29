// Content Factory recapture from the live demo (session e6dadf4a). Read only: every non GET request except
// POST /api/load_session is aborted. Names of the show in GPT text, hooks and subtitle lines are blurred by capture-only CSS.
// Run: node tools/factory-shoot.mjs [name filter], with playwright-core resolvable (NODE_PATH or a local install); writes shots/factory/*.png.
import { chromium } from 'playwright-core';
const OUT = process.env.OUT || './shots/factory/';
const URL = 'https://factory.prfo.design/?session=e6dadf4a';
const only = process.argv[2] || 'all';
const b = await chromium.launch();
const NAMES = 'Саш|Сань|Тан|ТНТ|TNT';

async function open(vp) {
  const ctx = await b.newContext(vp.mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
  const p = await ctx.newPage();
  await p.route('**/*', r => {
    const q = r.request();
    if (q.method() !== 'GET' && !(q.method() === 'POST' && q.url().includes('/api/load_session/'))) return r.abort();
    return r.continue();
  });
  await p.goto(URL, { waitUntil: 'networkidle' });
  await p.waitForSelector('.scene-desc');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  return { ctx, p };
}
async function blur(p) {
  await p.evaluate((re) => {
    const rx = new RegExp(re, 'i');
    document.querySelectorAll('.scene-desc, .scene-why, .hook, .sub-line, .codeblock, .transcript, .toast').forEach(el => {
      const txt = el.textContent + ' ' + [...el.querySelectorAll('input')].map(i => i.value).join(' ');
      if (rx.test(txt)) { el.style.filter = 'blur(5px)'; el.dataset.capBlur = '1'; }
    });
  }, NAMES);
}
async function addClips(p) {
  await p.evaluate(() => {
    const hooks = Object.fromEntries(scenes.map(s => [s.id, s.hook]));
    for (const id of [2, 3]) {
      const fn = `clip_${String(id).padStart(2, '0')}_shorts.mp4`;
      addClip({ type: 'clip_done', clip_id: id, filename: fn, hook: hooks[id], url: `/api/clips/${jobId}/${fn}` });
    }
    unlockStep(4); showStep(4);
  });
  // pause each clip on a frame whose burned subtitle names nobody
  const at = { 'clip_02_shorts.mp4': 26.0, 'clip_03_shorts.mp4': 19.0 };
  await p.evaluate(async (at) => {
    for (const card of document.querySelectorAll('.clip-card')) {
      const v = card.querySelector('video');
      v.muted = true; v.removeAttribute('controls');
      await new Promise(r => { if (v.readyState >= 1) r(); else v.addEventListener('loadedmetadata', r, { once: true }); });
      v.currentTime = at[card.dataset.filename];
      await new Promise(r => v.addEventListener('seeked', r, { once: true }));
    }
  }, at);
  await p.waitForTimeout(600);
}
async function shot(p, name) {
  // phone: the step bar scrolls sideways; it stays at its start unless the current step is cut, then it goes to its end
  await p.evaluate(() => { const st = document.querySelector('#stepper'), c = st.querySelector('.step.current'); st.scrollLeft = c.offsetLeft + c.offsetWidth > st.clientWidth ? st.scrollWidth : 0; });
  await blur(p); await p.waitForTimeout(200); await p.screenshot({ path: OUT + name + '.png' }); console.log('saved', name); }

const jobs = {
  'desktop-02-scenes': async (p) => { await shot(p, 'desktop-02-scenes'); },
  'desktop-03-subtitles': async (p) => {
    await p.evaluate(() => { toggleSubtitles(2); });
    await p.evaluate(() => { const c = document.getElementById('scene-2'); const top = document.querySelector('#stepper').getBoundingClientRect().bottom; window.scrollTo(0, c.getBoundingClientRect().top + scrollY - top - 6); });
    await p.waitForTimeout(500);
    await shot(p, 'desktop-03-subtitles');
  },
  'desktop-07-clips': async (p) => { await addClips(p); await p.evaluate(() => window.scrollTo(0, 0)); await shot(p, 'desktop-07-clips'); },
  'desktop-09-trim': async (p) => {
    await addClips(p);
    const card = p.locator('.clip-card').nth(1);
    await card.locator('.btn-toggle-trim').click();
    await p.evaluate(() => { const c = document.querySelectorAll('.clip-card')[1]; const top = document.querySelector('#stepper').getBoundingClientRect().bottom; window.scrollTo(0, c.getBoundingClientRect().top + scrollY - top - 6); });
    await p.waitForTimeout(600);
    const h = card.locator('.trim-handle-start'); const tr = card.locator('.trim-track');
    const hb = await h.boundingBox(), tb = await tr.boundingBox();
    await p.mouse.move(hb.x + hb.width / 2, hb.y + hb.height / 2); await p.mouse.down();
    await p.mouse.move(tb.x + tb.width * 0.2, hb.y + hb.height / 2, { steps: 8 });
    await p.waitForTimeout(1500);
    await p.evaluate(async () => { const v = document.querySelectorAll('.clip-card')[1].querySelector('video'); v.currentTime = 19.0; await new Promise(r => v.addEventListener('seeked', r, { once: true })); });
    await p.waitForTimeout(600);
    await shot(p, 'desktop-09-trim');
    await p.mouse.up();
  },
  'mobile-02-scenes': async (p) => { await shot(p, 'mobile-02-scenes'); },
  'mobile-03-subtitles': async (p) => {
    await p.evaluate(() => { toggleSubtitles(2); });
    await p.evaluate(() => { const c = document.getElementById('scene-2'); const top = document.querySelector('#stepper').getBoundingClientRect().bottom; window.scrollTo(0, c.getBoundingClientRect().top + scrollY - top - 6); });
    await p.waitForTimeout(500);
    await shot(p, 'mobile-03-subtitles');
  },
  'mobile-07-clips': async (p) => { await addClips(p); await p.evaluate(() => window.scrollTo(0, 0)); await shot(p, 'mobile-07-clips'); },
};
import fs from 'fs'; fs.mkdirSync(OUT, { recursive: true });
for (const [name, fn] of Object.entries(jobs)) {
  if (only !== 'all' && !name.includes(only)) continue;
  const { ctx, p } = await open({ mobile: name.startsWith('mobile') });
  await fn(p);
  await ctx.close();
}
await b.close();
