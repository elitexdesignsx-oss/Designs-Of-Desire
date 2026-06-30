import re
import os

workspace = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire"

def remove_faq(filename):
    filepath = os.path.join(workspace, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and remove the faq-section block
    # It starts with <section class="faq-section and ends with the next </section>
    content = re.sub(r'\s*<section class="faq-section.*?</section>', '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Removed FAQ section from {filename}")

if __name__ == "__main__":
    remove_faq("websites.html")
    remove_faq("visual-design.html")
