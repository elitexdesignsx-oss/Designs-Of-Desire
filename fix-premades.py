import os
import re

# 1. Update premades.html
with open('premades.html', 'r', encoding='utf-8') as f:
    html = f.read()

# remove .upload-section CSS
html = re.sub(r'\s*\.upload-section\s*\{\s*padding:\s*100px\s*0;\s*text-align:\s*center;\s*background:\s*rgba\(201,\s*168,\s*76,\s*0\.03\);\s*\}', '', html)

# replace section class and add stripe-actions
old_section = """  <section class="upload-section reveal">
    <div class="container">
      <h2 style="font-size: 2rem; margin-bottom: 20px;">Upload Your Own Taste</h2>
      <p style="opacity: 0.8; margin-bottom: 40px;">Not sure which style you like? Upload an inspiration image and I'll match your vibe.</p>
      <a href="mailto:designs.of.desirex@gmail.com?subject=Inspiration%20Upload" class="btn btn-outline">Email Inspiration Image</a>
    </div>
  </section>"""
new_section = """  <section class="uniform-stripe reveal">
    <div class="container">
      <h2>Upload Your Own Taste</h2>
      <p style="opacity: 0.8; margin-bottom: 40px;">Not sure which style you like? Upload an inspiration image and I'll match your vibe.</p>
      <div class="stripe-actions">
        <a href="mailto:designs.of.desirex@gmail.com?subject=Inspiration%20Upload" class="btn btn-outline">Email Inspiration Image</a>
      </div>
    </div>
  </section>"""

html = html.replace(old_section, new_section)
with open('premades.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update websites.html timeline-section CSS removal
with open('websites.html', 'r', encoding='utf-8') as f:
    web = f.read()

# remove padding from .timeline-section so it doesn't conflict
web = re.sub(r'\s*\.timeline-section\s*\{\s*padding:\s*100px\s*0;\s*\}', '', web)

with open('websites.html', 'w', encoding='utf-8') as f:
    f.write(web)


# 3. Check for any other 100px padding sections that are meant to be uniform stripes
print("Done fixing premades and websites padding")
