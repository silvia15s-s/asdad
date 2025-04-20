// Инициализация корзины
let cart = [];

// Загрузка корзины из localStorage
function loadCartFromStorage() {
    const savedCart = localStorage.getItem('nxtSportsCart');
    if (savedCart) {
        cart = JSON.parse(savedCart);
        updateCartCount();
    }
}

// Сохранение корзины в localStorage
function saveCartToStorage() {
    localStorage.setItem('nxtSportsCart', JSON.stringify(cart));
}

// Обновление счетчика корзины
function updateCartCount() {
    const cartCount = document.querySelector('.cart-count');
    if (cartCount) {
        const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        cartCount.textContent = totalItems;
    }
}

// Добавление товара в корзину
function addToCart(productId, productTitle, productPrice) {
    const existingItem = cart.find(item => item.id === productId);
    
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            id: productId,
            title: productTitle,
            price: productPrice,
            quantity: 1
        });
    }
    
    updateCartCount();
    saveCartToStorage();
}

// Фильтрация по категориям
function setupCategoryTabs() {
    document.querySelectorAll('.tab-button').forEach(button => {
        button.addEventListener('click', () => {
            // Удаляем активный класс у всех кнопок
            document.querySelectorAll('.tab-button').forEach(btn => {
                btn.classList.remove('active');
            });
            
            // Добавляем активный класс текущей кнопке
            button.classList.add('active');
            
            // Получаем выбранную категорию
            const category = button.getAttribute('data-tab');
            
            // Фильтруем товары
            document.querySelectorAll('.product-list').forEach(list => {
                if (list.id === category) {
                    list.style.display = 'grid';
                } else {
                    list.style.display = 'none';
                }
            });
        });
    });
}

// Управление модальными окнами
function setupModals() {
    // Открытие модального окна
    document.querySelectorAll('.product-about-btn').forEach(button => {
        button.addEventListener('click', function() {
            const modalId = this.getAttribute('data-modal');
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.style.display = 'block';
                document.body.style.overflow = 'hidden';
            }
        });
    });

    // Закрытие модального окна
    document.querySelectorAll('.close-modal').forEach(span => {
        span.addEventListener('click', function() {
            this.closest('.modal').style.display = 'none';
            document.body.style.overflow = 'auto';
        });
    });

    // Закрытие при клике вне окна
    window.addEventListener('click', function(event) {
        if (event.target.classList.contains('modal')) {
            event.target.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    // Загружаем корзину
    loadCartFromStorage();
    
    // Настраиваем кнопки добавления в корзину
    document.querySelectorAll('.product-add-to-cart').forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-id');
            const productTitle = this.closest('.product-item').querySelector('.product-title').textContent;
            const productPrice = this.closest('.product-item').querySelector('.product-price').textContent;
            
            addToCart(productId, productTitle, productPrice);
            alert('Товар добавлен в корзину');
        });
    });
    
    // Настраиваем табы категорий
    setupCategoryTabs();
    
    // Настраиваем модальные окна
    setupModals();
    
    // Показываем первую категорию по умолчанию
    const firstTab = document.querySelector('.tab-button');
    if (firstTab) {
        firstTab.classList.add('active');
        const firstCategory = firstTab.getAttribute('data-tab');
        const firstList = document.getElementById(firstCategory);
        if (firstList) {
            firstList.style.display = 'grid';
        }
    }
});