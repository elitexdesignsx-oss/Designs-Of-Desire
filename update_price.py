import os

workspace = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"
filepath = os.path.join(workspace, "websites.html")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update meta description
content = content.replace('Packages from EUR 150.', 'Packages from EUR 100.')

# Update schema.org minPrice
content = content.replace('"minPrice": 150,', '"minPrice": 100,')

# Update schema.org text description
content = content.replace('Starter: Link & Look for EUR 150 to EUR 250,', 'Starter: Link & Look for EUR 100 to EUR 200,')

# Update FAQ text (Wait, I removed the FAQ section! I did! Let's check if the FAQ text is still there, maybe it was in schema.org)
# Oh, line 847 is <dd> inside some definitions, wait let me check what line 847 was. 
# Ah, I removed the FAQ *section* but maybe there's a hidden schema or the FAQ was in an accordion. 
# It's better to just replace the text broadly.
content = content.replace('Starter: Link & Look: EUR 150-250.', 'Starter: Link & Look: EUR 100-200.')

# Update the card price
content = content.replace('€150–250', '€100–200')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Link & Look price in websites.html")
