import re

mdd_file = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\project_architecture.mdd"
html_file = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\miss-selina.html"

# Extract old 12 buttons from mdd
with open(mdd_file, 'r', encoding='utf-8') as f:
    mdd_content = f.read()

# The old buttons are enclosed between the "Gilded Command" button and the "At My Feet Seal" button
old_buttons_match = re.search(r'(<button class="work-item" data-full="Images/Miss%20Selina/Logo/logo-metallic-style\.png">.*?</button>)', mdd_content, re.DOTALL)
if not old_buttons_match:
    print("Could not find old buttons in MDD")

# Just grab from the first to the last in that block
start_idx = mdd_content.find('<button class="work-item" data-full="Images/Miss%20Selina/Logo/logo-metallic-style.png">')
end_idx = mdd_content.find('<div class="work-label"><strong>At My Feet Seal</strong><span>Highlight</span></div>\n          </button>')
if start_idx != -1 and end_idx != -1:
    end_idx += len('<div class="work-label"><strong>At My Feet Seal</strong><span>Highlight</span></div>\n          </button>')
    old_buttons = mdd_content[start_idx:end_idx]
else:
    print("Could not find exact bounds for old buttons")
    exit(1)


# Read current HTML
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Extract the 5 new buttons
start_idx_new = html_content.find('<button class="work-item" data-full="Images/Miss%20Selina/variation-1.webp">')
end_idx_new = html_content.find('<div class="work-label"><strong>Monogram Focus</strong><span>Logo</span></div>\n          </button>')
if start_idx_new != -1 and end_idx_new != -1:
    end_idx_new += len('<div class="work-label"><strong>Monogram Focus</strong><span>Logo</span></div>\n          </button>')
    new_buttons = html_content[start_idx_new:end_idx_new]
else:
    print("Could not find new buttons in HTML")
    exit(1)


# Build the new separated gallery section
new_gallery_section = f"""
    <section class="gallery-section reveal" id="phase-two">
      <div class="container">
        <div class="section-intro">
          <h2>Phase II: The Rebrand</h2>
          <p>Her identity evolved from a visual aesthetic into a highly custom, scalable luxury brand. These refined marks act as the seal for her digital estate.</p>
        </div>

        <div class="work-grid">
{new_buttons}
        </div>
      </div>
    </section>

    <section class="gallery-section reveal" id="phase-one" style="padding-top: 60px;">
      <div class="container">
        <div class="section-intro">
          <h2>Phase I: The Foundation</h2>
          <p>Before the website build, we architected her complete visual foundation: metallic styling, transparent cutouts, service menus, price lists, and boundaries.</p>
        </div>

        <div class="work-grid">
{old_buttons}
        </div>
      </div>
    </section>
"""

# Replace the old single gallery section block
# It starts at `<section class="gallery-section reveal" id="recent-work">` and ends at `</section>` before `<section class="quote-section container reveal" id="quotes">`
start_gallery = html_content.find('<section class="gallery-section reveal" id="recent-work">')
end_gallery = html_content.find('</section>\n\n    <section class="quote-section container reveal" id="quotes">')
if start_gallery != -1 and end_gallery != -1:
    end_gallery += len('</section>')
    html_content = html_content[:start_gallery] + new_gallery_section.strip() + html_content[end_gallery:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Successfully updated miss-selina.html with separated galleries!")
else:
    print("Could not find gallery bounds in HTML")

