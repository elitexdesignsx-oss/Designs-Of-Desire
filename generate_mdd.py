import os

root_dir = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"
output_file = os.path.join(root_dir, "project_architecture.mdd")

exclude_dirs = {'.git', 'Images'}
exclude_exts = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.woff', '.woff2', '.ttf', '.eot', '.pdf', '.zip'}

def generate_tree(dir_path, prefix=""):
    tree_str = ""
    try:
        items = os.listdir(dir_path)
    except PermissionError:
        return ""
    
    items = [i for i in items if i not in exclude_dirs]
    items.sort()
    
    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        tree_str += f"{prefix}{connector}{item}\n"
        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            tree_str += generate_tree(path, prefix + extension)
    return tree_str

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# Project Architecture\n\n")
    f.write("```\n")
    f.write(os.path.basename(root_dir) + "\n")
    f.write(generate_tree(root_dir))
    f.write("```\n\n")
    
    f.write("# Source Code\n\n")
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in exclude_exts or file == os.path.basename(output_file):
                continue
            
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, root_dir)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as cf:
                    content = cf.read()
                
                f.write(f"## {rel_path}\n\n")
                f.write(f"```{ext.replace('.', '')}\n")
                f.write(content)
                f.write("\n```\n\n")
            except Exception as e:
                pass
print("Created project_architecture.mdd successfully")
