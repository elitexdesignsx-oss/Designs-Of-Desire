document.addEventListener('DOMContentLoaded', () => {

  // ─── THEME TOGGLE ───────────────────────────────────────────────
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  const savedTheme = localStorage.getItem('dod-theme') || 'noir';
  document.documentElement.setAttribute('data-theme', savedTheme);
  if (themeToggleBtn) {
    themeToggleBtn.querySelector('.theme-icon').textContent = savedTheme === 'noir' ? '◑' : '◐';
  }
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'noir' ? 'marble' : 'noir';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('dod-theme', next);
      themeToggleBtn.querySelector('.theme-icon').textContent = next === 'noir' ? '◑' : '◐';
    });
  }

  // ─── LANGUAGE DROPDOWN ─────────────────────────────────────────
  const langCurrentBtn = document.getElementById('lang-current-btn');
  const langOptions = document.getElementById('lang-options');
  const langs = ['en', 'fr', 'de', 'es'];
  const langLabels = { en: '🇬🇧 EN', fr: '🇫🇷 FR', de: '🇩🇪 DE', es: '🇪🇸 ES' };
  let currentLang = localStorage.getItem('dod-lang') || 'en';

  const applyTranslations = (lang) => {
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (typeof TRANSLATIONS !== 'undefined' && TRANSLATIONS[lang] && TRANSLATIONS[lang][key]) {
        el.innerHTML = TRANSLATIONS[lang][key];
      }
    });
    if (langCurrentBtn) langCurrentBtn.textContent = langLabels[lang] + ' ▾';
    currentLang = lang;
  };

  applyTranslations(currentLang);

  if (langCurrentBtn && langOptions) {
    langCurrentBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      langOptions.classList.toggle('open');
    });
    langOptions.querySelectorAll('button').forEach(btn => {
      btn.addEventListener('click', () => {
        const lang = btn.getAttribute('data-lang');
        localStorage.setItem('dod-lang', lang);
        applyTranslations(lang);
        langOptions.classList.remove('open');
      });
    });
    document.addEventListener('click', () => langOptions.classList.remove('open'));
  }

  // ─── MOBILE MENU ───────────────────────────────────────────────
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  const mobileClose = document.querySelector('.mobile-close');

  const openMenu = () => {
    mobileMenu.classList.add('open');
    hamburger.classList.add('open');
    document.body.style.overflow = 'hidden';
  };
  const closeMenu = () => {
    mobileMenu.classList.remove('open');
    hamburger.classList.remove('open');
    document.body.style.overflow = '';
  };

  if (hamburger) hamburger.addEventListener('click', openMenu);
  if (mobileClose) mobileClose.addEventListener('click', closeMenu);
  if (mobileMenu) {
    mobileMenu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  }

  // ─── NAV SCROLL ────────────────────────────────────────────────
  const nav = document.querySelector('nav');
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        nav.classList.toggle('scrolled', window.scrollY > 60);
        ticking = false;
      });
      ticking = true;
    }
  });

  // ─── INTERSECTION OBSERVER — REVEAL + STAGGER ─────────────────
  const revealItems = document.querySelectorAll('.reveal, .stagger-children');
  if (revealItems.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealItems.forEach(el => observer.observe(el));
  }

  // ─── STATS COUNTER ─────────────────────────────────────────────
  const counters = document.querySelectorAll('.stat-number');
  if (counters.length > 0) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
          entry.target.classList.add('counted');
          const target = +entry.target.getAttribute('data-target');
          const suffix = entry.target.getAttribute('data-suffix') || '';
          const duration = 1600;
          const start = performance.now();
          const step = (timestamp) => {
            const elapsed = timestamp - start;
            const progress = Math.min(elapsed / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
            const current = Math.round(eased * target);
            entry.target.textContent = current + suffix;
            if (progress < 1) requestAnimationFrame(step);
            else entry.target.textContent = target + suffix;
          };
          requestAnimationFrame(step);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach(c => counterObserver.observe(c));
  }

  // ─── HERO PARTICLE CANVAS ──────────────────────────────────────
  const canvas = document.getElementById('hero-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const resize = () => {
      canvas.width = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;
    };
    resize();
    window.addEventListener('resize', resize, { passive: true });

    if (!isReducedMotion) {
      const PARTICLE_COUNT = window.innerWidth < 768 ? 28 : 55;
      const particles = Array.from({ length: PARTICLE_COUNT }, () => ({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 1.4 + 0.4,
        speedY: -(Math.random() * 0.4 + 0.1),
        speedX: (Math.random() - 0.5) * 0.15,
        opacity: Math.random() * 0.6 + 0.1,
        opacityDir: Math.random() > 0.5 ? 0.004 : -0.004,
      }));

      let animId;
      const animate = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {
          p.y += p.speedY;
          p.x += p.speedX;
          p.opacity += p.opacityDir;
          if (p.opacity >= 0.7 || p.opacity <= 0.05) p.opacityDir *= -1;
          if (p.y < -10) { p.y = canvas.height + 10; p.x = Math.random() * canvas.width; }
          const theme = document.documentElement.getAttribute('data-theme');
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
          ctx.fillStyle = theme === 'marble'
            ? `rgba(140, 100, 20, ${p.opacity * 0.7})`
            : `rgba(201, 168, 76, ${p.opacity})`;
          ctx.fill();
        });
        animId = requestAnimationFrame(animate);
      };

      // Only animate when visible
      const heroSection = canvas.parentElement;
      const visibilityObserver = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          animId = requestAnimationFrame(animate);
        } else {
          cancelAnimationFrame(animId);
        }
      }, { threshold: 0 });
      visibilityObserver.observe(heroSection);
    }
  }

  // --- Daily Design Quote Logic ---
  const quoteTextEl = document.getElementById('daily-quote-text');
  const quoteAuthorEl = document.getElementById('daily-quote-author');
  if (quoteTextEl && quoteAuthorEl) {
    const quoteCount = 7;
    // Calculate the day of the year to rotate quotes daily
    const now = new Date();
    const start = new Date(now.getFullYear(), 0, 0);
    const diff = (now - start) + ((start.getTimezoneOffset() - now.getTimezoneOffset()) * 60 * 1000);
    const oneDay = 1000 * 60 * 60 * 24;
    const dayOfYear = Math.floor(diff / oneDay);
    
    // Cycle from 1 to 7
    const quoteIndex = (dayOfYear % quoteCount) + 1;
    
    quoteTextEl.setAttribute('data-i18n', `quote_${quoteIndex}`);
    quoteAuthorEl.setAttribute('data-i18n', `quote_${quoteIndex}_author`);
    
    // Trigger translation update if the global updateTranslations function is available
    if (typeof updateTranslations === 'function') {
      const currentLang = localStorage.getItem('theme-lang') || 'en';
      updateTranslations(currentLang);
    }
  }

});
