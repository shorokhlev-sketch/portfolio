/* Portfolio: language switch, scene image switching, capsule, detail dialog. Vanilla, no build. */
(function () {
  'use strict';
  var doc = document.documentElement;
  var DICT = window.I18N || { en: {}, ru: {} };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var mqMobile = window.matchMedia('(max-width: 599px)');
  var lang = doc.lang === 'ru' ? 'ru' : 'en';
  var canon = document.querySelector('link[rel="canonical"]');
  var canonBase = canon ? canon.getAttribute('href').split('?')[0] : '';

  function t(key) { var d = DICT[lang] || {}; return d[key] != null ? d[key] : (DICT.en[key] || ''); }

  /* ---------- language ---------- */
  function applyLang(next, fromUser) {
    lang = next === 'ru' ? 'ru' : 'en';
    doc.lang = lang;
    document.title = t('title');
    var md = document.querySelector('meta[name="description"]');
    if (md) md.setAttribute('content', t('line'));
    document.querySelectorAll('[data-i18n]').forEach(function (el) { el.innerHTML = t(el.getAttribute('data-i18n')); });
    /* segments carry a hidden bold copy of their label (CSS ::after) that reserves the checked width */
    document.querySelectorAll('.seg__btn').forEach(function (el) { el.setAttribute('data-label', t(el.getAttribute('data-i18n'))); });
    document.querySelectorAll('[data-i18n-alt]').forEach(function (el) { el.alt = t(el.getAttribute('data-i18n-alt')); });
    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) { el.setAttribute('aria-label', t(el.getAttribute('data-i18n-aria'))); });
    document.querySelectorAll('.lang__btn').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-lang') === lang ? 'true' : 'false'); });
    scenes.forEach(function (s) { s.syncLabels(); s.fitCapsule(); s.fitSeg(); });
    if (fromUser) {
      try { localStorage.setItem('lang', lang); } catch (e) {}
      try {
        var u = new URL(location.href); u.searchParams.set('lang', lang);
        history.replaceState(null, '', u.pathname + u.search + u.hash);
      } catch (e) {}
    }
    /* canonical follows the explicit ?lang= URL, so it matches the hreflang alternates */
    if (canon) {
      var q = null;
      try { q = new URLSearchParams(location.search).get('lang'); } catch (e) {}
      canon.setAttribute('href', canonBase + (q === 'en' || q === 'ru' ? '?lang=' + q : ''));
    }
    doc.classList.remove('i18n-wait');
  }

  /* ---------- image loading ---------- */
  function load(img) {
    if (img.getAttribute('data-src')) {
      if (img.getAttribute('data-srcset')) { img.srcset = img.getAttribute('data-srcset'); img.removeAttribute('data-srcset'); }
      img.src = img.getAttribute('data-src'); img.removeAttribute('data-src');
    }
    return img;
  }
  function ready(img) {
    load(img);
    if (img.complete && img.naturalWidth) return Promise.resolve();
    if (img.decode) return img.decode().catch(function () {});
    return new Promise(function (r) { img.onload = img.onerror = r; });
  }
  function prefetch(img) {
    var src = img.getAttribute('data-src');
    if (!src) return;
    var pre = new Image();
    if (img.getAttribute('data-srcset')) { pre.sizes = img.sizes; pre.srcset = img.getAttribute('data-srcset'); }
    pre.src = src;
  }

  /* ---------- scenes ---------- */
  function Scene(section) {
    var self = this;
    this.el = section;
    this.stacks = {};
    section.querySelectorAll('.stack').forEach(function (st) {
      self.stacks[st.getAttribute('data-set')] = { imgs: Array.prototype.slice.call(st.querySelectorAll('.shot')), i: 0 };
    });
    this.segs = Array.prototype.slice.call(section.querySelectorAll('.seg__btn'));
    this.open = section.querySelector('.scene__open');
    this.label = section.querySelector('.capsule__label');
    this.fs = section.querySelector('.fs');

    this.segs.forEach(function (b, i) {
      b.addEventListener('click', function () { self.show('d', i); });
      b.addEventListener('keydown', function (ev) {
        var n = self.segs.length, j = null;
        if (ev.key === 'ArrowRight') j = (i + 1) % n;
        else if (ev.key === 'ArrowLeft') j = (i - 1 + n) % n;
        else if (ev.key === 'ArrowDown') j = (i + 1) % n;
        else if (ev.key === 'ArrowUp') j = (i - 1 + n) % n;
        else if (ev.key === 'Home') j = 0;
        else if (ev.key === 'End') j = n - 1;
        if (j !== null) { ev.preventDefault(); self.show('d', j); self.segs[j].focus(); }
      });
    });
    var seg = this.seg = section.querySelector('.seg');
    if (seg) {
      seg.addEventListener('pointerenter', function () {
        var st = self.stacks.d; prefetch(st.imgs[(st.i + 1) % st.imgs.length]);
      });
      seg.addEventListener('scroll', function () { self.fadeSeg(); }, { passive: true });
    }
    section.querySelectorAll('.capsule__btn').forEach(function (b) {
      b.addEventListener('click', function () {
        var key = self.activeSet(), st = self.stacks[key], n = st.imgs.length;
        self.show(key, (st.i + Number(b.getAttribute('data-step')) + n) % n);
      });
    });
    [this.open, this.fs].forEach(function (b) {
      if (b) b.addEventListener('click', function () { viewer.show(self, b); });
    });
    this.fitCapsule();
  }
  Scene.prototype.activeSet = function () {
    return (mqMobile.matches && this.stacks.m && this.el.getAttribute('data-shape') === 'portrait') ? 'm' : 'd';
  };
  Scene.prototype.current = function () { var st = this.stacks[this.activeSet()]; return st.imgs[st.i]; };
  Scene.prototype.show = function (key, i) {
    var st = this.stacks[key];
    if (!st || i === st.i) return;
    var next = st.imgs[i];
    st.i = i;
    if (key === 'd') {
      this.segs.forEach(function (b, j) {
        b.setAttribute('aria-checked', j === i ? 'true' : 'false');
        b.tabIndex = j === i ? 0 : -1;
      });
      this.revealSeg(i);
    }
    this.syncLabels();
    ready(next).then(function () {
      if (st.imgs[st.i] !== next) return;
      st.imgs.forEach(function (im) { im.classList.remove('is-top'); });
      next.classList.add('is-top', 'is-on');
      setTimeout(function () {
        if (st.imgs[st.i] !== next) return;
        st.imgs.forEach(function (im) { if (im !== next) im.classList.remove('is-on'); });
      }, reduce.matches ? 250 : 600);
    });
    var after = st.imgs[(i + 1) % st.imgs.length];
    if (after) prefetch(after);
  };
  Scene.prototype.syncLabels = function () {
    var img = this.current();
    if (!img) return;
    if (this.open) this.open.setAttribute('aria-label', img.alt);
    if (this.fs) this.fs.setAttribute('aria-label', img.alt);
    if (this.label) this.label.textContent = t(img.getAttribute('data-mode'));
  };
  /* a segment set wider than its scene scrolls sideways; the fade marks the side with more segments */
  Scene.prototype.fitSeg = function () {
    var seg = this.seg;
    if (!seg) return;
    seg.classList.remove('is-scroll');
    seg.scrollLeft = 0;
    if (seg.scrollWidth > seg.clientWidth + 1) { seg.classList.add('is-scroll'); this.revealSeg(this.stacks.d.i, true); }
    this.fadeSeg();
  };
  Scene.prototype.fadeSeg = function () {
    var seg = this.seg;
    if (!seg) return;
    if (!seg.classList.contains('is-scroll')) { seg.removeAttribute('data-more'); return; }
    var m = (seg.scrollLeft > 1 ? 'l' : '') + (seg.scrollLeft + seg.clientWidth < seg.scrollWidth - 1 ? 'r' : '');
    if (m) seg.setAttribute('data-more', m); else seg.removeAttribute('data-more');
  };
  /* the checked segment is always fully visible, clear of the fade */
  Scene.prototype.revealSeg = function (i, instant) {
    var seg = this.seg, b = this.segs[i];
    if (!seg || !b || !seg.classList.contains('is-scroll')) return;
    var sr = seg.getBoundingClientRect(), br = b.getBoundingClientRect(), pad = 40, x = seg.scrollLeft;
    if (br.left < sr.left + pad) x += br.left - sr.left - (i === 0 ? pad * 2 : pad);
    else if (br.right > sr.right - pad) x += br.right - sr.right + (i === this.segs.length - 1 ? pad * 2 : pad);
    else return;
    if (instant || reduce.matches || !seg.scrollTo) seg.scrollLeft = x; else seg.scrollTo({ left: x, behavior: 'smooth' });
  };
  /* the capsule keeps the width of its widest label for this project and language, so the arrows never move under the thumb */
  Scene.prototype.fitCapsule = function () {
    if (!this.label) return;
    var st = this.stacks[this.activeSet()], lab = this.label, cur = lab.textContent, w = 0;
    lab.style.minWidth = '';
    st.imgs.forEach(function (im) { lab.textContent = t(im.getAttribute('data-mode')); w = Math.max(w, lab.scrollWidth); });
    lab.textContent = cur;
    lab.style.minWidth = w + 'px';
  };

  /* ---------- detail dialog ---------- */
  /* Pages through the captures of the scene that opened it, in the set that matches the viewport (desktop from 600 px,
     phone below). Closing leaves the scene on the last capture viewed and returns focus to the opener. */
  var viewer = (function () {
    var dlg = document.querySelector('.viewer');
    if (!dlg || typeof dlg.showModal !== 'function') return { show: function () {} };
    var img = dlg.querySelector('.viewer__img'), scroller = dlg.querySelector('.viewer__scroll'), close = dlg.querySelector('.viewer__close');
    var labelEl = dlg.querySelector('.viewer__label'), posEl = dlg.querySelector('.viewer__pos');
    var navs = Array.prototype.slice.call(dlg.querySelectorAll('.viewer__nav'));
    var returnTo = null, timer = null, scene = null, key = 'd', list = [], idx = 0, swipedAt = 0;
    function big(el) { return el.getAttribute('data-big') || el.currentSrc || el.src; }
    function preload(el) { if (el) { var p = new Image(); p.src = big(el); } }
    function center() {
      scroller.scrollTop = 0; scroller.scrollLeft = Math.max(0, (scroller.scrollWidth - scroller.clientWidth) / 2);
      dlg.classList.toggle('is-pannable', scroller.scrollWidth > scroller.clientWidth + 1);
    }
    function meta() {
      var el = list[idx];
      labelEl.textContent = t(el.getAttribute('data-mode'));
      posEl.textContent = (idx + 1) + ' / ' + list.length;
      img.alt = el.alt;
      dlg.setAttribute('aria-label', el.alt);
    }
    function render(dir) {
      var el = list[idx], src = big(el);
      meta();
      var shown = function () {
        center();
        if (dir && !reduce.matches && img.animate) {
          img.animate([{ opacity: 0, transform: 'translateX(' + (dir * 24) + 'px)' }, { opacity: 1, transform: 'none' }],
            { duration: 250, easing: 'cubic-bezier(.4,0,.2,1)' });
        }
      };
      if (img.getAttribute('src') !== src) {
        img.src = src;
        if (img.complete && img.naturalWidth) shown(); else img.addEventListener('load', shown, { once: true });
      } else shown();
      /* the neighbours load while this one is looked at */
      if (list.length > 1) { preload(list[(idx + 1) % list.length]); preload(list[(idx - 1 + list.length) % list.length]); }
    }
    function step(d) {
      if (list.length < 2) return;
      idx = (idx + d + list.length) % list.length;
      render(d);
    }
    function hide() {
      /* the scene behind switches while the viewer fades, so it is already on the last capture viewed when it shows */
      if (scene) scene.show(key, idx);
      dlg.classList.remove('is-open');
      clearTimeout(timer);
      timer = setTimeout(function () { if (dlg.open) dlg.close(); }, reduce.matches ? 0 : 300);
    }
    dlg.addEventListener('cancel', function (ev) { ev.preventDefault(); hide(); });
    dlg.addEventListener('close', function () {
      img.removeAttribute('src');
      /* the scene behind shows the last capture viewed, its switch follows (again here for a close that skipped hide) */
      if (scene) scene.show(key, idx);
      if (returnTo) returnTo.focus();
    });
    close.addEventListener('click', hide);
    navs.forEach(function (b) { b.addEventListener('click', function () { step(Number(b.getAttribute('data-step'))); }); });
    scroller.addEventListener('click', function (ev) { if (ev.target !== img && Date.now() - swipedAt > 400) hide(); });
    dlg.addEventListener('keydown', function (ev) {
      if (ev.key === 'ArrowLeft' || ev.key === 'ArrowRight') {
        ev.preventDefault(); step(ev.key === 'ArrowRight' ? 1 : -1);
      } else if (ev.key === 'Tab') {
        /* focus stays inside the dialog */
        var f = Array.prototype.slice.call(dlg.querySelectorAll('button, [tabindex]')).filter(function (el) {
          return !el.hidden && el.tabIndex >= 0 && el.offsetParent !== null;
        });
        if (!f.length) return;
        var at = f.indexOf(document.activeElement);
        ev.preventDefault();
        f[ev.shiftKey ? (at <= 0 ? f.length - 1 : at - 1) : (at === -1 || at === f.length - 1 ? 0 : at + 1)].focus();
      }
    });
    /* swipe: a mostly horizontal move past the threshold pages; a capture that pans sideways pages only from its edge */
    var sx = 0, sy = 0, sl = 0, track = false;
    scroller.addEventListener('touchstart', function (ev) {
      track = ev.touches.length === 1;
      if (!track) return;
      sx = ev.touches[0].clientX; sy = ev.touches[0].clientY; sl = scroller.scrollLeft;
    }, { passive: true });
    scroller.addEventListener('touchend', function (ev) {
      if (!track) return;
      track = false;
      var tch = ev.changedTouches[0], dx = tch.clientX - sx, dy = tch.clientY - sy;
      if (Math.abs(dx) < 50 || Math.abs(dx) < Math.abs(dy) * 1.5) return;
      var max = scroller.scrollWidth - scroller.clientWidth;
      if (max > 1) {
        if (dx < 0 && sl < max - 1) return;
        if (dx > 0 && sl > 1) return;
      }
      swipedAt = Date.now();
      step(dx < 0 ? 1 : -1);
    }, { passive: true });
    return {
      show: function (sc, from) {
        scene = sc; key = sc.activeSet();
        var st = sc.stacks[key];
        if (!st || !st.imgs.length) return;
        list = st.imgs; idx = st.i;
        returnTo = from;
        clearTimeout(timer);
        var paged = list.length > 1;
        dlg.classList.toggle('is-paged', paged);
        dlg.setAttribute('data-set', key);
        navs.forEach(function (b) { b.hidden = !paged; });
        posEl.hidden = !paged;
        img.removeAttribute('src');
        dlg.showModal();
        /* the label and "n / N" keep the width of their widest text in this list, so the pill holds still while paging */
        var wl = 0, wp = 0;
        labelEl.style.minWidth = ''; posEl.style.minWidth = '';
        list.forEach(function (el, i) {
          labelEl.textContent = t(el.getAttribute('data-mode')); wl = Math.max(wl, labelEl.getBoundingClientRect().width);
          posEl.textContent = (i + 1) + ' / ' + list.length; wp = Math.max(wp, posEl.getBoundingClientRect().width);
        });
        labelEl.style.minWidth = Math.ceil(wl) + 'px'; posEl.style.minWidth = Math.ceil(wp) + 'px';
        render(0);
        close.focus();
        requestAnimationFrame(function () { dlg.classList.add('is-open'); });
      }
    };
  })();

  var sections = Array.prototype.slice.call(document.querySelectorAll('.project'));

  /* ---------- init ---------- */
  var scenes = sections.map(function (s) { return new Scene(s); });
  document.querySelectorAll('.lang__btn').forEach(function (b) {
    b.addEventListener('click', function () { if (b.getAttribute('data-lang') !== lang) applyLang(b.getAttribute('data-lang'), true); });
  });
  applyLang(lang, false);
  var onMq = function () { scenes.forEach(function (s) { s.syncLabels(); s.fitCapsule(); }); };
  if (mqMobile.addEventListener) mqMobile.addEventListener('change', onMq);
  /* labels measured with a fallback font are re-measured once the page fonts are in */
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { scenes.forEach(function (s) { s.fitCapsule(); s.fitSeg(); }); });
  var rz = null;
  window.addEventListener('resize', function () { clearTimeout(rz); rz = setTimeout(function () { scenes.forEach(function (s) { s.fitSeg(); }); }, 100); });
})();
