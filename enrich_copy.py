import re

recent_work_path = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\recent-work.html"
miss_selina_path = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\miss-selina.html"

# 1. Update recent-work.html
with open(recent_work_path, 'r', encoding='utf-8') as f:
    rw_content = f.read()

old_bio = r'<p class="creator-bio" style="margin: 0 auto 20px;">A high-end, immersive digital estate built to convert high-net-worth clients and serve as the ultimate brand destination.</p>'
new_bio = r"""<div class="creator-bio" style="margin: 0 auto 28px; text-align: left; max-width: 720px; font-size: 1.05rem;">
          <p style="margin-bottom: 14px;"><strong>The Challenge:</strong> As a rapidly growing creator, she faced a critical bottleneck—managing over 800 unread DMs. Instagram severely restricted her content control, and replying to everyone manually with image-based price lists was no longer practical or scalable.</p>
          <p><strong>The Solution:</strong> We engineered a multi-page digital estate to give her absolute freedom. The custom architecture provides crystal-clear, dedicated pages for her rules, services, and pricing. Crucially, we integrated a streamlined booking system—allowing real buyers to book directly without waiting in a mountain of texts, empowering her to filter out time-wasters at lightspeed.</p>
        </div>"""

if old_bio in rw_content:
    rw_content = rw_content.replace(old_bio, new_bio)
    with open(recent_work_path, 'w', encoding='utf-8') as f:
        f.write(rw_content)
    print("Updated recent-work.html copy.")
else:
    print("Could not find old bio in recent-work.html")

# 2. Update miss-selina.html
with open(miss_selina_path, 'r', encoding='utf-8') as f:
    ms_content = f.read()

old_mockup_p = r'<p>Experience the brand evolution in its natural habitat. Feel free to scroll and interact with the live website below.</p>'
new_mockup_p = r"""<div style="max-width: 760px; margin: 0 auto 30px; text-align: left; font-size: 1.1rem; line-height: 1.6;">
            <p style="margin-bottom: 16px;"><strong>The Challenge:</strong> Buried under 800+ unread messages, restricted by Instagram's content policies, and relying on static image-based price lists, she was losing countless hours to manual filtering and communication.</p>
            <p><strong>The Solution:</strong> A fully custom, multi-page architecture that reclaims her content freedom. It features highly detailed, elegant pages for rules, services, and prices, all anchored by an automated booking system. Now, serious buyers can book instantly without waiting, while time-wasters are filtered out at lightspeed. Experience the live interactive build below.</p>
          </div>"""

if old_mockup_p in ms_content:
    ms_content = ms_content.replace(old_mockup_p, new_mockup_p)
    with open(miss_selina_path, 'w', encoding='utf-8') as f:
        f.write(ms_content)
    print("Updated miss-selina.html copy.")
else:
    print("Could not find old mockup text in miss-selina.html")
