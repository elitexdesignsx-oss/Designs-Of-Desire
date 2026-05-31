import os
import re

# 1. Add uniform-stripe CSS to styles.css
css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

new_css = """
/* Uniform Stripes */
.uniform-stripe {
  padding: 80px 0;
  text-align: center;
  width: 100%;
}
.uniform-stripe h2 {
  font-size: 2.2rem;
  margin-bottom: 25px;
  color: inherit;
}
.uniform-stripe .stripe-actions {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}
"""

if '.uniform-stripe' not in css_content:
    css_content += new_css
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# remove inline .bottom-cta css
idx = re.sub(r'\s*\.bottom-cta\s*\{\s*padding:\s*100px\s*0;\s*text-align:\s*center;\s*\}\s*\.bottom-cta\s*h2\s*\{\s*font-size:\s*3rem;\s*margin-bottom:\s*40px;\s*color:\s*var\(--button-text\);\s*\}', '', idx)

# change <section class="bottom-cta gold-gradient-bg"> to use uniform-stripe
idx = idx.replace('class="bottom-cta gold-gradient-bg"', 'class="uniform-stripe gold-gradient-bg"')
idx = idx.replace('class="bottom-cta gold-gradient-bg reveal"', 'class="uniform-stripe gold-gradient-bg reveal"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

# 3. Update visual-design.html
with open('visual-design.html', 'r', encoding='utf-8') as f:
    vd = f.read()

vd = vd.replace('class="bottom-cta gold-gradient-bg reveal"', 'class="uniform-stripe gold-gradient-bg reveal"')
vd = vd.replace('<div class="container" style="display: flex; flex-direction: column; align-items: flex-start;">', '<div class="container">')
vd = vd.replace('<h2 style="font-size: 2.5rem; margin-bottom: 40px; color: var(--button-text);">Not sure which to choose?</h2>', '<h2 style="color: var(--button-text);">Not sure which to choose?</h2>')
vd = vd.replace('<div style="display: flex; gap: 20px;">', '<div class="stripe-actions">')

with open('visual-design.html', 'w', encoding='utf-8') as f:
    f.write(vd)

# 4. Update websites.html
with open('websites.html', 'r', encoding='utf-8') as f:
    web = f.read()

# Update The Creation Process
web = web.replace('<section class="timeline-section container reveal">', '<section class="uniform-stripe timeline-section container reveal">')
web = web.replace('<h2 class="text-center" style="font-size: 2.5rem;">The Creation Process</h2>', '<h2>The Creation Process</h2>')

# Update Bottom CTA
web = web.replace('class="bottom-cta gold-gradient-bg reveal"', 'class="uniform-stripe gold-gradient-bg reveal"')
web = web.replace('<div class="container" style="display: flex; flex-direction: column; align-items: flex-start;">', '<div class="container">')
web = web.replace('<h2 style="font-size: 2.5rem; margin-bottom: 40px; color: var(--button-text);">Want to be featured here?</h2>', '<h2 style="color: var(--button-text);">Want to be featured here?</h2>')
# Wrap the anchor tag in stripe-actions for centering
web = re.sub(r'(<a href="mailto:designs\.of\.desirex@gmail\.com\?subject=Website%20Inquiry"[^>]+>Book Your Design</a>)', r'<div class="stripe-actions">\1</div>', web)

with open('websites.html', 'w', encoding='utf-8') as f:
    f.write(web)

# 5. Update loyal-clients.html
with open('loyal-clients.html', 'r', encoding='utf-8') as f:
    lc = f.read()

lc = lc.replace('<div style="text-align: center; margin-top: 60px;">', '<section class="uniform-stripe reveal">\n      <div class="container">')
# the closing div will become a closing section, but we must be careful
# The structure is: <div style="text-align: center; margin-top: 60px;"> ... </div>  </main>
# Let's do a targeted replace
old_lc_section = """      <div style="text-align: center; margin-top: 60px;">
        <h2>Want your own client story?</h2>
        <p style="opacity: 0.8; max-width: 600px; margin: 0 auto 30px;">
          Start with one asset, or build the full identity: logo, price list, services, rules, highlights, banners, and a brand system that feels unmistakably yours.
        </p>
        <a href="visual-design.html" class="btn btn-primary" style="margin: 0 auto;">Start the Story</a>
      </div>"""
new_lc_section = """      <section class="uniform-stripe">
        <div class="container">
          <h2>Want your own client story?</h2>
          <p style="opacity: 0.8; max-width: 600px; margin: 0 auto 30px;">
            Start with one asset, or build the full identity: logo, price list, services, rules, highlights, banners, and a brand system that feels unmistakably yours.
          </p>
          <div class="stripe-actions">
            <a href="visual-design.html" class="btn btn-primary">Start the Story</a>
          </div>
        </div>
      </section>"""
lc = lc.replace(old_lc_section, new_lc_section)

with open('loyal-clients.html', 'w', encoding='utf-8') as f:
    f.write(lc)

# 6. Update recent-work.html
with open('recent-work.html', 'r', encoding='utf-8') as f:
    rw = f.read()

rw = rw.replace('class="bottom-cta gold-gradient-bg reveal"', 'class="uniform-stripe gold-gradient-bg reveal"')
rw = rw.replace('<h2 style="font-size: 2.5rem; margin-bottom: 40px; color: var(--button-text);">Want to be featured here?</h2>', '<h2 style="color: var(--button-text);">Want to be featured here?</h2>')
rw = re.sub(r'(<a href="mailto:designs\.of\.desirex@gmail\.com\?subject=Booking%20Inquiry"[^>]+>Book Your Design</a>)', r'<div class="stripe-actions">\1</div>', rw)

with open('recent-work.html', 'w', encoding='utf-8') as f:
    f.write(rw)

print('Stripes uniformed successfully!')
