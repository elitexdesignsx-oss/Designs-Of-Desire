import re
import os

workspace = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"

def update_websites():
    filepath = os.path.join(workspace, "websites.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Change links
    content = content.replace('href="#website-quote-form"', 'href="order.html"')
    
    # 2. Remove quote form section
    content = re.sub(r'\s*<section class="quote-form-section.*?</section>', '', content, flags=re.DOTALL)
    
    # 3. Remove script logic
    content = re.sub(r'\s*<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*const quoteForm = document\.getElementById\(\'website-quote-form\'\);.*?</script>', '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("websites.html updated.")

def update_visual():
    filepath = os.path.join(workspace, "visual-design.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Change buttons to links
    content = re.sub(
        r'<button class="btn btn-outline order-now-btn" type="button" style="width: 100%;" data-service=".*?" data-budget=".*?">Order Now →</button>',
        r'<a href="order.html" class="btn btn-outline" style="width: 100%;">Order Now →</a>',
        content
    )
    content = re.sub(
        r'<button class="btn btn-outline order-now-btn" type="button" data-service=".*?" data-budget=".*?">Add to Order</button>',
        r'<a href="order.html" class="btn btn-outline">Add to Order</a>',
        content
    )
    
    # 2. Remove modal HTML
    content = re.sub(r'\s*<div class="order-modal" id="order-modal" aria-hidden="true">.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # 3. Remove script logic
    content = re.sub(r'\s*<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*const modal = document\.getElementById\(\'order-modal\'\);.*?</script>', '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("visual-design.html updated.")

def update_index_and_others():
    files_to_check = ["index.html", "recent-work.html"]
    for fname in files_to_check:
        filepath = os.path.join(workspace, fname)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace('websites.html#website-quote-form', 'order.html')
        content = content.replace('visual-design.html#order-modal', 'order.html') # Just in case

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"{fname} updated.")

if __name__ == "__main__":
    update_websites()
    update_visual()
    update_index_and_others()
