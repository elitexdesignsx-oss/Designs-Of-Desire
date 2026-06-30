import re
import os

workspace = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"
filepath = os.path.join(workspace, "websites.html")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the merged Pro tier block
merged_pro = """    <div class="web-card elite">
      <div class="fit-label">Pro / Business</div>
      <h3 style="font-size: 2.2rem;">Monetization Hub</h3>
      <div class="gold-gradient-text web-price">€1,000+</div>
      <p class="web-price-note">Scoped after discovery call</p>
      <p class="follower-fit">Best for 50K+ followers</p>
      <p class="web-fit">For established creators running an actual business. Custom content, subscriptions, multiple revenue streams, automation, and brand protection flows.</p>
      <ul>
        <li>Everything in Creator Presence</li>
        <li>Digital product/clip store: Stripe, crypto-friendly</li>
        <li>Subscription or members-only area</li>
        <li>Custom content request system with pricing tiers</li>
        <li>Wishlist integration: Amazon, throne.com</li>
        <li>Tip jar/pay-per-message flow</li>
        <li>DMCA takedown page + watermark guidance</li>
        <li>Multi-persona or multi-brand setup</li>
        <li>Chatbot or intake automation for fan screening</li>
        <li>Collab/affiliate program for other creators</li>
        <li>Advanced analytics dashboard</li>
        <li>Custom DRM/content protection flows</li>
        <li>Full brand identity integration</li>
      </ul>
      <p class="payment-plan"><strong>Payment plan</strong>Discussed individually per project scope (typically 4-Pay Monthly)</p>
      <a href="order.html" class="btn btn-outline" style="width: 100%;" data-quote-service="Pro: Monetization Hub">Explore this tier</a>
    </div>"""

# Regex to match both the Elite and Business tier blocks and replace them with the merged block
# The match starts at <div class="web-card elite"> and ends just before the <aside class="upgrade-policy"
content = re.sub(
    r'\s*<div class="web-card elite">.*?(?=<aside class="upgrade-policy")', 
    '\n' + merged_pro + '\n    ', 
    content, 
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Merged Pro and Business tiers in websites.html")
