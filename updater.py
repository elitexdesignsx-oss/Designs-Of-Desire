import os
import glob
import re

# 1. Update copyright in all html files
html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    new_content = content.replace('&copy; 2025 Designs of Desire', '&copy; 2026 Designs of Desire')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)

# 2. Update websites.html specifically
with open('websites.html', 'r', encoding='utf-8') as f:
    web = f.read()

# Replace Fetish pages
web = web.replace('fetish pages', 'adult creators and niche platforms')

# Remove agency value section
agency_pattern = re.compile(r'<!-- Agency Value -->.*?<!-- Web Cards -->', re.DOTALL)
web = agency_pattern.sub('<!-- Web Cards -->', web)

# Add agency-vs context to cards
card1_old = '<div class="gold-gradient-text web-price">€400 — €600</div>'
card1_new = '<div class="gold-gradient-text web-price">€400 — €600</div>\n      <p class="agency-vs">Agencies charge $5,000–$15,000 for this</p>'
web = web.replace(card1_old, card1_new)

card2_old = '<div class="gold-gradient-text web-price">€1,200 — €1,500</div>'
card2_new = '<div class="gold-gradient-text web-price">€1,200 — €1,500</div>\n      <p class="agency-vs">Agencies charge $8,000–$20,000 for this</p>'
web = web.replace(card2_old, card2_new)

card3_old = '<div class="gold-gradient-text web-price">€2,000+ discussion</div>'
card3_new = '<div class="gold-gradient-text web-price">€2,000+ discussion</div>\n      <p class="agency-vs">Agencies charge $15,000–$50,000 for this</p>'
web = web.replace(card3_old, card3_new)

# Add CSS class
css_target = '    .dod-start strong {\n      display: block;\n      font-family: var(--font-display);\n      font-size: clamp(1.35rem, 2.4vw, 2rem);\n      color: var(--accent-color-1);\n      font-weight: 500;\n      margin-bottom: 6px;\n    }'
new_css = css_target + '\n\n    .agency-vs {\n      font-size: 0.78rem;\n      opacity: 0.52;\n      margin-top: -10px;\n      margin-bottom: 14px;\n      letter-spacing: 0.03em;\n    }'
web = web.replace(css_target, new_css)

# Remove FAQ
faq_pattern = re.compile(r'      <article>\s*<h3>Are the dollar amounts on this page Designs of Desire prices\?</h3>\s*<p>No\. Dollar amounts are shown as agency-market context only\. Designs of Desire package prices are listed in EUR on the website package cards\.</p>\s*</article>\n')
web = faq_pattern.sub('', web)

with open('websites.html', 'w', encoding='utf-8') as f:
    f.write(web)

print('Updated successfully.')
