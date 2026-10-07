document.body.classList.remove('no-js');
var yEl = document.getElementById('y');
if (yEl) yEl.textContent = new Date().getFullYear();

// theme toggle (light by default, remembered per visitor)
var root = document.documentElement;
function setTheme(t) {
  if (t === 'dark') root.setAttribute('data-theme', 'dark'); else root.removeAttribute('data-theme');
  try { localStorage.setItem('meetek-theme', t); } catch (e) {}
}
document.querySelectorAll('.theme').forEach(function (b) {
  b.addEventListener('click', function () {
    setTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
  });
});

// reveal on scroll
var els = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) { io.observe(el); });
} else {
  els.forEach(function (el) { el.classList.add('in'); });
}
