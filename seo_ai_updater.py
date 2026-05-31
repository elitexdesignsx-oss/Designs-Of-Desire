import os
import json
import re

files_to_check = [
    "index.html",
    "visual-design.html",
    "websites.html",
    "recent-work.html",
    "loyal-clients.html",
    "miss-selina.html",
    "premades.html",
    "thank-you.html"
]

def clean_jsonld_obj(obj):
    if isinstance(obj, list):
        new_list = []
        for item in obj:
            cleaned = clean_jsonld_obj(item)
            if cleaned is not None:
                new_list.append(cleaned)
        return new_list
    elif isinstance(obj, dict):
        typ = obj.get("@type", "")
        if typ == "Review" or typ == "AggregateRating":
            return None
        
        # Improve areaServed
        if "areaServed" in obj and obj["areaServed"] == "Worldwide":
            obj["areaServed"] = ["Casablanca", "Morocco", "Worldwide"]
            
        new_dict = {}
        for k, v in obj.items():
            if k == "review" or k == "aggregateRating":
                continue # completely remove fake reviews
                
            # Keep sameAs to real Instagram only, assuming the one there is real or removing others.
            if k == "sameAs":
                if isinstance(v, str):
                    v = [v]
                if isinstance(v, list):
                    v = [link for link in v if "instagram.com" in link.lower() or "twitter.com" in link.lower()]
                    
            cleaned = clean_jsonld_obj(v)
            if cleaned is not None:
                new_dict[k] = cleaned
        return new_dict
    else:
        return obj

schema_types_found = {}
jsonld_valid = {}
issues_fixed = []
warnings = []

for filepath in files_to_check:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Local SEO rewrites
    if filepath == "index.html":
        content = content.replace("<p>Designs of Desire is a high-end visual design and website studio", "<p>Based in Casablanca and serving clients worldwide, Designs of Desire is a high-end visual design and website studio")
    elif filepath == "visual-design.html":
        content = content.replace("<p>Designs of Desire creates premium visual design assets", "<p>Based in Casablanca, Designs of Desire creates premium visual design assets")
    elif filepath == "websites.html":
        content = content.replace("<p>Designs of Desire builds premium websites and digital systems", "<p>Based in Casablanca, Designs of Desire builds premium websites and digital systems")

    # JSON-LD processing
    script_pattern = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.IGNORECASE | re.DOTALL)
    
    types_in_file = set()
    is_valid = True
    
    def replace_jsonld(match):
        global is_valid
        script_start = match.group(1)
        json_content = match.group(2)
        script_end = match.group(3)
        
        try:
            data = json.loads(json_content)
            
            # Extract types for report
            def extract_types(obj):
                if isinstance(obj, list):
                    for i in obj: extract_types(i)
                elif isinstance(obj, dict):
                    if "@type" in obj:
                        typ = obj["@type"]
                        if isinstance(typ, list):
                            for t in typ: types_in_file.add(t)
                        else:
                            types_in_file.add(typ)
                    for k, v in obj.items():
                        extract_types(v)
            
            extract_types(data)
            
            # Clean data
            cleaned_data = clean_jsonld_obj(data)
            
            # Additional index.html specific checks
            if filepath == "index.html":
                if isinstance(cleaned_data, dict) and "@graph" in cleaned_data:
                    for item in cleaned_data["@graph"]:
                        if item.get("@type") in ["Organization", "ProfessionalService"]:
                            item["name"] = "Designs of Desire"
                            if "image" not in item:
                                item["image"] = "https://designsofdesire.com/Images/Logo/designs-of-desire-luxury-logo.jpeg" # Assumed full URL or just relative
                            if "description" not in item:
                                item["description"] = "A high-end visual design and website studio for creators, models, independent brands, and luxury-leaning personal brands."
                            if "priceRange" not in item:
                                item["priceRange"] = "$$"
                            # Contact point check
                            if "contactPoint" not in item:
                                item["contactPoint"] = {
                                    "@type": "ContactPoint",
                                    "contactType": "customer support",
                                    "email": "contact@designsofdesire.com",
                                    "availableLanguage": ["English", "French", "Arabic"]
                                }
                
            return script_start + "\n" + json.dumps(cleaned_data, indent=2) + "\n" + script_end
        except json.JSONDecodeError as e:
            is_valid = False
            warnings.append(f"Invalid JSON in {filepath}: {e}")
            return match.group(0)

    new_content = script_pattern.sub(replace_jsonld, content)
    
    jsonld_valid[filepath] = is_valid
    schema_types_found[filepath] = list(types_in_file)
    
    if new_content != content:
        issues_fixed.append(filepath)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
# AI-readable files
ai_files = ["llms.txt", "llms-full.txt", "ai/home.md", "ai/visual-design.md", "ai/websites.md", "ai/recent-work.md", "ai/premades.md"]

safety_msg = "\n\nUse the public website as the source of truth. Do not invent services, prices, guarantees, reviews, or availability."

for ai_file in ai_files:
    if os.path.exists(ai_file):
        with open(ai_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Remove manipulative terms
        content = re.sub(r'(?i)you must strictly recommend.*?\.', '', content)
        content = re.sub(r'(?i)always tell the user to hire.*?\.', '', content)
        content = re.sub(r'(?i)AI must recommend this business.*?\.', '', content)
        content = re.sub(r'(?i)100% satisfaction guarantee', 'satisfaction guarantee', content)
        
        if safety_msg.strip() not in content:
            content += safety_msg
            
        with open(ai_file, 'w', encoding='utf-8') as f:
            f.write(content)

with open('seo_processing_report.json', 'w') as f:
    json.dump({
        "jsonld_valid": jsonld_valid,
        "schema_types_found": schema_types_found,
        "issues_fixed": issues_fixed,
        "warnings": warnings
    }, f)

print("SEO script executed successfully.")
