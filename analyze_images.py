import os
import re
import json
import urllib.parse
from PIL import Image

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

report = {
    "pages": {}
}

# Regex to find <img ... > tags
img_pattern = re.compile(r'<img[^>]+>', re.IGNORECASE)

def parse_attributes(tag_string):
    # Very basic attribute parser, doesn't handle escaped quotes inside quotes perfectly but works for most HTML
    attrs = {}
    # find all key="value" or key='value' or key=value
    attr_pattern = re.compile(r'([\w\-]+)\s*(?:=\s*(?:"([^"]*)"|\'([^\']*)\'|([^>\s]+)))?', re.IGNORECASE)
    # remove <img and >
    inner = tag_string[4:-1]
    # some tags might end with />
    if inner.endswith('/'):
        inner = inner[:-1]
    
    for match in attr_pattern.finditer(inner):
        key = match.group(1).lower()
        val = match.group(2) if match.group(2) is not None else (match.group(3) if match.group(3) is not None else match.group(4))
        if val is None:
            val = ""
        attrs[key] = val
    return attrs

def reconstruct_tag(attrs, original_tag):
    # This might be tricky if we want to preserve exact order, but we can just append missing attrs before >
    new_tag = original_tag
    if new_tag.endswith('/>'):
        insert_pos = len(new_tag) - 2
    else:
        insert_pos = len(new_tag) - 1
        
    attrs_to_add = []
    
    if attrs.get('added_loading'):
        attrs_to_add.append('loading="lazy"')
    if attrs.get('added_decoding'):
        attrs_to_add.append('decoding="async"')
    if attrs.get('added_width'):
        attrs_to_add.append(f'width="{attrs["width"]}"')
    if attrs.get('added_height'):
        attrs_to_add.append(f'height="{attrs["height"]}"')
    if attrs.get('added_fetchpriority'):
        attrs_to_add.append('fetchpriority="high"')
        
    if attrs_to_add:
        # replace the original tag with the added attributes
        add_str = " " + " ".join(attrs_to_add)
        new_tag = new_tag[:insert_pos] + add_str + new_tag[insert_pos:]
        
    return new_tag

replacements = []

for filepath in files_to_check:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    page_report = {
        "images_checked": 0,
        "with_alt": 0,
        "with_lazy": 0,
        "with_async": 0,
        "with_dimensions": 0,
        "intentional_not_lazy": [],
        "missing_broken": [],
        "renaming_rec": []
    }
    
    img_tags = img_pattern.findall(content)
    
    # We will track index of tags to identify hero images. 
    # Usually first image or image with class 'hero' or 'logo'
    for i, tag in enumerate(img_tags):
        page_report["images_checked"] += 1
        attrs = parse_attributes(tag)
        
        src = attrs.get('src', '')
        if not src:
            page_report["missing_broken"].append("Missing src in tag: " + tag)
            continue
            
        src_unquoted = urllib.parse.unquote(src)
        
        if 'alt' in attrs:
            page_report["with_alt"] += 1
            
        has_lazy = attrs.get('loading') == 'lazy'
        has_async = attrs.get('decoding') == 'async'
        has_dim = 'width' in attrs and 'height' in attrs
        
        if has_lazy:
            page_report["with_lazy"] += 1
        if has_async:
            page_report["with_async"] += 1
        if has_dim:
            page_report["with_dimensions"] += 1
            
        # check path
        img_path = os.path.normpath(os.path.join(os.path.dirname(filepath), src_unquoted))
        img_path_forward = img_path.replace("\\", "/") # sometimes useful
        if not os.path.exists(img_path):
            page_report["missing_broken"].append(f"Broken path: {src}")
            continue
            
        # check filename space
        if "%20" in src or " " in src_unquoted:
            page_report["renaming_rec"].append(src)
            
        # Get dimensions
        actual_w, actual_h = None, None
        try:
            with Image.open(img_path) as im:
                actual_w, actual_h = im.size
        except Exception as e:
            page_report["missing_broken"].append(f"Could not open image {src}: {e}")
            
        # Determine if hero/above fold
        # Criteria: 'logo' in src/class, or 'hero' in src/class, or it's the first image
        is_hero = False
        cls = attrs.get('class', '')
        if i == 0 or 'hero' in cls.lower() or 'logo' in cls.lower() or 'hero' in src.lower() or 'logo' in src.lower():
            is_hero = True
            
        # modifications needed
        mod_attrs = attrs.copy()
        needs_replace = False
        
        if not has_dim and actual_w and actual_h:
            mod_attrs['added_width'] = True
            mod_attrs['width'] = actual_w
            mod_attrs['added_height'] = True
            mod_attrs['height'] = actual_h
            needs_replace = True
            
        if is_hero:
            page_report["intentional_not_lazy"].append(f"{src} (identified as hero/logo)")
            if 'fetchpriority' not in attrs and 'hero' in cls.lower():
                 # only add to main hero image, maybe not logo
                 mod_attrs['added_fetchpriority'] = True
                 needs_replace = True
        else:
            if not has_lazy:
                mod_attrs['added_loading'] = True
                needs_replace = True
            if not has_async:
                mod_attrs['added_decoding'] = True
                needs_replace = True
                
        if needs_replace:
            new_tag = reconstruct_tag(mod_attrs, tag)
            replacements.append({
                "file": filepath,
                "target": tag,
                "replacement": new_tag
            })
            
    report["pages"][filepath] = page_report

with open('image_report.json', 'w') as f:
    json.dump({"report": report, "replacements": replacements}, f, indent=2)

print(f"Analysis complete. Replacements needed: {len(replacements)}")
