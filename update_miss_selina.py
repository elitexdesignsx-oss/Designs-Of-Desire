import re

filename = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\miss-selina.html"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace background URL
content = content.replace("url('Images/Miss%20Selina/Logo/logo-metallic-style.png')", "url('Images/Miss%20Selina/variation-1.webp')")

# 2. Update Narrative Text
content = content.replace(
    "<dd>Logo variations, metallic styling, transparent logo files, services menu, price list slides, rules graphics, and story highlights.</dd>",
    "<dd>Complete Logo Rebrand, Full Custom Website (thesoftcommand.com), services menu, price list slides, rules graphics, and story highlights.</dd>"
)

content = content.replace(
    "<p>Logo variations, metallic styling, transparent marks, services, price list, rules, and story highlights.</p>",
    "<p>A full brand evolution leading into a high-end, fully custom website architecture.</p>"
)

# 3. Inject CSS
css_inject = """
    /* Device Mockup */
    .mockup-section {
      padding: 100px 0;
      background: var(--bg-color);
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .mockup-header {
      text-align: center;
      margin-bottom: 60px;
    }
    .mockup-header h2 {
      font-size: clamp(2.2rem, 4vw, 3.5rem);
      margin-bottom: 16px;
    }
    .mockup-header p {
      opacity: 0.8;
      max-width: 600px;
      margin: 0 auto;
    }
    .macbook-mockup {
      width: 90%;
      max-width: 1024px;
      margin: 0 auto;
      border: 1px solid var(--border-color);
      border-radius: 12px 12px 0 0;
      background: #111;
      box-shadow: 0 30px 60px rgba(0,0,0,0.4);
      position: relative;
      overflow: hidden;
    }
    [data-theme="marble"] .macbook-mockup {
      background: #f4f4f4;
      box-shadow: 0 30px 60px rgba(0,0,0,0.1);
    }
    .macbook-top-bar {
      height: 32px;
      background: #222;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      padding: 0 16px;
      gap: 6px;
    }
    [data-theme="marble"] .macbook-top-bar {
      background: #e0e0e0;
    }
    .mac-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #ff5f56;
    }
    .mac-dot:nth-child(2) { background: #ffbd2e; }
    .mac-dot:nth-child(3) { background: #27c93f; }
    .mac-url {
      margin: 0 auto;
      background: #333;
      padding: 2px 12px;
      border-radius: 4px;
      font-size: 0.75rem;
      color: #aaa;
      font-family: monospace;
      transform: translateX(-24px); /* offset for dots */
    }
    [data-theme="marble"] .mac-url {
      background: #fff;
      color: #666;
    }
    .macbook-screen {
      width: 100%;
      aspect-ratio: 16/10;
      background: #000;
      position: relative;
    }
    .macbook-screen iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
  </style>
"""
content = content.replace("  </style>", css_inject)

# 4. Inject HTML section
html_inject = """
    <section class="mockup-section reveal">
      <div class="container">
        <div class="mockup-header">
          <div class="eyebrow">The Digital Estate</div>
          <h2>Live Custom Website</h2>
          <p>Experience the brand evolution in its natural habitat. Feel free to scroll and interact with the live website below.</p>
        </div>
        <div class="macbook-mockup">
          <div class="macbook-top-bar">
            <div class="mac-dot"></div>
            <div class="mac-dot"></div>
            <div class="mac-dot"></div>
            <div class="mac-url">thesoftcommand.com</div>
          </div>
          <div class="macbook-screen">
            <iframe src="https://thesoftcommand.com" title="The Soft Command Live Website" loading="lazy"></iframe>
          </div>
        </div>
      </div>
    </section>

    <section class="gallery-section reveal" id="recent-work">
"""
content = content.replace('    <section class="gallery-section reveal" id="recent-work">', html_inject)

# 5. Update Gallery
# Find the start of the work-grid and replace everything up to the List of services item.
old_gallery_pattern = re.compile(r'(<div class="work-grid">).*?(<button class="work-item" data-full="Images/Miss%20Selina/List%20of%20services/list-of-services\.png">)', re.DOTALL)

new_gallery_html = r"""\1
          <button class="work-item" data-full="Images/Miss%20Selina/variation-1.webp">
            <img src="Images/Miss%20Selina/variation-1.webp" alt="Miss Selina Variation 1" loading="lazy" decoding="async" width="1254" height="1254">
            <div class="work-label"><strong>Primary Identity</strong><span>Logo</span></div>
          </button>
          <button class="work-item" data-full="Images/Miss%20Selina/variation-2.webp">
            <img src="Images/Miss%20Selina/variation-2.webp" alt="Miss Selina Variation 2" loading="lazy" decoding="async" width="1254" height="1254">
            <div class="work-label"><strong>Signature Mark</strong><span>Logo</span></div>
          </button>
          <button class="work-item" data-full="Images/Miss%20Selina/variation-3.webp">
            <img src="Images/Miss%20Selina/variation-3.webp" alt="Miss Selina Variation 3" loading="lazy" decoding="async" width="1254" height="1254">
            <div class="work-label"><strong>Brand Emblem</strong><span>Logo</span></div>
          </button>
          <button class="work-item" data-full="Images/Miss%20Selina/variation-4.webp">
            <img src="Images/Miss%20Selina/variation-4.webp" alt="Miss Selina Variation 4" loading="lazy" decoding="async" width="1254" height="1254">
            <div class="work-label"><strong>Secondary Lockup</strong><span>Logo</span></div>
          </button>
          <button class="work-item" data-full="Images/Miss%20Selina/variation-5.webp">
            <img src="Images/Miss%20Selina/variation-5.webp" alt="Miss Selina Variation 5" loading="lazy" decoding="async" width="1254" height="1254">
            <div class="work-label"><strong>Monogram Focus</strong><span>Logo</span></div>
          </button>
          \2"""

content = old_gallery_pattern.sub(new_gallery_html, content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated miss-selina.html successfully")
