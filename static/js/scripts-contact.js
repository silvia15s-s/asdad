// Обработка формы
document.querySelector('.contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Thank you for your message! We will contact you soon.');
    this.reset();
});
