import os
import re

with open('websites.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace CSS
old_css = """    /* Timeline */
    .timeline {
      display: flex;
      justify-content: space-between;
      max-width: 900px;
      margin: 60px auto 0;
      position: relative;
    }
    .timeline::before {
      content: '';
      position: absolute;
      top: 25px;
      left: 0;
      right: 0;
      height: 2px;
      background: var(--border-color);
      z-index: 1;
    }
    .timeline-step {
      position: relative;
      z-index: 2;
      text-align: center;
      flex: 1;
    }
    .step-icon {
      width: 50px;
      height: 50px;
      background: var(--card-bg);
      border: 2px solid var(--accent-color-1);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 15px;
      font-size: 1.2rem;
    }
    .step-title {
      font-weight: bold;
      font-size: 0.9rem;
      text-transform: uppercase;
    }"""

new_css = """    /* Timeline Enhanced */
    .timeline {
      display: flex;
      justify-content: space-between;
      max-width: 1000px;
      margin: 80px auto 0;
      position: relative;
    }
    .timeline::before {
      content: '';
      position: absolute;
      top: 35px;
      left: 0;
      right: 0;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--border-color) 20%, var(--border-color) 80%, transparent);
      z-index: 1;
    }
    .timeline-step {
      position: relative;
      z-index: 2;
      text-align: center;
      flex: 1;
      padding: 0 10px;
      transition: var(--transition);
    }
    .timeline-step:hover {
      transform: translateY(-8px);
    }
    .timeline-step:hover .step-icon {
      background: rgba(201, 168, 76, 0.08);
      box-shadow: 0 0 30px rgba(201, 168, 76, 0.25);
      border-color: var(--accent-color-2);
    }
    .step-icon {
      width: 70px;
      height: 70px;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      box-shadow: 0 8px 20px rgba(0,0,0,0.4);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 20px;
      color: var(--accent-color-1);
      transition: var(--transition);
    }
    .step-icon svg {
      width: 28px;
      height: 28px;
    }
    .step-title {
      font-weight: 600;
      font-size: 0.95rem;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 6px;
    }
    .step-desc {
      font-size: 0.85rem;
      opacity: 0.7;
      font-family: var(--font-body);
    }"""

content = content.replace(old_css, new_css)

# Update media query
content = content.replace("left: 25px;\n        width: 2px;", "left: 35px;\n        width: 2px;")

# 2. Replace HTML
old_html = """      <div class="timeline">
        <div class="timeline-step">
          <div class="step-icon">📋</div>
          <div class="step-title">1. Discovery Brief</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">🎨</div>
          <div class="step-title">2. Design Mockup</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">✏️</div>
          <div class="step-title">3. Revisions</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">🚀</div>
          <div class="step-title">4. Launch</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">💛</div>
          <div class="step-title">5. Ongoing Support</div>
        </div>
      </div>"""

new_html = """      <div class="timeline">
        <div class="timeline-step">
          <div class="step-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          </div>
          <div class="step-title">1. Discovery Brief</div>
          <div class="step-desc">Vision & Scope</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"></path><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path><path d="M2 2l7.586 7.586"></path><circle cx="11" cy="11" r="2"></circle></svg>
          </div>
          <div class="step-title">2. Design Mockup</div>
          <div class="step-desc">Concepts & UI</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
          </div>
          <div class="step-title">3. Revisions</div>
          <div class="step-desc">Refining Details</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
          </div>
          <div class="step-title">4. Launch</div>
          <div class="step-desc">Handover & Live</div>
        </div>
        <div class="timeline-step">
          <div class="step-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          </div>
          <div class="step-title">5. Ongoing Support</div>
          <div class="step-desc">Post-Launch Care</div>
        </div>
      </div>"""

content = content.replace(old_html, new_html)

with open('websites.html', 'w', encoding='utf-8') as f:
    f.write(content)
