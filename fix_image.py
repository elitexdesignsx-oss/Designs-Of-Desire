import os

workspace = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"
filepath = os.path.join(workspace, "loyal-clients.html")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace min-height with aspect-ratio
content = content.replace(
    'min-height: 340px;', 
    'aspect-ratio: 1 / 1;\n      min-height: 300px;'
)

# Wait, maybe the image is 4:5? Let's use background-position: center bottom too just in case.
content = content.replace(
    "center / cover no-repeat;", 
    "center bottom / cover no-repeat;"
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated image layout in loyal-clients.html")
