/**
 * UniSearch - Categories Page
 */
(function () {
    'use strict';

    // ===== Theme Toggle =====
    const themeToggle = document.getElementById('themeToggle');
    const savedTheme = localStorage.getItem('unisearch-theme') || 'dark';
    if (savedTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
    }

    themeToggle.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'light' ? 'dark' : 'light';
        if (next === 'light') {
            document.documentElement.setAttribute('data-theme', 'light');
        } else {
            document.documentElement.removeAttribute('data-theme');
        }
        localStorage.setItem('unisearch-theme', next);
    });

    // ===== Mobile Menu =====
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const nav = document.querySelector('.nav');
    mobileMenuBtn.addEventListener('click', () => nav.classList.toggle('open'));
    nav.addEventListener('click', (e) => {
        if (e.target.classList.contains('nav-link')) nav.classList.remove('open');
    });

    // ===== Load Categories =====
    const grid = document.getElementById('categoriesGrid');

    async function loadCategories() {
        try {
            const resp = await fetch('data/symbols.json');
            const data = await resp.json();
            const categories = data.categories;

            const frag = document.createDocumentFragment();
            categories.forEach(cat => {
                const card = document.createElement('a');
                card.className = 'category-card';
                card.href = `index.html?category=${encodeURIComponent(cat.id)}`;
                card.innerHTML = `
                    <span class="category-card-icon">${cat.icon}</span>
                    <div class="category-card-name">${cat.name}</div>
                    <div class="category-card-count">${cat.symbols.length} symbol${cat.symbols.length !== 1 ? 's' : ''}</div>
                `;
                frag.appendChild(card);
            });
            grid.appendChild(frag);
        } catch (err) {
            console.error('Failed to load categories:', err);
            grid.innerHTML = '<p style="color: var(--text-muted); text-align: center; padding: 40px;">Failed to load categories. Please refresh.</p>';
        }
    }

    loadCategories();
})();
