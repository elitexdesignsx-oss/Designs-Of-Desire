import os
import re

with open('loyal-clients.html', 'r', encoding='utf-8') as f:
    lc = f.read()

# remove .loyal-cta CSS entirely
lc = re.sub(r'\s*\.loyal-cta\s*\{[^}]*\}', '', lc)
lc = re.sub(r'\s*\.loyal-cta\s*h2\s*\{[^}]*\}', '', lc)
lc = re.sub(r'\s*\.loyal-cta\s*p\s*\{[^}]*\}', '', lc)

old_section = """    <section class="loyal-cta reveal">
      <div class="container">
        <h2>Want your own client story?</h2>
        <p>Start with one asset, or build the full identity: logo, price list, services, rules, highlights, banners, and a brand system that feels unmistakably yours.</p>
        <a href="mailto:designs.of.desirex@gmail.com?subject=Loyal%20Client%20Profile%20Inquiry" class="btn btn-primary">Start the Story</a>
      </div>
    </section>"""

new_section = """    <section class="uniform-stripe gold-gradient-bg reveal">
      <div class="container">
        <h2>Want your own client story?</h2>
        <p>Start with one asset, or build the full identity: logo, price list, services, rules, highlights, banners, and a brand system that feels unmistakably yours.</p>
        <div class="stripe-actions">
          <a href="mailto:designs.of.desirex@gmail.com?subject=Loyal%20Client%20Profile%20Inquiry" class="btn btn-outline">Start the Story</a>
        </div>
      </div>
    </section>"""

lc = lc.replace(old_section, new_section)

with open('loyal-clients.html', 'w', encoding='utf-8') as f:
    f.write(lc)
