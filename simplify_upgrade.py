import re
import os

workspace = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"
filepath = os.path.join(workspace, "websites.html")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new simplified block
new_block = """    <aside class="upgrade-policy" aria-labelledby="upgrade-policy-title">
      <div class="upgrade-policy-header" style="grid-template-columns: 1fr; max-width: 800px; margin: 0 auto; text-align: center;">
        <div>
          <div class="fit-label" style="justify-content: center;">Upgrade Policy</div>
          <h3 id="upgrade-policy-title" style="margin-bottom: 20px;">Your previous payment counts toward the next tier.</h3>
          <p style="margin-bottom: 30px; font-size: 1.1rem;">When you're ready to upgrade to a higher tier, you never start from zero. The amount you've already paid for your current website is simply credited toward your new package.</p>
        </div>
        <div class="upgrade-rule" aria-label="Upgrade formula" style="margin: 0 auto; display: inline-block; text-align: center;">
          <span>Simple rule</span>
          <strong>New package price - amount already paid = Upgrade cost</strong>
          <small>You only pay the difference.</small>
        </div>
      </div>
    </aside>"""

# Replace the old block
# Match from <aside class="upgrade-policy" to </aside>
content = re.sub(r'\s*<aside class="upgrade-policy".*?</aside>', '\n' + new_block, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("websites.html upgrade policy simplified.")
