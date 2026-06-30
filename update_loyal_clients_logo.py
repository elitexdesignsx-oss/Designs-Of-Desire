import re

filepath = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\loyal-clients.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace meta tags
old_meta = "Images/Miss%20Selina/Logo/logo-metallic-style.png"
new_meta = "Images/Recent%20Work/The%20Soft%20command%20logo/miss-selina-variation-1.webp"
content = content.replace(old_meta, new_meta)

# Replace CSS background image
old_css_img = "Images/Miss%20Selina/Logo/other%20variations/logo-transparent-variation-1.png"
new_css_img = "Images/Recent%20Work/The%20Soft%20command%20logo/miss-selina-variation-1.webp"

# We should probably change `contain` to `cover` so the square image fills the 340px high rectangle nicely, or keep `contain`. 
# If it's a square inside a wider rectangle, contain will leave #090909 borders on left/right.
# `cover` will fill the whole rectangle but crop top/bottom. Let's use `cover`.
content = content.replace(old_css_img + "') center / contain", new_css_img + "') center / cover")
content = content.replace(old_css_img + "') center / cover", new_css_img + "') center / cover") # Just in case

# If the replace failed because of exact string matching, fallback to standard replace
content = content.replace(old_css_img, new_css_img)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated loyal-clients.html with the new logo.")
