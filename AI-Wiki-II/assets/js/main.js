// ============================================================
// AI Wiki — interactive behaviors
// ============================================================

// Theme toggle
(function () {
  const saved = localStorage.getItem('ai-wiki-theme');
  if (saved) document.documentElement.setAttribute('data-theme', saved);

  document.addEventListener('click', (e) => {
    const btn = e.target.closest('#theme-toggle');
    if (!btn) return;
    const cur = document.documentElement.getAttribute('data-theme') || 'dark';
    const next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('ai-wiki-theme', next);
  });
})();

// Sidebar toggle (mobile)
(function () {
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('#sidebar-toggle');
    if (!btn) return;
    document.querySelector('.sidebar')?.classList.toggle('open');
  });
})();

// Mark current nav item active based on page
(function () {
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-item a').forEach(a => {
    const href = a.getAttribute('href').split('/').pop();
    if (href === path) a.classList.add('active');
  });
})();

// KaTeX render-all pass
document.addEventListener('DOMContentLoaded', () => {
  if (window.renderMathInElement) {
    renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false },
        { left: '\\[', right: '\\]', display: true },
        { left: '\\(', right: '\\)', display: false }
      ],
      throwOnError: false
    });
  }
});
