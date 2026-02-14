# UniSearch - Unicode Symbol Search & Copy Tool

A fast, lightweight web application and Chrome extension for searching, browsing, and copying Unicode symbols.

## 🌐 Website

### Features
- **Real-time search** across 500+ Unicode symbols
- **Categories**: Emojis, Arrows, Math Symbols, Currency, Punctuation, Shapes, Technical, Box Drawing
- **One-click copy** - click any symbol to copy it to clipboard
- **Right-click** any symbol for detailed view (Unicode, HTML entity, etc.)
- **Keyboard shortcuts**: `Ctrl+K` or `/` to focus search, `Escape` to close modal
- **Responsive design** - works on desktop, tablet, and mobile
- **No login required** - fully public access
- **SEO friendly** - proper meta tags and semantic HTML

### How to Run Locally
1. Open a terminal in the `website/` folder
2. Start any local server:
   ```bash
   # Python
   python -m http.server 8000
   
   # Node.js
   npx serve .
   
   # VS Code Live Server extension
   # Right-click index.html → "Open with Live Server"
   ```
3. Open `http://localhost:8000` in your browser

### Deploy to GitHub Pages
1. Create a GitHub repository
2. Push the `website/` folder contents to the `main` branch
3. Go to **Settings → Pages**
4. Set source to `main` branch, root folder
5. Your site will be live at `https://your-username.github.io/repo-name/`

---

## 🧩 Chrome Extension

### Features
- **Popup search** - access from Chrome toolbar
- **Offline support** - all symbols are embedded, no internet needed
- **Right-click context menu** - select text on any page, right-click → "Search Unicode"
- **Hotkey** - `Alt+U` to open the popup
- **Click to copy** symbol, right-click to copy Unicode value
- **Lightweight** - minimal permissions, fast loading
- **Manifest V3** compliant

### Install Locally (Developer Mode)
1. Open Chrome and go to `chrome://extensions/`
2. Enable **Developer mode** (top-right toggle)
3. Click **Load unpacked**
4. Select the `chrome-extension/` folder
5. The extension icon will appear in your toolbar

### Publish to Chrome Web Store
1. Zip the `chrome-extension/` folder
2. Go to [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole)
3. Pay one-time $5 registration fee
4. Click **New Item** → Upload the ZIP
5. Fill in listing details, screenshots, etc.
6. Submit for review

---

## 📁 Project Structure

```
Project-unicodes/
├── website/
│   ├── index.html          # Main HTML page
│   ├── css/
│   │   └── style.css       # All styles
│   ├── js/
│   │   └── app.js          # Search, copy, modal logic
│   └── data/
│       └── symbols.json    # Symbol database (JSON)
├── chrome-extension/
│   ├── manifest.json       # Extension manifest (V3)
│   ├── popup.html          # Extension popup UI
│   ├── popup.css           # Popup styles
│   ├── popup.js            # Popup logic
│   ├── symbols.js          # Embedded symbol data
│   ├── background.js       # Context menu handler
│   └── icons/
│       ├── icon16.png
│       ├── icon48.png
│       └── icon128.png
└── README.md
```

---

## ➕ How to Add New Symbols

### Method 1: Edit JSON directly
1. Open `website/data/symbols.json`
2. Add new symbols to an existing category:
   ```json
   {
     "char": "♾",
     "name": "Permanent Paper Sign",
     "unicode": "U+267E",
     "html": "&#9854;"
   }
   ```
3. Or add a new category:
   ```json
   {
     "id": "new-category",
     "name": "New Category",
     "icon": "★",
     "symbols": [...]
   }
   ```

### Method 2: Update Chrome Extension
After editing `symbols.json`, regenerate the extension data:
```powershell
$json = Get-Content -Path "website\data\symbols.json" -Raw -Encoding UTF8
$js = "const SYMBOLS_DATA = " + $json + ";"
[System.IO.File]::WriteAllText("chrome-extension\symbols.js", $js, [System.Text.Encoding]::UTF8)
```

---

## 🔧 Technical Details

| Component | Technology |
|-----------|-----------|
| Frontend | Vanilla HTML/CSS/JS |
| Search | Client-side, real-time filtering |
| Styling | Custom CSS with CSS variables |
| Symbol Data | JSON (preloaded) |
| Extension | Manifest V3 |
| Hosting | GitHub Pages (static) |

### Browser Support
- Chrome 90+
- Firefox 90+
- Safari 15+
- Edge 90+

---

## 📄 License

This project is free to use for personal and commercial purposes. Feel free to modify and distribute.
