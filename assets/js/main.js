document.addEventListener('DOMContentLoaded', () => {
  // Mark the current page in every repeated navigation area.
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('a[href]').forEach(link => {
    const linkPage = link.getAttribute('href').split('#')[0];
    if (linkPage === currentPage) {
      link.classList.add('active');
    }
  });

  // The public site stays in the noir luxury theme.
  document.documentElement.setAttribute('data-theme', 'noir');
  localStorage.removeItem('dod-theme');

  // Language Toggle
  const langSwitchBtn = document.querySelector('.lang-switch');
  const currentLang = localStorage.getItem('dod-lang') || 'en';
  const langs = ['en', 'fr', 'de', 'es'];
  const langLabels = { en: '🇬🇧 EN', fr: '🇫🇷 FR', de: '🇩🇪 DE', es: '🇪🇸 ES' };
  
  const updateLanguage = (lang) => {
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (TRANSLATIONS[lang] && TRANSLATIONS[lang][key]) {
        el.innerText = TRANSLATIONS[lang][key];
      }
    });
    if (langSwitchBtn) {
      langSwitchBtn.innerHTML = langLabels[lang];
    }
  };

  updateLanguage(currentLang);

  if (langSwitchBtn) {
    langSwitchBtn.addEventListener('click', () => {
      let currentIndex = langs.indexOf(localStorage.getItem('dod-lang') || 'en');
      let nextIndex = (currentIndex + 1) % langs.length;
      let nextLang = langs[nextIndex];
      localStorage.setItem('dod-lang', nextLang);
      updateLanguage(nextLang);
    });
  }

  // Scroll animations
  const reveals = document.querySelectorAll('.reveal');
  const revealOnScroll = () => {
    for (let i = 0; i < reveals.length; i++) {
      let windowHeight = window.innerHeight;
      let elementTop = reveals[i].getBoundingClientRect().top;
      let elementVisible = 100;
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add('active');
      }
    }
  };
  window.addEventListener('scroll', revealOnScroll);
  revealOnScroll(); // Trigger once on load

  // Nav Scroll Effect
  const nav = document.querySelector('nav');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  });

  // Mobile Menu
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
    });
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => mobileMenu.classList.remove('open'));
    });
  }
  
  // Stats counter
  const counters = document.querySelectorAll('.stat-number');
  const speed = 200; 

  const runCounters = () => {
    counters.forEach(counter => {
      const updateCount = () => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText.replace(/\D/g, '');
        const inc = target / speed;
        
        if(count < target) {
          let current = Math.ceil(count + inc);
          let text = current.toString();
          if (counter.getAttribute('data-suffix')) text += counter.getAttribute('data-suffix');
          counter.innerText = text;
          setTimeout(updateCount, 20);
        } else {
          let text = target.toString();
          if (counter.getAttribute('data-suffix')) text += counter.getAttribute('data-suffix');
          counter.innerText = text;
        }
      };
      
      const rect = counter.getBoundingClientRect();
      if(rect.top < window.innerHeight && !counter.classList.contains('counted')) {
        counter.classList.add('counted');
        updateCount();
      }
    });
  };
  
  if (counters.length > 0) {
    window.addEventListener('scroll', runCounters);
    runCounters();
  }

  // Homepage reviews carousel
  const reviewSlides = document.querySelectorAll('[data-review-slide]');
  const reviewPrev = document.getElementById('review-prev');
  const reviewNext = document.getElementById('review-next');
  const reviewDots = document.getElementById('review-dots');

  if (reviewSlides.length > 0 && reviewDots) {
    let reviewIndex = 0;
    let reviewTimer;

    reviewSlides.forEach((_, index) => {
      const dot = document.createElement('button');
      dot.className = 'review-dot';
      dot.type = 'button';
      dot.setAttribute('aria-label', `Show review ${index + 1}`);
      dot.addEventListener('click', () => {
        showReview(index);
        restartReviewTimer();
      });
      reviewDots.appendChild(dot);
    });

    const dots = reviewDots.querySelectorAll('.review-dot');

    const showReview = (index) => {
      reviewIndex = (index + reviewSlides.length) % reviewSlides.length;
      reviewSlides.forEach((slide, slideIndex) => {
        slide.classList.toggle('active', slideIndex === reviewIndex);
      });
      dots.forEach((dot, dotIndex) => {
        dot.classList.toggle('active', dotIndex === reviewIndex);
      });
    };

    const moveReview = (direction) => {
      showReview(reviewIndex + direction);
    };

    const restartReviewTimer = () => {
      window.clearInterval(reviewTimer);
      reviewTimer = window.setInterval(() => moveReview(1), 6200);
    };

    if (reviewPrev) {
      reviewPrev.addEventListener('click', () => {
        moveReview(-1);
        restartReviewTimer();
      });
    }

    if (reviewNext) {
      reviewNext.addEventListener('click', () => {
        moveReview(1);
        restartReviewTimer();
      });
    }

    showReview(0);
    restartReviewTimer();
  }

  // Daily inspiration rotates once per local calendar day.
  const dailyQuoteEl = document.getElementById('daily-inspiration-quote');
  const dailyPersonEl = document.getElementById('daily-inspiration-person');
  const dailyMetaEl = document.getElementById('daily-inspiration-meta');

  if (dailyQuoteEl && dailyPersonEl) {
    const dailyInspirations = [
      { quote: '“Design is the silent ambassador of your brand.”', person: 'Paul Rand' },
      { quote: '“Design is not just what it looks like and feels like. Design is how it works.”', person: 'Steve Jobs' },
      { quote: '“Good design is as little design as possible.”', person: 'Dieter Rams' },
      { quote: '“Less, but better.”', person: 'Dieter Rams' },
      { quote: '“Good design makes a product understandable.”', person: 'Dieter Rams' },
      { quote: '“Good design is honest.”', person: 'Dieter Rams' },
      { quote: '“The details are not the details. They make the design.”', person: 'Charles Eames' },
      { quote: '“If you can design one thing, you can design everything.”', person: 'Massimo Vignelli' },
      { quote: '“Whatever we do, if not understood, fails to communicate and is wasted effort.”', person: 'Massimo Vignelli' },
      { quote: '“There are three responses to a piece of design—yes, no, and WOW! Wow is the one to aim for.”', person: 'Milton Glaser' },
      { quote: '“Design can be art. Design can be aesthetics. Design is so simple, that’s why it is so complicated.”', person: 'Paul Rand' },
      { quote: '“Content precedes design. Design in the absence of content is not design, it’s decoration.”', person: 'Jeffrey Zeldman' },
      { quote: '“People ignore design that ignores people.”', person: 'Frank Chimero' },
      { quote: '“Design is intelligence made visible.”', person: 'Alina Wheeler' },
      { quote: '“A brand is a person’s gut feeling about a product, service, or company.”', person: 'Marty Neumeier' },
      { quote: '“Brand is not what you say it is. It’s what they say it is.”', person: 'Marty Neumeier' },
      { quote: '“If it doesn’t sell, it isn’t creative.”', person: 'David Ogilvy' },
      { quote: '“Make it simple. Make it memorable. Make it inviting to look at. Make it fun to read.”', person: 'Leo Burnett' },
      { quote: '“Advertising is fundamentally persuasion and persuasion happens to be not a science, but an art.”', person: 'Bill Bernbach' },
      { quote: '“Marketing is no longer about the stuff that you make, but about the stories you tell.”', person: 'Seth Godin' },
      { quote: '“People do not buy goods and services. They buy relations, stories, and magic.”', person: 'Seth Godin' },
      { quote: '“Design is really an act of communication.”', person: 'Don Norman' },
      { quote: '“Attractive things work better.”', person: 'Don Norman' },
      { quote: '“My goal is to put the human back into design.”', person: 'Don Norman' },
      { quote: '“Good designers never start by trying to solve the problem given to them.”', person: 'Don Norman' },
      { quote: '“Everything is designed. Few things are designed well.”', person: 'Brian Reed' },
      { quote: '“Simplicity is the ultimate sophistication.”', person: 'Often attributed to Leonardo da Vinci' },
      { quote: '“A designer knows he has achieved perfection not when there is nothing left to add, but when there is nothing left to take away.”', person: 'Antoine de Saint-Exupéry' },
      { quote: '“Art is not what you see, but what you make others see.”', person: 'Edgar Degas' },
      { quote: '“Creativity takes courage.”', person: 'Henri Matisse' },
      { quote: '“Learn the rules like a pro, so you can break them like an artist.”', person: 'Often attributed to Pablo Picasso' },
      { quote: '“Art washes away from the soul the dust of everyday life.”', person: 'Often attributed to Pablo Picasso' },
      { quote: '“Every artist was first an amateur.”', person: 'Often attributed to Ralph Waldo Emerson' },
      { quote: '“The chief enemy of creativity is good sense.”', person: 'Often attributed to Pablo Picasso' },
      { quote: '“Color is a power which directly influences the soul.”', person: 'Wassily Kandinsky' },
      { quote: '“I found I could say things with color and shapes that I couldn’t say any other way.”', person: 'Georgia O’Keeffe' },
      { quote: '“Art enables us to find ourselves and lose ourselves at the same time.”', person: 'Thomas Merton' },
      { quote: '“The purpose of art is washing the dust of daily life off our souls.”', person: 'Often attributed to Pablo Picasso' },
      { quote: '“Fashion fades, only style remains the same.”', person: 'Coco Chanel' },
      { quote: '“Fashions fade, style is eternal.”', person: 'Yves Saint Laurent' },
      { quote: '“Elegance is not about being noticed, it’s about being remembered.”', person: 'Giorgio Armani' },
      { quote: '“Dressing well is a form of good manners.”', person: 'Tom Ford' },
      { quote: '“Look for the woman in the dress. If there is no woman, there is no dress.”', person: 'Coco Chanel' },
      { quote: '“Style is a way to say who you are without having to speak.”', person: 'Often attributed to Rachel Zoe' },
      { quote: '“Luxury is in each detail.”', person: 'Often attributed to Hubert de Givenchy' },
      { quote: '“Elegance is the only beauty that never fades.”', person: 'Audrey Hepburn' },
      { quote: '“Beauty begins the moment you decide to be yourself.”', person: 'Coco Chanel' },
      { quote: '“The best color in the whole world is the one that looks good on you.”', person: 'Coco Chanel' },
      { quote: '“To create, one must first question everything.”', person: 'Eileen Gray' },
      { quote: '“Design is the art of making things possible.”', person: 'Paula Scher' }
    ];

    const today = new Date();
    const localMidnight = new Date(today.getFullYear(), today.getMonth(), today.getDate());
    const dayNumber = Math.floor(localMidnight.getTime() / 86400000);
    const inspirationIndex = dayNumber % dailyInspirations.length;
    const inspiration = dailyInspirations[inspirationIndex];

    dailyQuoteEl.innerText = inspiration.quote;
    dailyPersonEl.innerText = inspiration.person;

    if (dailyMetaEl) {
      dailyMetaEl.innerText = 'A new quote appears here every day.';
    }
  }
});
