document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');

    // Theme Logic (Resets on refresh)
    const defaultTheme = 'light';
    document.documentElement.setAttribute('data-theme', defaultTheme);
    if (themeIcon) themeIcon.textContent = '🌙';

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            const newTheme = isDark ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            if (themeIcon) themeIcon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
        });
    }
});

const translationCache = new Map();

function applyTranslations(translations) {
    const currentYear = new Date().getFullYear();

    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        let text = translations[key];

        if (!text) return;

        text = text.replace('{{year}}', currentYear);

        if (el.dataset.html === "true") {
            el.innerHTML = text;
        } else {
            el.textContent = text;
        }
    });
}

async function setLanguage(lang) {
    lang = lang.toUpperCase();

    // Update active UI state for language buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
    });

    if (translationCache.has(lang)) {
        applyTranslations(translationCache.get(lang));
        return;
    }

    try {
        const res = await fetch(`/translations/${lang}`);
        const data = await res.json();

        translationCache.set(lang, data);
        applyTranslations(data);

        localStorage.setItem("lang", lang);
    } catch (err) {
        console.error("Translation load failed:", err);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const savedLang = localStorage.getItem("lang") || "EN";
    setLanguage(savedLang);

    document.querySelectorAll(".lang-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            setLanguage(btn.dataset.lang);
        });
    });
});
