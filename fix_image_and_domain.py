import os
import glob
import re

workspace = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"

# 1. Fix the image cropping on loyal-clients.html
loyal_path = os.path.join(workspace, "loyal-clients.html")
with open(loyal_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('min-height: 340px;', 'aspect-ratio: 1 / 1;\n      min-height: 300px;')
content = content.replace("center / cover no-repeat;", "center bottom / cover no-repeat;")

with open(loyal_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated image layout in loyal-clients.html")

# 2. Fix the canonical URLs and og:urls across all files
old_url = "https://elitexdesignsx-oss.github.io/Designs-Of-Desire/"
new_url = "https://designsofdesire.netlify.app/"

html_files = glob.glob(os.path.join(workspace, "*.html"))
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_url in content:
        content = content.replace(old_url, new_url)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated domain in {os.path.basename(filepath)}")

# Also check for robots.txt or sitemap.xml if they exist
for fname in ["sitemap.xml", "robots.txt"]:
    filepath = os.path.join(workspace, fname)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if old_url in content:
            content = content.replace(old_url, new_url)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated domain in {fname}")
