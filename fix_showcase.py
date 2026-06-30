import re

filepath = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\recent-work.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the showcase-img-col inside CREATOR_WEBSITE
old_html = """      <div class="showcase-img-col" style="padding: 0; border: none; background: transparent; box-shadow: none;">
        <div class="macbook-mockup" style="transform: scale(0.95); transform-origin: center;">
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
      </div>"""

new_html = """      <div class="showcase-img-col" style="padding: 10px; display: flex; align-items: stretch;">
        <iframe src="https://thesoftcommand.com" title="The Soft Command Live Website" loading="lazy" style="width: 100%; aspect-ratio: 1/1; border: none; border-radius: 8px; background: #000;"></iframe>
      </div>"""

if old_html in content:
    content = content.replace(old_html, new_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced mockup with full-box iframe in recent-work.html")
else:
    print("Could not find the exact old HTML to replace.")
