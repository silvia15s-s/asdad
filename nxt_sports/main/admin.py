from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Product, ProductCategory, Cart, CartItem

admin.site.register(UserProfile, UserAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('title', 'description')

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'total_price')
    list_select_related = ('cart', 'product')
    
    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price'