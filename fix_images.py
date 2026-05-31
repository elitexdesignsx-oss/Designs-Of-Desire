import os
import re
import urllib.parse
import shutil

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll use a regex to find all image src and content paths
image_paths = set()
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        paths = re.findall(r'src=["\'](Images/[^"\']+)["\']', content)
        image_paths.update(paths)
        meta_paths = re.findall(r'content=["\'][^"\']*?(Images/[^"\']+)["\']', content)
        image_paths.update(meta_paths)

def generate_seo_name(old_path):
    # Decode URL-encoded paths
    decoded = urllib.parse.unquote(old_path)
    # Get the basename without extension
    basename = os.path.basename(decoded)
    name, ext = os.path.splitext(basename)
    
    # Check directory to give context
    parts = decoded.split('/')
    context = []
    for p in parts[1:-1]:
        context.append(p.lower().replace(' ', '-'))
        
    # Standardize names
    if "whatsapp" in name.lower() or "photoroom" in name.lower():
        if "miss selina" in decoded.lower() or "soft command" in decoded.lower():
            seo_name = "miss-selina-the-soft-command-brand-identity"
        elif "viper queen" in decoded.lower():
            if "gold" in name.lower():
                seo_name = "viper-queen-luxury-logo-gold"
            else:
                seo_name = "viper-queen-luxury-logo-silver"
        elif "miss blue" in decoded.lower():
            seo_name = "miss-blue-luxury-logo-variation"
        elif "logo" in [p.lower() for p in parts]:
            seo_name = "designs-of-desire-luxury-logo"
        else:
            seo_name = "-".join(context) + "-" + name.lower()
    else:
        # Just slugify the existing name
        seo_name = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

    # Add a hash or counter if name already exists to prevent collisions?
    # We will just append a counter later if needed.
    return seo_name, ext

# Map old_path to new_path
rename_map = {}
used_names = set()

for p in image_paths:
    decoded_p = urllib.parse.unquote(p)
    seo_name, ext = generate_seo_name(p)
    
    # Ensure uniqueness
    base_seo_name = seo_name
    counter = 1
    while base_seo_name in used_names:
        base_seo_name = f"{seo_name}-{counter}"
        counter += 1
    used_names.add(base_seo_name)
    
    # We want to flatten the Images folder or keep the structure? Keeping structure is safer.
    parts = decoded_p.split('/')
    dir_path = '/'.join(parts[:-1])
    new_p = f"{dir_path}/{base_seo_name}{ext}"
    rename_map[p] = new_p

print("Rename operations:")
for old, new in rename_map.items():
    print(f"{old} -> {new}")
    
    # Rename file on disk
    old_disk_path = urllib.parse.unquote(old)
    new_disk_path = urllib.parse.unquote(new)
    
    if os.path.exists(old_disk_path):
        os.rename(old_disk_path, new_disk_path)
    else:
        print(f"WARNING: File {old_disk_path} not found!")

# Now update all HTML files
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    for old, new in rename_map.items():
        # URL encode the new path for HTML
        # But we only need to encode the filename part usually, or the spaces
        # Actually our new names have no spaces. So url encoding the parts is safe.
        encoded_old = old # It's already in the format from HTML
        
        # Build encoded new path
        new_parts = new.split('/')
        encoded_new = '/'.join(urllib.parse.quote(p) for p in new_parts)
        
        content = content.replace(old, encoded_new)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("All HTML files updated.")
