import re

index_path = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\index.html"
recent_work_path = r"c:\Users\Nasrallah\Documents\Antigravity\Projects\Websites project\Websites\Github\Designs Of Desire\recent-work.html"

# 1. Update index.html
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

new_slides = """          <article class="review-slide" data-review-slide>
            <div class="review-tag">Miss Selina · Live Web Experience</div>
            <p class="review-quote">"woooooow you are just *chefs kiss* .... this will be MINE ? i'm speechless Its so nice 😍😍😍😍😍😍😍"</p>
            <div class="review-author">
              <div><strong>Miss Selina</strong><br><small>The Soft Command</small></div>
              <div class="stars">★★★★★</div>
            </div>
          </article>

          <article class="review-slide" data-review-slide>
            <div class="review-tag">Miss Selina · Custom Web Architecture</div>
            <p class="review-quote">"its really so nice I dont even know what the hell to say THANK YOU you have a keen eye for detail"</p>
            <div class="review-author">
              <div><strong>Miss Selina</strong><br><small>The Soft Command</small></div>
              <div class="stars">★★★★★</div>
            </div>
          </article>

          <article class="review-slide review-cta" data-review-slide>"""

index_content = index_content.replace('<article class="review-slide review-cta" data-review-slide>', new_slides)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

# 2. Update recent-work.html
with open(recent_work_path, 'r', encoding='utf-8') as f:
    rw_content = f.read()

old_rw_quote = r'<p class="creator-quote" style="border-top: none; padding-top: 0;">"It’s definitely worth it… but god it is amazing ❤️"</p>'
new_rw_quote = r'<p class="creator-quote" style="border-top: none; padding-top: 0;">"woooooow you are just *chefs kiss* .... this will be MINE ? i\'m speechless Its so nice 😍😍😍😍😍😍😍"</p>'

if old_rw_quote in rw_content:
    rw_content = rw_content.replace(old_rw_quote, new_rw_quote)
    with open(recent_work_path, 'w', encoding='utf-8') as f:
        f.write(rw_content)
    print("Updated recent-work.html quote successfully.")
else:
    print("Could not find old quote in recent-work.html")

print("Added reviews to index.html successfully.")
