import re
import os

workspace = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"
filepath = os.path.join(workspace, "websites.html")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the highly optimized block
new_block = """    <aside class="upgrade-policy" aria-labelledby="upgrade-policy-title" style="text-align: center;">
      <div style="max-width: 800px; margin: 0 auto;">
        <div class="fit-label" style="margin: 0 auto 16px;">Upgrade Policy</div>
        <h3 id="upgrade-policy-title" style="margin-bottom: 20px; max-width: 100%;">Your previous payment counts toward the next tier.</h3>
        <p style="margin: 0 auto 40px; font-size: 1.1rem; max-width: 620px;">When you're ready to upgrade to a higher tier, you never start from zero. The amount you've already paid for your current website is simply credited toward your new package.</p>
        
        <div class="upgrade-rule" aria-label="Upgrade formula" style="margin: 0 auto; display: inline-block; text-align: center; border-left: 1px solid rgba(201, 168, 76, 0.34);">
          <span style="margin-bottom: 12px; display: block;">Simple rule</span>
          <strong style="margin-bottom: 10px; font-size: 1.3rem;">New package price - amount already paid = Upgrade cost</strong>
          <small>You only pay the difference.</small>
        </div>
      </div>
    </aside>"""

# Replace the block
content = re.sub(r'\s*<aside class="upgrade-policy".*?</aside>', '\n' + new_block, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("websites.html upgrade policy layout optimized.")
