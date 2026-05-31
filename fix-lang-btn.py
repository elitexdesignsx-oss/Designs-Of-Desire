import os
import glob
import re

# 1. Update CSS
css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

old_css = """.lang-switch {
  display: inline-flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--border-color);
  color: var(--text-color);
  font-family: var(--font-body);
  font-size: 0.75rem;
  letter-spacing: 1px;
  padding: 6px 14px;
  border-radius: 50px;
  cursor: pointer;
  text-transform: uppercase;
  transition: var(--transition);
}
[data-theme="marble"] .lang-switch {
  background: rgba(0, 0, 0, 0.02);
}
.lang-switch:hover {
  border-color: var(--accent-color-1);
  background: rgba(201, 168, 76, 0.05);
  box-shadow: 0 0 15px rgba(201, 168, 76, 0.15);
  color: var(--accent-color-1);
}"""

new_css = """.lang-switch {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: transparent;
  border: 1px solid var(--border-color);
  color: var(--accent-color-1);
  font-family: var(--font-body);
  font-size: 0.75rem;
  letter-spacing: 2px;
  padding: 8px 18px;
  border-radius: 4px;
  cursor: pointer;
  text-transform: uppercase;
  transition: var(--transition);
  position: relative;
  overflow: hidden;
}
.lang-switch::before {
  content: '';
  position: absolute;
  top: 0; left: -100%; width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(201,168,76,0.15), transparent);
  transition: 0.6s ease;
}
.lang-switch:hover::before {
  left: 100%;
}
[data-theme="marble"] .lang-switch {
  background: rgba(0, 0, 0, 0.02);
}
.lang-switch:hover {
  border-color: var(--accent-color-1);
  box-shadow: 0 0 18px rgba(201, 168, 76, 0.2);
  background: rgba(201, 168, 76, 0.05);
}"""

css = css.replace(old_css, new_css)
with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update JS
js_file = 'assets/js/main.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the globe icon and langLabels block
js = re.sub(
    r"const globeIcon = '<svg[^>]+>.*?</svg>';\s*const langLabels = \{[^}]+\};",
    """const globeIcon = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>';
  const langLabels = { 
    en: `${globeIcon} EN`, 
    fr: `${globeIcon} FR`, 
    de: `${globeIcon} DE`, 
    es: `${globeIcon} ES` 
  };""",
    js
)
with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js)

# 3. Update HTML files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We replace any 🇬🇧 EN inside a button with the new globe layout
    new_html_content = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg> EN'
    html = html.replace('🇬🇧 EN', new_html_content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Language button completely overhauled and hardcoded emojis removed.")
