# NXT Sports

NXT Sports — это веб-сайт для каталога спортивных товаров с возможностью управления товарами, корзиной и пользовательскими профилями. Проект реализован на Django с использованием Django REST Framework для API и Swagger для документации.

## Основные возможности

- Просмотр каталога товаров с категориями
- Управление корзиной (добавление, удаление, обновление количества)
- Регистрация, вход и управление профилем пользователя
- Административная панель для управления товарами
- REST API с документацией Swagger

## Технологии

- Python 3
- Django 5
- Django REST Framework
- drf-yasg (Swagger)
- PostgreSQL
- HTML, CSS, JavaScript

## Установка и запуск

1. Клонируйте репозиторий:
   ```
   git clone <https://github.com/silvia15s-s/asdad>
   cd nxt_sports
   ```

2. Создайте и активируйте виртуальное окружение:
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

4. Настройте базу данных PostgreSQL и обновите параметры в `nxt_sports/settings.py`:
   - NAME, USER, PASSWORD, HOST, PORT

5. Примените миграции:
   ```
   python manage.py migrate
   ```

6. Запустите сервер разработки:
   ```
   python manage.py runserver
   ```

7. Откройте в браузере:
   - Основной сайт: http://127.0.0.1:8000/
   - Swagger API документация: http://127.0.0.1:8000/swagger/
   - Redoc документация: http://127.0.0.1:8000/redoc/

## API

- Полный набор CRUD операций для товаров и категорий доступен через REST API.
- Документация API доступна через Swagger UI.

## Структура проекта

- `main/` — основное приложение с моделями, формами, представлениями и шаблонами.
- `nxt_sports/` — настройки проекта.
- `templates/` — шаблоны HTML.
- `static/` — статические файлы (CSS, JS, изображения).
- `media/` — загружаемые пользователями файлы.

## Контакты

Для вопросов и предложений пишите на @NXTSPORT

---
