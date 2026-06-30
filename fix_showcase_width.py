import re

filepath = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\recent-work.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The current block starts at <!-- CREATOR_WEBSITE --> and ends before <!-- CREATOR_1 -->
pattern = re.compile(r'(<!-- CREATOR_WEBSITE -->\s*<div class="showcase-block vip-client">).*?(<!-- CREATOR_1 -->)', re.DOTALL)

new_block = r"""<!-- CREATOR_WEBSITE -->
    <div class="showcase-block vip-client" style="display: flex; flex-direction: column; gap: 40px; padding: clamp(30px, 5vw, 60px);">
      <div class="showcase-text-col creator-card" style="border: none; padding: 0; text-align: center; max-width: 800px; margin: 0 auto; background: transparent;">
        <h2 class="creator-name">The Soft Command</h2>
        <div class="creator-platform">Live Web Experience</div>
        <div class="vip-meta" style="justify-content: center;">
          <span>Digital Estate</span>
          <span>Fully Custom</span>
          <span>Web Architecture</span>
        </div>
        <p class="creator-bio" style="margin: 0 auto 20px;">A high-end, immersive digital estate built to convert high-net-worth clients and serve as the ultimate brand destination.</p>
        <div class="creator-deliverable" style="justify-content: center; display: flex;">Delivered: Full Custom Website</div>
        <p class="creator-quote" style="border-top: none; padding-top: 0;">"It’s definitely worth it… but god it is amazing ❤️"</p>
        <div class="creator-actions" style="justify-content: center;">
          <a href="miss-selina.html" class="btn btn-outline">View Case Study</a>
          <a href="https://thesoftcommand.com" target="_blank" class="gold-gradient-text">Visit Live Site →</a>
        </div>
      </div>
      
      <div class="showcase-img-col" style="width: 100%; max-width: 1024px; margin: 0 auto; padding: 0; border: none; background: transparent; box-shadow: none;">
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
    </div>

    \2"""

content = pattern.sub(new_block, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated CREATOR_WEBSITE block to be stacked and full-width.")
