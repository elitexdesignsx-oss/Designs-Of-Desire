import os
import re

# 1. Update styles.css
css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

gold_stripe_css = """
/* Gold Stripe Children */
.gold-gradient-bg h2, 
.gold-gradient-bg p, 
.gold-gradient-bg .step-title {
  color: var(--button-text) !important;
}
.gold-gradient-bg .timeline::before {
  background: var(--button-text) !important;
  opacity: 0.2;
}
.gold-gradient-bg .step-icon {
  border-color: var(--button-text) !important;
  background: transparent !important;
  color: var(--button-text) !important;
}
.gold-gradient-bg .btn-outline {
  border-color: var(--button-text) !important;
  color: var(--button-text) !important;
}
.gold-gradient-bg .btn-primary {
  background: var(--button-text) !important;
  color: var(--text-color) !important; /* Button text inverse */
}
"""
if '/* Gold Stripe Children */' not in css_content:
    css_content += gold_stripe_css
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)

# 2. Update loyal-clients.html
with open('loyal-clients.html', 'r', encoding='utf-8') as f:
    lc = f.read()
lc = lc.replace('<section class="uniform-stripe">', '<section class="uniform-stripe gold-gradient-bg reveal">')
with open('loyal-clients.html', 'w', encoding='utf-8') as f:
    f.write(lc)

# 3. Update premades.html
with open('premades.html', 'r', encoding='utf-8') as f:
    pr = f.read()
pr = pr.replace('<section class="uniform-stripe reveal">', '<section class="uniform-stripe gold-gradient-bg reveal">')
with open('premades.html', 'w', encoding='utf-8') as f:
    f.write(pr)

# 4. Update websites.html
with open('websites.html', 'r', encoding='utf-8') as f:
    web = f.read()

old_timeline = """  <section class="uniform-stripe timeline-section container reveal">
    <h2>The Creation Process</h2>
    <div class="timeline">
      <div class="timeline-step">
        <div class="step-icon">📋</div>
        <div class="step-title">1. Discovery Brief</div>
      </div>
      <div class="timeline-step">
        <div class="step-icon">🎨</div>
        <div class="step-title">2. Design Mockup</div>
      </div>
      <div class="timeline-step">
        <div class="step-icon">✏️</div>
        <div class="step-title">3. Revisions</div>
      </div>
      <div class="timeline-step">
        <div class="step-icon">🚀</div>
        <div class="step-title">4. Launch</div>
      </div>
      <div class="timeline-step">
        <div class="step-icon">💛</div>
        <div class="step-title">5. Ongoing Support</div>
      </div>
    </div>
  </section>"""

new_timeline = """  <section class="uniform-stripe timeline-section gold-gradient-bg reveal">
    <div class="container">
      <h2>The Creation Process</h2>
      <div class="timeline">
        <div class="timeline-step">
          <div class="step-icon">📋</div>
          <div class="step-title">1. Discovery Brief</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">🎨</div>
          <div class="step-title">2. Design Mockup</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">✏️</div>
          <div class="step-title">3. Revisions</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">🚀</div>
          <div class="step-title">4. Launch</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">💛</div>
          <div class="step-title">5. Ongoing Support</div>
        </div>
      </div>
    </div>
  </section>"""

if old_timeline in web:
    web = web.replace(old_timeline, new_timeline)
else:
    print("WARNING: Could not find old_timeline in websites.html")

with open('websites.html', 'w', encoding='utf-8') as f:
    f.write(web)

print("Gold stripes successfully added to all targeted sections.")
