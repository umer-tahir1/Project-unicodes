/**
 * UniSearch Chrome Extension - Popup Script
 */

(function () {
    'use strict';

    const searchInput = document.getElementById('searchInput');
    const clearBtn = document.getElementById('clearBtn');
    const tabs = document.getElementById('tabs');
    const results = document.getElementById('results');
    const status = document.getElementById('status');
    const toast = document.getElementById('toast');

    let allSymbols = [];
    let categories = [];
    let activeCat = 'all';

    // Build flat symbol list from embedded data
    function init() {
        if (typeof SYMBOLS_DATA === 'undefined') {
            status.textContent = 'Error loading symbols';
            return;
        }

        categories = SYMBOLS_DATA.categories;
        allSymbols = [];
        categories.forEach(cat => {
            cat.symbols.forEach(sym => {
                allSymbols.push({ ...sym, catId: cat.id, catName: cat.name });
            });
        });

        // Build category tabs
        categories.forEach(cat => {
            const btn = document.createElement('button');
            btn.className = 'tab';
            btn.dataset.cat = cat.id;
            btn.textContent = `${cat.icon} ${cat.name}`;
            tabs.appendChild(btn);
        });

        render(allSymbols);
        status.textContent = `${allSymbols.length} symbols · Right-click for details`;

        // Check for pending search from context menu
        if (chrome.storage && chrome.storage.local) {
            chrome.storage.local.get('pendingSearch', (data) => {
                if (data.pendingSearch) {
                    searchInput.value = data.pendingSearch;
                    chrome.storage.local.remove('pendingSearch');
                    search();
                }
            });
        }
    }

    function render(syms) {
        if (syms.length === 0) {
            results.innerHTML = `
                <div class="empty">
                    <div class="empty-icon">🔍</div>
                    <h3>No symbols found</h3>
                    <p>Try different keywords</p>
                </div>`;
            return;
        }

        const frag = document.createDocumentFragment();
        syms.forEach(sym => {
            const el = document.createElement('div');
            el.className = 'sym';
            el.title = `${sym.name}\n${sym.unicode}`;
            el.innerHTML = `
                <span class="sym-char">${sym.char}</span>
                <span class="sym-name">${sym.name}</span>
                <div class="sym-hover">Copy</div>`;

            el.addEventListener('click', () => {
                copyText(sym.char, `${sym.char} copied!`);
            });

            el.addEventListener('contextmenu', (e) => {
                e.preventDefault();
                // Copy unicode value on right click
                copyText(sym.unicode, `${sym.unicode} copied!`);
            });

            frag.appendChild(el);
        });

        results.innerHTML = '';
        results.appendChild(frag);
    }

    function search() {
        const q = searchInput.value.trim().toLowerCase();
        clearBtn.style.display = q ? 'block' : 'none';

        let filtered = allSymbols;
        if (activeCat !== 'all') {
            filtered = filtered.filter(s => s.catId === activeCat);
        }
        if (q) {
            filtered = filtered.filter(s =>
                s.name.toLowerCase().includes(q) ||
                s.unicode.toLowerCase().includes(q) ||
                s.html.toLowerCase().includes(q) ||
                s.char === q
            );
        }

        render(filtered);
        status.textContent = q
            ? `${filtered.length} result${filtered.length !== 1 ? 's' : ''} for "${searchInput.value.trim()}"`
            : `${filtered.length} symbols · Right-click for Unicode`;
    }

    async function copyText(text, msg) {
        try {
            await navigator.clipboard.writeText(text);
        } catch {
            const ta = document.createElement('textarea');
            ta.value = text;
            ta.style.cssText = 'position:fixed;opacity:0';
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
        }
        showToast(msg);
    }

    let toastTimer;
    function showToast(msg) {
        toast.textContent = msg;
        toast.classList.add('show');
        clearTimeout(toastTimer);
        toastTimer = setTimeout(() => toast.classList.remove('show'), 1500);
    }

    // Events
    let debounce;
    searchInput.addEventListener('input', () => {
        clearTimeout(debounce);
        debounce = setTimeout(search, 120);
    });

    clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        clearBtn.style.display = 'none';
        search();
        searchInput.focus();
    });

    tabs.addEventListener('click', (e) => {
        const btn = e.target.closest('.tab');
        if (!btn) return;
        tabs.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        btn.classList.add('active');
        activeCat = btn.dataset.cat;
        search();
    });

    init();
})();
