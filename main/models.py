from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True)
    # Новые поля для платежных реквизитов
    card_number = models.CharField(max_length=19, blank=True, null=True)
    card_expiry = models.CharField(max_length=5, blank=True, null=True)
    card_cvv = models.CharField(max_length=3, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('profile')

    def __str__(self):
        return self.username

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    details = models.TextField()
    specs = models.JSONField(default=dict)
    material = models.CharField(max_length=200, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)
    installation = models.TextField(blank=True, null=True)
    compatibility = models.TextField(blank=True, null=True)
    features = models.TextField()
    achievements = models.TextField()
    
    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return f"Cart #{self.id} for {self.user.username}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.cartitem_set.all())

    @property
    def total_items(self):
        return self.cartitem_set.count()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.product.title} in cart #{self.cart.id}"
