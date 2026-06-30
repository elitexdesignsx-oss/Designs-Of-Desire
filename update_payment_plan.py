import os

workspace = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"
filepath = os.path.join(workspace, "websites.html")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the specific text
content = content.replace(
    '2-Pay — 50% at delivery, 50% two weeks later', 
    '2-Pay — 50% at delivery, 50% one week later'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated payment plan in websites.html")
