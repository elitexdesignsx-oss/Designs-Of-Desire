import os
import glob
import re

html_files = glob.glob('*.html')
js_files = glob.glob('assets/js/*.js')
css_files = glob.glob('assets/css/*.css')

# 1. Read all HTML content
html_content = ""
links_in_html = set()
data_i18n_keys = set()
html_classes = set()

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        html_content += content
        # Find links
        links = re.findall(r'href="([^"#]+.html)"', content)
        links_in_html.update(links)
        
        # Find data-i18n
        keys = re.findall(r'data-i18n="([^"]+)"', content)
        data_i18n_keys.update(keys)
        
        # Find classes
        classes = re.findall(r'class="([^"]+)"', content)
        for cls_str in classes:
            html_classes.update(cls_str.split())

js_content = ""
for f in js_files:
    with open(f, 'r', encoding='utf-8') as file:
        js_content += file.read()

# 2. Check CSS classes
defined_css_classes = set()
for f in css_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        classes = re.findall(r'\.([a-zA-Z0-9_-]+)[^a-zA-Z0-9_-]', content)
        defined_css_classes.update(classes)

unused_css = defined_css_classes - html_classes
# Exclude classes added dynamically by JS
js_added_classes = re.findall(r'classList\.(?:add|toggle|remove|contains)\([\'"]([^\'"]+)[\'"]\)', js_content)
unused_css = unused_css - set(js_added_classes)
# Also exclude state classes like is-active, scrolled, open etc if they are toggled dynamically or missed
# Let's filter some common pseudo-classes and tag names matched accidentally
unused_css = {c for c in unused_css if not c.isdigit() and c not in ('hover', 'active', 'focus', 'before', 'after', 'html')}

print("--- UNUSED CSS CLASSES ---")
for c in sorted(unused_css):
    if len(c) > 2: print(c)

# 3. Check Translation Keys
defined_translations = set()
with open('assets/js/translations.js', 'r', encoding='utf-8') as file:
    content = file.read()
    keys = re.findall(r'([a-zA-Z0-9_]+)\s*:\s*\{', content)
    defined_translations.update(keys)

# Exclude the outer object 'translations'
if 'en' in defined_translations: defined_translations.remove('en')

unused_translations = defined_translations - data_i18n_keys
# wait translations are inside en, fr etc: e.g. en: { "nav_home": "Home" }
# better regex: look inside 'en: {'
en_block = re.search(r'en\s*:\s*\{(.*?)\}', content, re.DOTALL)
if en_block:
    en_keys = re.findall(r'["\']?([a-zA-Z0-9_]+)["\']?\s*:', en_block.group(1))
    defined_translations = set(en_keys)

unused_translations = defined_translations - data_i18n_keys
# some translations might be injected via JS directly
print("\n--- UNUSED TRANSLATION KEYS ---")
for t in unused_translations:
    print(t)

# 4. Unlinked HTML files
unlinked_html = set(html_files) - links_in_html - {'index.html'}
print("\n--- UNLINKED HTML FILES ---")
for h in unlinked_html:
    print(h)

# 5. Commented out code (specifically links or major blocks)
print("\n--- COMMENTED HTML ---")
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        comments = re.findall(r'<!--(.*?)-->', content, re.DOTALL)
        for c in comments:
            if 'premades.html' in c:
                print(f"{f}: premades link commented out")
                break
