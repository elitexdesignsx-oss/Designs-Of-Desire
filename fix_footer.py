import glob
import re

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the opening div
    content = re.sub(r'<div style="display:\s*flex;\s*gap:\s*60px;">\s*', '', content)
    
    # Remove the closing div before the footer-bottom
    content = re.sub(r'</address>\s*</div>\s*</div>\s*<div class="footer-bottom">', '</address>\n      </div>\n      <div class="footer-bottom">', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed', filename)
