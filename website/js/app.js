/**
 * UniSearch - Unicode Symbol Search Application
 * Client-side search with instant results
 */

(function () {
    'use strict';

    // ===== State =====
    let allSymbols = [];
    let categories = [];
    let activeCategory = 'all';
    let currentModal = null;
    let currentFiltered = [];
    let displayedCount = 0;
    const PAGE_SIZE = 200;

    // ===== DOM Elements =====
    const searchInput = document.getElementById('searchInput');
    const clearSearch = document.getElementById('clearSearch');
    const searchStats = document.getElementById('searchStats');
    const resultsGrid = document.getElementById('resultsGrid');
    const resultsTitle = document.getElementById('resultsTitle');
    const resultsCount = document.getElementById('resultsCount');
    const noResults = document.getElementById('noResults');
    const loading = document.getElementById('loading');
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toastMessage');
    const modalOverlay = document.getElementById('modalOverlay');
    const modal = document.getElementById('modal');
    const modalClose = document.getElementById('modalClose');
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const nav = document.querySelector('.nav');
    const themeToggle = document.getElementById('themeToggle');

    // ===== Theme Toggle =====
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

    // ===== URL Params =====
    function getCategoryFromURL() {
        const params = new URLSearchParams(window.location.search);
        return params.get('category') || 'all';
    }

    // ===== Init =====
    async function init() {
        try {
            const resp = await fetch('data/symbols.json');
            const data = await resp.json();
            categories = data.categories;

            // Flatten all symbols with category info
            allSymbols = [];
            categories.forEach(cat => {
                cat.symbols.forEach(sym => {
                    allSymbols.push({
                        ...sym,
                        categoryId: cat.id,
                        categoryName: cat.name
                    });
                });
            });

            // Check URL for category pre-selection
            activeCategory = getCategoryFromURL();
            if (activeCategory !== 'all') {
                const cat = categories.find(c => c.id === activeCategory);
                if (cat) {
                    resultsTitle.textContent = cat.name;
                } else {
                    activeCategory = 'all';
                }
            }

            performSearch();
            loading.style.display = 'none';
            searchStats.textContent = `${allSymbols.length} symbols available`;
        } catch (err) {
            console.error('Failed to load symbols:', err);
            loading.innerHTML = '<p style="color:#ff6b6b">Failed to load symbols. Please refresh.</p>';
        }
    }

    // ===== Render Symbol Cards (with pagination) =====
    function renderSymbols(symbols) {
        currentFiltered = symbols;
        displayedCount = 0;

        if (symbols.length === 0) {
            resultsGrid.innerHTML = '';
            noResults.style.display = 'block';
            resultsCount.textContent = '';
            removeLoadMore();
            return;
        }

        noResults.style.display = 'none';
        resultsCount.textContent = `${symbols.length} symbol${symbols.length !== 1 ? 's' : ''}`;

        resultsGrid.innerHTML = '';
        loadMore();
    }

    function loadMore() {
        const symbols = currentFiltered;
        const end = Math.min(displayedCount + PAGE_SIZE, symbols.length);
        const frag = document.createDocumentFragment();

        for (let i = displayedCount; i < end; i++) {
            const sym = symbols[i];
            const card = document.createElement('div');
            card.className = 'symbol-card';
            card.setAttribute('role', 'button');
            card.setAttribute('tabindex', '0');
            card.setAttribute('title', `${sym.name} - Click to copy`);
            card.innerHTML = `
                <span class="symbol-char">${sym.char}</span>
                <span class="symbol-name">${sym.name}</span>
                <span class="symbol-unicode">${sym.unicode}</span>
                <div class="copy-overlay">Click to copy</div>
            `;

            card.addEventListener('click', (e) => {
                e.stopPropagation();
                copyToClipboard(sym.char, `${sym.char} copied!`);
            });

            card.addEventListener('contextmenu', (e) => {
                e.preventDefault();
                openModal(sym);
            });

            card.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    copyToClipboard(sym.char, `${sym.char} copied!`);
                } else if (e.key === ' ') {
                    e.preventDefault();
                    openModal(sym);
                }
            });

            frag.appendChild(card);
        }

        resultsGrid.appendChild(frag);
        displayedCount = end;

        // Show/hide Load More button
        removeLoadMore();
        if (displayedCount < symbols.length) {
            const btn = document.createElement('button');
            btn.id = 'loadMoreBtn';
            btn.className = 'load-more-btn';
            btn.textContent = `Load More (${symbols.length - displayedCount} remaining)`;
            btn.addEventListener('click', loadMore);
            resultsGrid.parentNode.insertBefore(btn, resultsGrid.nextSibling);
        }
    }

    function removeLoadMore() {
        const existing = document.getElementById('loadMoreBtn');
        if (existing) existing.remove();
    }

    // ===== Search =====
    function performSearch() {
        const query = searchInput.value.trim().toLowerCase();
        clearSearch.style.display = query ? 'block' : 'none';

        let filtered = allSymbols;

        // Filter by category
        if (activeCategory !== 'all') {
            filtered = filtered.filter(s => s.categoryId === activeCategory);
        }

        // Filter by search query
        if (query) {
            filtered = filtered.filter(s =>
                s.name.toLowerCase().includes(query) ||
                s.unicode.toLowerCase().includes(query) ||
                s.html.toLowerCase().includes(query) ||
                s.char === query ||
                s.categoryName.toLowerCase().includes(query)
            );
            searchStats.textContent = `Found ${filtered.length} result${filtered.length !== 1 ? 's' : ''} for "${searchInput.value.trim()}"`;
        } else {
            searchStats.textContent = `${filtered.length} symbols available`;
        }

        // Update title
        if (activeCategory === 'all') {
            resultsTitle.textContent = query ? 'Search Results' : 'All Symbols';
        } else {
            const cat = categories.find(c => c.id === activeCategory);
            resultsTitle.textContent = cat ? cat.name : 'Symbols';
        }

        renderSymbols(filtered);
    }

    // ===== Copy to Clipboard =====
    async function copyToClipboard(text, message) {
        try {
            await navigator.clipboard.writeText(text);
            showToast(message || 'Copied!');
        } catch {
            // Fallback
            const ta = document.createElement('textarea');
            ta.value = text;
            ta.style.position = 'fixed';
            ta.style.opacity = '0';
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            showToast(message || 'Copied!');
        }
    }

    // ===== Toast =====
    let toastTimer;
    function showToast(message) {
        toastMessage.textContent = message;
        toast.classList.add('show');
        clearTimeout(toastTimer);
        toastTimer = setTimeout(() => toast.classList.remove('show'), 2000);
    }

    // ===== Modal =====
    function openModal(sym) {
        currentModal = sym;
        document.getElementById('modalSymbol').textContent = sym.char;
        document.getElementById('modalName').textContent = sym.name;
        document.getElementById('modalUnicode').textContent = sym.unicode;
        document.getElementById('modalHtml').textContent = sym.html;
        document.getElementById('modalChar').textContent = sym.char;
        document.getElementById('modalCategory').textContent = sym.categoryName || '';
        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = '';
        currentModal = null;
    }

    // ===== Event Listeners =====

    // Search input
    let searchDebounce;
    searchInput.addEventListener('input', () => {
        clearTimeout(searchDebounce);
        searchDebounce = setTimeout(performSearch, 150);
    });

    // Clear search
    clearSearch.addEventListener('click', () => {
        searchInput.value = '';
        clearSearch.style.display = 'none';
        performSearch();
        searchInput.focus();
    });

    // Category filters removed - now on categories.html page

    // Modal close
    modalClose.addEventListener('click', closeModal);
    modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) closeModal();
    });

    // Modal copy buttons
    modal.addEventListener('click', (e) => {
        const btn = e.target.closest('.copy-small-btn');
        if (!btn || !currentModal) return;
        const type = btn.dataset.copy;
        let val = '';
        if (type === 'unicode') val = currentModal.unicode;
        else if (type === 'html') val = currentModal.html;
        else if (type === 'char') val = currentModal.char;
        if (val) copyToClipboard(val, `${val} copied!`);
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Escape to close modal
        if (e.key === 'Escape') {
            if (modalOverlay.classList.contains('active')) {
                closeModal();
            }
        }
        // Ctrl+K or / to focus search
        if ((e.ctrlKey && e.key === 'k') || (e.key === '/' && document.activeElement !== searchInput)) {
            e.preventDefault();
            searchInput.focus();
            searchInput.select();
        }
    });

    // Mobile menu
    mobileMenuBtn.addEventListener('click', () => {
        nav.classList.toggle('open');
    });

    // Close mobile menu on nav link click
    nav.addEventListener('click', (e) => {
        if (e.target.classList.contains('nav-link')) {
            nav.classList.remove('open');
        }
    });

    // ===== Start =====
    init();
})();
