import os
import re
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

img_pattern = re.compile(r'<img[^>]+>', re.IGNORECASE)

def parse_attributes(tag_string):
    attrs = {}
    attr_pattern = re.compile(r'([\w\-]+)\s*(?:=\s*(?:"([^"]*)"|\'([^\']*)\'|([^>\s]+)))?', re.IGNORECASE)
    inner = tag_string[4:-1]
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
        add_str = " " + " ".join(attrs_to_add)
        new_tag = new_tag[:insert_pos] + add_str + new_tag[insert_pos:]
        
    return new_tag

report = ""

for filepath in files_to_check:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    images_checked = 0
    with_alt = 0
    with_lazy = 0
    with_async = 0
    with_dimensions = 0
    intentional_not_lazy = []
    missing_broken = []
    renaming_rec = []
    
    img_tags = img_pattern.findall(content)
    
    new_content = content
    
    for i, tag in enumerate(img_tags):
        images_checked += 1
        attrs = parse_attributes(tag)
        
        src = attrs.get('src', '')
        if not src:
            missing_broken.append("Missing src in tag: " + tag)
            continue
            
        src_unquoted = urllib.parse.unquote(src)
        
        if 'alt' in attrs and attrs['alt']:
            with_alt += 1
            
        has_lazy = attrs.get('loading') == 'lazy'
        has_async = attrs.get('decoding') == 'async'
        has_dim = 'width' in attrs and 'height' in attrs
        
        img_path = os.path.normpath(os.path.join(os.path.dirname(filepath), src_unquoted))
        if not os.path.exists(img_path):
            missing_broken.append(f"Broken path: {src}")
            continue
            
        if "%20" in src or " " in src_unquoted:
            renaming_rec.append(src)
            
        actual_w, actual_h = None, None
        try:
            with Image.open(img_path) as im:
                actual_w, actual_h = im.size
        except Exception as e:
            missing_broken.append(f"Could not open image {src}")
            
        cls = attrs.get('class', '')
        
        is_hero = False
        is_main_hero = False
        
        if i == 0 or 'nav-logo' in cls.lower():
            is_hero = True
            
        if 'hero-logo' in cls.lower() or 'hero-img' in cls.lower() or 'hero' in cls.lower():
            is_hero = True
            if i <= 2:
                is_main_hero = True
                
        mod_attrs = attrs.copy()
        needs_replace = False
        
        if not has_dim and actual_w and actual_h:
            mod_attrs['added_width'] = True
            mod_attrs['width'] = actual_w
            mod_attrs['added_height'] = True
            mod_attrs['height'] = actual_h
            needs_replace = True
            with_dimensions += 1
        elif has_dim:
            with_dimensions += 1
            
        if is_hero:
            intentional_not_lazy.append(f"{src} (is_hero=True)")
            if is_main_hero and 'fetchpriority' not in attrs:
                 mod_attrs['added_fetchpriority'] = True
                 needs_replace = True
        else:
            if not has_lazy:
                mod_attrs['added_loading'] = True
                needs_replace = True
                with_lazy += 1
            else:
                with_lazy += 1
                
            if not has_async:
                mod_attrs['added_decoding'] = True
                needs_replace = True
                with_async += 1
            else:
                with_async += 1
                
        if needs_replace:
            new_tag = reconstruct_tag(mod_attrs, tag)
            new_content = new_content.replace(tag, new_tag, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    report += f"\nPage: {filepath}\n"
    report += f"- Images checked: {images_checked}\n"
    report += f"- Images with alt text: {with_alt}\n"
    report += f"- Images with loading='lazy': {with_lazy}\n"
    report += f"- Images with decoding='async': {with_async}\n"
    report += f"- Images with width/height: {with_dimensions}\n"
    if intentional_not_lazy:
        report += f"- Intentionally not lazy:\n  - " + "\n  - ".join(set(intentional_not_lazy)) + "\n"
    if missing_broken:
        report += f"- Missing/broken:\n  - " + "\n  - ".join(set(missing_broken)) + "\n"
    if renaming_rec:
        report += f"- Poor filenames (spaces/%20):\n  - " + "\n  - ".join(set(renaming_rec)) + "\n"
        
with open('final_report.txt', 'w', encoding='utf-8') as f:
    f.write(report)
    
print("Changes applied. Report written to final_report.txt.")
