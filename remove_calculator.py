import re
import os

workspace = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"
filepath = os.path.join(workspace, "websites.html")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the calculator HTML section
content = re.sub(r'\s*<!-- ROI Calculator -->\s*<section class="calculator-section.*?</section>', '', content, flags=re.DOTALL)

# Remove the script tag
content = re.sub(r'\s*<script src="assets/js/calculator\.js"></script>', '', content)

# Remove calc CSS block (starts at .calc-container and ends before /* Timeline Enhanced */)
content = re.sub(r'\s*\.calc-container \{.*?(?=\s*/\* Timeline Enhanced \*/)', '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed calculator from websites.html")

# Delete the calculator.js file
js_path = os.path.join(workspace, "assets", "js", "calculator.js")
if os.path.exists(js_path):
    os.remove(js_path)
    print("Deleted calculator.js")
