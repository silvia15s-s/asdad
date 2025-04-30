document.addEventListener('DOMContentLoaded', function() {
    // Обновление аватара при выборе файла
    const avatarUpload = document.getElementById('avatar-upload');
    if (avatarUpload) {
        avatarUpload.addEventListener('change', function() {
            if (this.files && this.files[0]) {
                const form = this.closest('form');
                form.submit();
            }
        });
    }
    
    // Загрузка корзины
    function loadCartFromStorage() {
        const savedCart = localStorage.getItem('nxtSportsCart');
        if (savedCart) {
            const cart = JSON.parse(savedCart);
            const cartCount = document.querySelector('.cart-count');
            if (cartCount) {
                const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
                cartCount.textContent = totalItems;
            }
        }
    }
    
    loadCartFromStorage();
});