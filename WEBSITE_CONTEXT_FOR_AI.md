# Designs of Desire - Complete Website Architecture & Codebase Documentation

This document provides a hyper-detailed breakdown of the "Designs of Desire" website to provide full context to Claude or any other AI assistant.

## 1. Project Overview & Identity
- **Project Name:** Designs of Desire
- **Niche:** Premium visual identity and custom website creation for content creators.
- **Aesthetic:** High-end, exclusive, luxury, using gold accents with dark/light themes.
- **Tech Stack:** Vanilla HTML5, CSS3, and JavaScript (No external frameworks like React or Tailwind).
- **Core Capabilities:** Custom i18n (internationalization) system, robust dual-theme toggling, scroll-triggered animations, and canvas-based particle effects.

## 2. Directory & File Structure

```text
/ (Root)
├── index.html            # Landing page (hero, dual services, reviews, daily quotes)
├── visual-design.html    # Visual design services, pricing, and discounted bundles
├── websites.html         # Website creation services (custom vs. basic)
├── recent-work.html      # Portfolio gallery of past projects
├── premades.html         # Pre-made templates/designs for sale
├── Images/               # Contains logos, avatars, and background textures
└── assets/
    ├── css/
    │   └── styles.css    # Centralized stylesheet for the entire website
    └── js/
        ├── main.js       # Core logic (UI interactions, canvas, observers, etc.)
        ├── translations.js # i18n dictionary object
        └── calculator.js   # Pricing calculator logic (used on specific pages)
```

## 3. Core Architecture & Global Systems

### A. Theming System (Dark / Light Mode)
- **Implementation:** Controlled via the `data-theme` attribute on the `<html>` tag.
- **Themes:**
  - **`noir` (Default Dark):** Deep black (`#080808`) with off-white text (`#F0EBE1`). Features a CSS-generated SVG noise grain background.
  - **`marble` (Light):** Off-white (`#F9F6F1`) with dark text (`#1A1614`). Features a light marble texture background image.
- **CSS Variables:** The site relies heavily on CSS variables defined in `:root` and overridden in `[data-theme="marble"]` (e.g., `--bg-color`, `--text-color`, `--accent-color-1`, `--card-bg`).
- **Persistence:** The user's theme choice is saved in `localStorage` under the key `dod-theme`.

### B. Internationalization (i18n)
- **Implementation:** Vanilla JS parser.
- **Languages Supported:** English (`en`), French (`fr`), German (`de`), Spanish (`es`).
- **Mechanics:** 
  1. HTML elements use the `data-i18n="key_name"` attribute.
  2. `translations.js` exposes a global `TRANSLATIONS` object mapping `TRANSLATIONS[lang][key]`.
  3. `main.js` loops over `[data-i18n]` tags and injects the corresponding string based on the active language.
- **Persistence:** Language preference is saved in `localStorage` under the key `dod-lang`.

### C. Styling & Design Tokens (`styles.css`)
- **Typography:**
  - Display Font: `Cormorant Garamond` (Elegant serif for headings)
  - Body Font: `Jost` (Clean sans-serif for readability)
  - Accent Font: `Cinzel` (Uppercase serif for tags, buttons, and eyebrows)
- **Animations & Interactivity:**
  - Scroll Reveals: Elements with `.reveal` or `.stagger-children` are hidden (opacity 0, translated Y) and smoothly animated in using `IntersectionObserver`.
  - Gold Gradients: Used extensively for text (`.gold-gradient-text`) and backgrounds (`.gold-gradient-bg`).
  - Buttons: Feature hover states with glowing box-shadows (`var(--border-glow)`).

## 4. JavaScript Logic & Interactivity (`main.js`)

The `main.js` file handles all DOM interactivity inside a `DOMContentLoaded` event listener:

1. **Theme Toggle:** Listens to `#theme-toggle-btn`, switches the `data-theme` attribute, updates `localStorage`, and changes the icon (◑/◐).
2. **Language Dropdown:** Toggles the visibility of the language selector and triggers the `applyTranslations()` function on selection.
3. **Mobile Menu:** Manages the hamburger icon state and the `.mobile-menu` overlay. Note: The mobile menu has `z-index: 1001` to properly sit above the fixed navigation bar (`z-index: 1000`).
4. **Nav Scroll Effect:** Uses a throttled `window.addEventListener('scroll')` to add a `.scrolled` class to the `<nav>` when scrolled past 60px (adds background blur and borders).
5. **Intersection Observers:**
   - **Reveals:** Observes `.reveal` and `.stagger-children` elements to add an `.active` class when they enter the viewport.
   - **Stats Counter:** Animates numbers from 0 to target (e.g., in `index.html`) using `requestAnimationFrame` with a cubic ease-out function.
6. **Hero Particle Canvas:**
   - Renders floating ambient particles on `#hero-canvas` using the 2D Canvas API.
   - Adapts particle color to the current theme.
   - Pauses rendering when the hero section leaves the viewport via `IntersectionObserver` to save CPU.
   - Respects user accessibility settings (`prefers-reduced-motion`).
7. **Daily Design Quote:** Calculates the current day of the year to cycle through 7 predefined quotes dynamically.

## 5. Page-Specific Details

### A. Home Page (`index.html`)
- **Hero Section:** Features a large title, particle canvas background, pulsing background gradients, and a looping "Scroll" indicator line.
- **Daily Inspiration:** A dynamically updated quote section.
- **Dual Cards:** Links to Visual Design vs Website Creation services.
- **Reviews Carousel:** A horizontal carousel of client testimonials, navigable via arrow buttons and dots, with touch/swipe support.

### B. Visual Design (`visual-design.html`)
- **Services Grid:** Individual product cards (Watermark, Logo, Banners, Posters) with prices.
- **Bundled Packages:** Discounted tiers (Identity Pack, Professional Pack, Empire Pack, Independence Pack) highlighting savings.
- **Add-ons:** Simple pill-shaped UI for additional services like Expedited Delivery.

### C. Navigation & Footer (Shared across pages)
- **Navigation:** Fixed top bar with logo, page links, language dropdown, theme toggle, and hamburger menu.
- **Footer:** Contains branding, tagline, quick links, social connections (Instagram, Email), and a "PayPal Accepted" notice.

## 6. How to Instruct Claude with this File
When giving this file to Claude, you can simply say: 
> *"Here is the complete documentation and architecture of my current codebase. I want to add [Feature X] / modify [Component Y]. Please write the code considering my existing HTML structure, CSS variables, and vanilla JS setup."*
