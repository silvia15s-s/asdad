document.addEventListener('DOMContentLoaded', function() {
    // Обработка изменения количества
    document.querySelectorAll('.quantity-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const action = this.getAttribute('data-action');
            const itemId = this.getAttribute('data-id');
            
            fetch(`/update-cart/${itemId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    action: action
                })
            })
            .then(response => response.json())
            .then(data => {
                if(data.success) {
                    location.reload();
                }
            });
        });
    });

    // Удаление товара
    document.querySelectorAll('.remove-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const itemId = this.getAttribute('data-id');
            
            if(confirm('Удалить товар из корзины?')) {
                fetch(`/remove-from-cart/${itemId}/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken'),
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if(data.success) {
                        location.reload();
                    }
                });
            }
        });
    });

    // Функция для получения CSRF токена
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

document.addEventListener('DOMContentLoaded', function() {
    // Обработка изменения количества
    document.querySelectorAll('.quantity-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const row = this.closest('tr');
            const quantityElement = row.querySelector('.quantity');
            let quantity = parseInt(quantityElement.textContent);
            
            if (this.classList.contains('plus')) {
                quantity++;
            } else if (this.classList.contains('minus') && quantity > 1) {
                quantity--;
            }
            
            quantityElement.textContent = quantity;
            
            // Здесь можно добавить AJAX-запрос для обновления на сервере
        });
    });
    
    // Обработка удаления товара
    document.querySelectorAll('.remove-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            if (confirm('Удалить товар из корзины?')) {
                const row = this.closest('tr');
                row.style.opacity = '0';
                setTimeout(() => {
                    row.remove();
                    // Здесь можно добавить AJAX-запрос для удаления на сервере
                    // и обновить общую сумму
                }, 300);
            }
        });
    });
});