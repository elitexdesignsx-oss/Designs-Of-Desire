import re

filepath = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\recent-work.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Using regex to find and replace the creator-bio div entirely
pattern = re.compile(r'<div class="creator-bio".*?</div>', re.DOTALL)

new_bio = """<div class="creator-bio" style="margin: 0 auto 28px; text-align: left; max-width: 720px; font-size: 1.05rem; line-height: 1.6;">
          <p style="margin-bottom: 14px;"><strong>The Challenge:</strong><br>
          She was growing fast as a creator, but it quickly became overwhelming—over 800 unread DMs piling up. Instagram kept limiting what she could do, and sending the same price list images over and over wasn’t sustainable anymore.</p>
          <p><strong>The Solution:</strong><br>
          We built her a clean, multi-page website that finally gave her full control. It has simple, dedicated pages for her rules, services, and pricing. Even better, we added an easy booking system so serious buyers can book directly instead of getting lost in her DMs. This lets her spot the real ones instantly and spend way less time dealing with time-wasters.</p>
        </div>"""

if pattern.search(content):
    content = pattern.sub(new_bio, content, count=1) # Only replace the first one, which is the website block (the other blocks don't have this structure)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated description in recent-work.html")
else:
    print("Could not find the bio block.")
