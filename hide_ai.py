import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if agent-summary exists
    if 'agent-summary' in content:
        # replace class="agent-summary container reveal" or similar with "agent-summary sr-only"
        new_content = re.sub(r'class="agent-summary[^"]*"', 'class="agent-summary sr-only"', content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
