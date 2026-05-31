import json, re

with open('index.html', encoding='utf-8') as f:
    content = f.read()

script_pattern = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.IGNORECASE | re.DOTALL)

def rep(match):
    d = json.loads(match.group(2))
    for o in d.get('@graph', []):
        if o.get('@type') in ['Organization', 'ProfessionalService']:
            if 'priceRange' in o:
                o['priceRange'] = 'EUR 10-2000+'
            if 'contactPoint' in o and 'contactType' in o['contactPoint']:
                o['contactPoint']['contactType'] = 'sales'
    return match.group(1) + '\n' + json.dumps(d, indent=2) + '\n' + match.group(3)

new_content = script_pattern.sub(rep, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Schema updated.")
