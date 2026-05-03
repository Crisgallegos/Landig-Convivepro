document.addEventListener('DOMContentLoaded', () => {
            // 1. Intersection Observer for scroll animations
            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                    }
                });
            }, { root: null, rootMargin: '0px', threshold: 0.15 });

            document.querySelectorAll('.reveal').forEach(el => observer.observe(el));


            // 2. FAQ Accordion Logic
            const faqButtons = document.querySelectorAll('.faq-btn');
            faqButtons.forEach(btn => {
                btn.addEventListener('click', () => {
                    const content = btn.nextElementSibling;
                    const icon = btn.querySelector('.faq-icon');
                    // Toggle current
                    if (content.style.maxHeight) {
                        content.style.maxHeight = null;
                        icon.style.transform = "rotate(0deg)";
                    } else {
                        // Close all others
                        document.querySelectorAll('.faq-content').forEach(c => c.style.maxHeight = null);
                        document.querySelectorAll('.faq-icon').forEach(i => i.style.transform = "rotate(0deg)");
                        // Open current
                        content.style.maxHeight = content.scrollHeight + "px";
                        icon.style.transform = "rotate(180deg)";
                    }
                });
            });


            // 3. Dark Mode Toggle Logic
            const themeToggleBtn = document.getElementById('theme-toggle');
            const darkIcon = document.getElementById('theme-toggle-dark-icon');
            const lightIcon = document.getElementById('theme-toggle-light-icon');

            // Set initial icon based on theme
            if (document.documentElement.classList.contains('dark')) {
                lightIcon.classList.remove('hidden');
            } else {
                darkIcon.classList.remove('hidden');
            }

            themeToggleBtn.addEventListener('click', function () {
                darkIcon.classList.toggle('hidden');
                lightIcon.classList.toggle('hidden');

                if (document.documentElement.classList.contains('dark')) {
                    document.documentElement.classList.remove('dark');
                    localStorage.setItem('color-theme', 'light');
                } else {
                    document.documentElement.classList.add('dark');
                    localStorage.setItem('color-theme', 'dark');
                }
            });


            // 4. Mobile Menu Drawer Logic
            const mobileMenuBtn = document.getElementById('hamburger-menu');
            const closeMenuBtn = document.getElementById('close-menu');
            const mobileMenu = document.getElementById('mobile-menu');
            const menuBackdrop = document.getElementById('menu-backdrop');

            function toggleMenu() {
                mobileMenu.classList.toggle('open');
                menuBackdrop.classList.toggle('hidden');
                // Trigger reflow to apply opacity transition
                void menuBackdrop.offsetWidth;
                menuBackdrop.classList.toggle('open');
            }

            mobileMenuBtn.addEventListener('click', toggleMenu);
            closeMenuBtn.addEventListener('click', toggleMenu);
            menuBackdrop.addEventListener('click', toggleMenu);
            // Close menu when a link inside is clicked
            mobileMenu.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', toggleMenu);
            });


            // 5. Pricing Toggle (Mensual / Anual)
            const btnMonthly = document.getElementById('toggle-monthly');
            const btnAnnual = document.getElementById('toggle-annual');
            const prices = [
                document.getElementById('price-basic'),
                document.getElementById('price-pro'),
                document.getElementById('price-premium')
            ];

            const activeClass = ['bg-cp-brand', 'text-white', 'shadow-md'];
            const inactiveClass = ['text-cp-text-secondary'];

            function setToggle(mode) {
                prices.forEach(el => {
                    if (el) el.textContent = el.dataset[mode];
                });
                if (mode === 'monthly') {
                    activeClass.forEach(c => btnMonthly.classList.add(c));
                    inactiveClass.forEach(c => btnMonthly.classList.remove(c));
                    inactiveClass.forEach(c => btnAnnual.classList.add(c));
                    activeClass.forEach(c => btnAnnual.classList.remove(c));
                } else {
                    activeClass.forEach(c => btnAnnual.classList.add(c));
                    inactiveClass.forEach(c => btnAnnual.classList.remove(c));
                    inactiveClass.forEach(c => btnMonthly.classList.add(c));
                    activeClass.forEach(c => btnMonthly.classList.remove(c));
                }
            }

            if (btnMonthly && btnAnnual) {
                btnMonthly.addEventListener('click', () => setToggle('monthly'));
                btnAnnual.addEventListener('click', () => setToggle('annual'));
            }
        });


        // --- UX/UI Dynamism Logic ---

        // Dynamic Header
        const header = document.getElementById('main-header');
        const fab = document.getElementById('fab-contact');

        window.addEventListener('scroll', () => {
            // Header transition
            if (window.scrollY > 50) {
                header.classList.remove('bg-transparent', 'border-transparent', 'py-2');
                header.classList.add('bg-cp-surface/90', 'dark:bg-[theme(colors.cp.dark.surface.1)]/90', 'backdrop-blur-md', 'border-b', 'border-cp-border', 'dark:border-[theme(colors.cp.dark.border.DEFAULT)]', 'shadow-sm', 'py-0');
            } else {
                header.classList.add('bg-transparent', 'border-transparent', 'py-2');
                header.classList.remove('bg-cp-surface/90', 'dark:bg-[theme(colors.cp.dark.surface.1)]/90', 'backdrop-blur-md', 'border-b', 'border-cp-border', 'dark:border-[theme(colors.cp.dark.border.DEFAULT)]', 'shadow-sm', 'py-0');
            }
        });

        // Animated Counters using Intersection Observer
        const counters = document.querySelectorAll('.counter');
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = entry.target;
                    const finalValue = parseInt(target.getAttribute('data-target'));
                    const duration = 2000; // ms
                    const step = (finalValue / (duration / 16)); // assuming 60fps (~16ms per frame)
                    let current = 0;

                    const updateCounter = () => {
                        current += step;
                        if (current < finalValue) {
                            target.innerText = Math.ceil(current);
                            requestAnimationFrame(updateCounter);
                        } else {
                            target.innerText = finalValue;
                        }
                    };

                    if (target.innerText === "0") { // Only run once
                        updateCounter();
                    }
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => counterObserver.observe(counter));

        // AI Typing Effect
        const aiTypingText = document.getElementById('ai-typing-text');
        if (aiTypingText) {
            const originalHTML = aiTypingText.innerHTML;
            aiTypingText.innerHTML = '';
            
            const typingObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !aiTypingText.dataset.typed) {
                        aiTypingText.dataset.typed = 'true';
                        
                        // Simple HTML typing effect
                        let i = 0;
                        let isTag = false;
                        let text = '';
                        
                        const typeChar = () => {
                            if (i < originalHTML.length) {
                                const char = originalHTML.charAt(i);
                                text += char;
                                aiTypingText.innerHTML = text + '<span class="animate-pulse border-r-2 border-[#A78BFA] ml-1"></span>';
                                
                                if (char === '<') isTag = true;
                                if (char === '>') isTag = false;
                                
                                i++;
                                
                                // If it's a tag, we type it instantly
                                if (isTag) {
                                    typeChar();
                                } else {
                                    // Randomize typing speed slightly for realism
                                    setTimeout(typeChar, Math.random() * 20 + 10); 
                                }
                            } else {
                                aiTypingText.innerHTML = originalHTML; // remove cursor
                            }
                        };
                        
                        // Add a small delay before starting to type
                        setTimeout(typeChar, 600);
                    }
                });
            }, { threshold: 0.5 });
            
            typingObserver.observe(aiTypingText);
        }
