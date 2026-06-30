import re

filepath = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\recent-work.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to restore the creator-card styling to the text block and hide the ::before badge on the img col
# Let's find the CREATOR_WEBSITE block

# 1. Update text col: remove the inline overrides so it gets its nice gold border and gradient back
# Old: <div class="showcase-text-col creator-card" style="border: none; padding: 0; text-align: center; max-width: 800px; margin: 0 auto; background: transparent;">
# New: <div class="showcase-text-col creator-card" style="max-width: 900px; margin: 0 auto; text-align: center; display: flex; flex-direction: column; align-items: center;">

# Wait, if we align items center, the left border might look weird if it's centered. Let's make it left-aligned but centered as a block.
# New: <div class="showcase-text-col creator-card" style="max-width: 800px; margin: 0 auto;">

old_text_col = r'<div class="showcase-text-col creator-card" style="border: none; padding: 0; text-align: center; max-width: 800px; margin: 0 auto; background: transparent;">'
new_text_col = r'<div class="showcase-text-col creator-card" style="max-width: 860px; margin: 0 auto; text-align: center; display: flex; flex-direction: column; align-items: center; padding: 40px; border-radius: 8px;">'

# I will also align the text center, but since creator-card has a left border, I'll remove the left border and add a top border or just keep it symmetrical.
new_text_col = r'<div class="showcase-text-col creator-card" style="max-width: 860px; margin: 0 auto; text-align: center; display: flex; flex-direction: column; align-items: center; border-left: none; border-top: 3px solid #f4da8b; background: linear-gradient(180deg, rgba(201, 168, 76, 0.08), transparent 70%); border-radius: 8px; padding: 40px;">'

content = content.replace(old_text_col, new_text_col)

# 2. Add an inline style block to hide the before badge on the website showcase
# Add a class `website-img-col` to the img col
old_img_col = r'<div class="showcase-img-col" style="width: 100%; max-width: 1024px; margin: 0 auto; padding: 0; border: none; background: transparent; box-shadow: none;">'
new_img_col = r'<div class="showcase-img-col website-img-col" style="width: 100%; max-width: 1024px; margin: 0 auto; padding: 0; border: none; background: transparent; box-shadow: none;">'

content = content.replace(old_img_col, new_img_col)

# Add CSS to hide the before badge
css_hide_badge = """
    .website-img-col::before { display: none !important; }
    .website-img-col::after { display: none !important; } /* Also hide the sheen animation over the macbook */
  </style>
"""

content = content.replace("  </style>", css_hide_badge)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Healed and optimized the upper side of the box in recent-work.html")
