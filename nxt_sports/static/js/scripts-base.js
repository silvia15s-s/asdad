
// Анимация для корзины
document.querySelectorAll('.product-add-to-cart').forEach(button => {
    button.addEventListener('click', function() {
        const cartCount = document.querySelector('.cart-count');
        cartCount.textContent = parseInt(cartCount.textContent) + 1;
        cartCount.style.transform = 'scale(1.5)';
        setTimeout(() => {
            cartCount.style.transform = 'scale(1)';
        }, 300);
    });
});
