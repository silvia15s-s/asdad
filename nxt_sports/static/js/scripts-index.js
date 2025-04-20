// Обработчики для кнопок
document.querySelectorAll('.top-auth-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        if (this.getAttribute('href') === '#') {
            e.preventDefault();
            const action = this.textContent.trim();
            alert(`${action} временно недоступна`);
        }
    });
});

// Добавляем обработчик для пункта CONTACT в меню
document.querySelectorAll('nav ul li a').forEach(link => {
    if(link.textContent.trim() === 'CONTACT') {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const contactSection = document.getElementById('contact');
            if (contactSection) {
                contactSection.scrollIntoView({
                    behavior: 'smooth'
                });
            } else {
                window.location.href = this.getAttribute('href');
            }
        });
    }
});

// Автовоспроизведение видео
document.addEventListener('DOMContentLoaded', function() {
    const video = document.querySelector('.video-background');
    if (video) {
        video.play().catch(e => console.log("Autoplay prevented:", e));
    }
});