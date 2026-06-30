import re

css_code = """
/* MacBook Device Mockup */
.macbook-mockup {
  width: 100%;
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
  transform: translateX(-24px);
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
"""

with open(r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\assets\css\styles.css", "a", encoding="utf-8") as f:
    f.write("\n" + css_code)

print("Added mockup CSS to styles.css")

# Add the showcase block to recent-work.html
recent_work_path = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\recent-work.html"
with open(recent_work_path, "r", encoding="utf-8") as f:
    content = f.read()

new_block = """
    <!-- CREATOR_WEBSITE -->
    <div class="showcase-block vip-client">
      <div class="showcase-img-col" style="padding: 0; border: none; background: transparent; box-shadow: none;">
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
      </div>
      <div class="showcase-text-col creator-card">
        <h2 class="creator-name">The Soft Command</h2>
        <div class="creator-platform">Live Web Experience</div>
        <div class="vip-meta">
          <span>Digital Estate</span>
          <span>Fully Custom</span>
          <span>Web Architecture</span>
        </div>
        <p class="creator-bio">A high-end, immersive digital estate built to convert high-net-worth clients and serve as the ultimate brand destination.</p>
        <div class="creator-deliverable">Delivered: Full Custom Website</div>
        <p class="creator-quote">"It’s definitely worth it… but god it is amazing ❤️"</p>
        <div class="creator-actions">
          <a href="miss-selina.html" class="btn btn-outline">View Case Study</a>
          <a href="https://thesoftcommand.com" target="_blank" class="gold-gradient-text">Visit Live Site →</a>
        </div>
      </div>
    </div>
"""

content = content.replace("    <!-- CREATOR_1 -->", new_block + "\n    <!-- CREATOR_1 -->")

with open(recent_work_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added showcase to recent-work.html")
