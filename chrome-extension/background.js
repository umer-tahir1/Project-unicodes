// Background service worker for UniSearch Chrome Extension
// Handles context menu for looking up Unicode symbols

chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: 'unisearch-lookup',
        title: 'Search Unicode for "%s"',
        contexts: ['selection']
    });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === 'unisearch-lookup' && info.selectionText) {
        // Open popup with search query
        // Since we can't directly open popup, we'll store the query
        chrome.storage.local.set({ pendingSearch: info.selectionText.trim() });
        // Open the popup by triggering the action
        chrome.action.openPopup().catch(() => {
            // Fallback: open as a new tab with the website
            chrome.tabs.create({
                url: `https://your-username.github.io/unisearch/?q=${encodeURIComponent(info.selectionText.trim())}`
            });
        });
    }
});
