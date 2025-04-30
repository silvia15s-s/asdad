from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import views_admin

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'categories', views.ProductCategoryViewSet, basename='category')

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('catalog/', views.catalog, name='catalog'),
    path('cart/', views.view_cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Пути для создания и редактирования товаров из сайта
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:product_id>/edit/', views.edit_product, name='edit_product'),

    # Кастомная админ-панель для товаров
    path('custom-admin/products/', views_admin.admin_product_list, name='admin_product_list'),
    path('custom-admin/products/create/', views_admin.admin_product_create, name='admin_product_create'),
    path('custom-admin/products/create-simple/', views_admin.admin_product_create_simple, name='admin_product_create_simple'),
    path('custom-admin/products/add-panel/', views_admin.admin_product_add_panel, name='admin_product_add_panel'),
    path('custom-admin/products/<int:product_id>/edit/', views_admin.admin_product_edit, name='admin_product_edit'),
    path('custom-admin/products/<int:product_id>/edit-specs/', views_admin.admin_product_edit_specs, name='admin_product_edit_specs'),
    path('custom-admin/products/<int:product_id>/delete/', views_admin.admin_product_delete, name='admin_product_delete'),

    # API routes
    path('api/', include(router.urls)),
]
