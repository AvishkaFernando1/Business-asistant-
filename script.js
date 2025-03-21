// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.background = 'transparent';
        navbar.style.boxShadow = 'none';
    }
});

// Theme switcher functionality
const themes = {
    light: {
        background: '#ffffff',
        text: '#333333',
        primary: '#4A90E2'
    },
    dark: {
        background: '#1a1a1a',
        text: '#ffffff',
        primary: '#64B5F6'
    },
    blue: {
        background: '#1e3d59',
        text: '#ffffff',
        primary: '#17c0eb'
    }
};

function setTheme(themeName) {
    const root = document.documentElement;
    const theme = themes[themeName];
    
    root.style.setProperty('--background-color', theme.background);
    root.style.setProperty('--text-color', theme.text);
    root.style.setProperty('--primary-color', theme.primary);
    
    localStorage.setItem('theme', themeName);
}

// Initialize theme from localStorage or default to light
const savedTheme = localStorage.getItem('theme') || 'light';
setTheme(savedTheme);

// Theme switcher event listeners
document.querySelectorAll('.theme-btn').forEach(button => {
    button.addEventListener('click', () => {
        setTheme(button.dataset.theme);
    });
});

// Chat widget functionality
const chatWidget = document.querySelector('.chat-widget');
const minimizeBtn = document.querySelector('.minimize-btn');
const chatMessages = document.querySelector('.chat-messages');
const chatInput = document.querySelector('.chat-input textarea');
const sendBtn = document.querySelector('.send-btn');

let isMinimized = false;

// Sample AI responses
const aiResponses = [
    "Hello! How can I assist you today?",
    "I understand. Could you please provide more details?",
    "I'll help you with that right away.",
    "Is there anything else you'd like to know?",
];

minimizeBtn.addEventListener('click', () => {
    isMinimized = !isMinimized;
    chatWidget.style.transform = isMinimized ? 'translateY(calc(100% - 60px))' : 'translateY(0)';
    minimizeBtn.textContent = isMinimized ? '+' : '−';
});

function addMessage(message, isAi = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isAi ? 'ai' : 'user'}`;
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function getAiResponse() {
    const randomIndex = Math.floor(Math.random() * aiResponses.length);
    return aiResponses[randomIndex];
}

function handleSend() {
    const message = chatInput.value.trim();
    if (!message) return;

    addMessage(message);
    chatInput.value = '';

    // Simulate AI response
    setTimeout(() => {
        addMessage(getAiResponse(), true);
    }, 1000);
}

sendBtn.addEventListener('click', handleSend);
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSend();
    }
});
// Add to your existing script.js
function reveal() {
    const reveals = document.querySelectorAll('.reveal');
    
    reveals.forEach(element => {
        const windowHeight = window.innerHeight;
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < windowHeight - elementVisible) {
            element.classList.add('active');
        }
    });
}

window.addEventListener('scroll', reveal);
// Animation on scroll
const animateOnScroll = () => {
    const elements = document.querySelectorAll('.feature-card, .stat-item');
    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < window.innerHeight - elementVisible) {
            element.classList.add('animate');
        }
    });
};

window.addEventListener('scroll', animateOnScroll);

// Mobile menu toggle
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Form submission
// Contact form handling
const contactForm = document.querySelector('.contact-form');
const submitBtn = contactForm?.querySelector('.submit-btn');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Add loading state
        submitBtn.classList.add('loading');
        
        // Simulate form submission
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // Show success message
        const successMessage = document.createElement('div');
        successMessage.className = 'success-message';
        successMessage.textContent = 'Thank you for your message! We will get back to you soon.';
        contactForm.appendChild(successMessage);
        
        // Reset form and button
        contactForm.reset();
        submitBtn.classList.remove('loading');
        
        // Remove success message after 5 seconds
        setTimeout(() => {
            successMessage.remove();
        }, 5000);
    });
}

// Animate info cards on scroll
const infoCards = document.querySelectorAll('.info-card');
const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.transform = 'translateY(0)';
                entry.target.style.opacity = '1';
            }
        });
    },
    { threshold: 0.2 }
);

infoCards.forEach(card => {
    card.style.transform = 'translateY(20px)';
    card.style.opacity = '0';
    card.style.transition = 'all 0.6s ease';
    observer.observe(card);
});

// Footer animations
const footerObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('footer-animate');
        }
    });
}, { threshold: 0.2 });

document.querySelectorAll('.footer-section').forEach(section => {
    footerObserver.observe(section);
});

// Social media hover effects
document.querySelectorAll('.social-links a').forEach(link => {
    link.addEventListener('mouseenter', (e) => {
        e.target.classList.add('social-hover');
    });
});