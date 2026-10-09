document.body.classList.remove('no-js');
var root = document.documentElement;
var yEl = document.getElementById('y');
if (yEl) yEl.textContent = new Date().getFullYear();

// theme: dark by default, remembered per visitor, eased (no abrupt brightness jump)
document.querySelectorAll('.theme').forEach(function (b) {
  b.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    if (next === 'dark') root.setAttribute('data-theme', 'dark'); else root.removeAttribute('data-theme');
    try { localStorage.setItem('meetek-theme', next); } catch (e) {}
  });
});

// scroll-edge effect on the translucent nav
var nav = document.querySelector('.nav');
function onScroll() { nav.classList.toggle('scrolled', scrollY > 4); }
addEventListener('scroll', onScroll, { passive: true }); onScroll();

// before / after segmented control: responds on pointer-down, keyboard accessible
document.querySelectorAll('.seg').forEach(function (seg) {
  var tabs = Array.prototype.slice.call(seg.querySelectorAll('[role="tab"]'));
  function select(tab) {
    if (tab.getAttribute('aria-selected') === 'true') return;
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    seg.setAttribute('data-state', tab.dataset.state);
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('pointerdown', function (e) { if (e.button === 0) select(t); });
    t.addEventListener('click', function () { select(t); });
    t.addEventListener('keydown', function (e) {
      if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
      var forward = (e.key === 'ArrowRight') !== (root.dir === 'rtl');
      var n = tabs[(i + (forward ? 1 : -1) + tabs.length) % tabs.length];
      select(n); n.focus(); e.preventDefault();
    });
  });
});

// entrance reveal (transform + opacity only)
var els = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -6% 0px' });
  els.forEach(function (el) { io.observe(el); });
} else {
  els.forEach(function (el) { el.classList.add('in'); });
}
