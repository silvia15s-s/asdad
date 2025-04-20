from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductCategory, Cart, CartItem
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, CustomUserCreationForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def team(request):
    return render(request, 'main/team.html')

def catalog(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items_count = cart.cartitem_set.count()
    else:
        cart_items_count = 0
    
    return render(request, 'main/catalog.html', {
        'categories': categories,
        'products': products,
        'cart_items_count': cart_items_count
    })





@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'main/login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            
            # Форматирование номера карты перед сохранением
            if profile.card_number:
                card_number = profile.card_number.replace(' ', '')
                profile.card_number = ' '.join([card_number[i:i+4] for i in range(0, len(card_number), 4)])
            
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
        
        # Форматирование номера карты для отображения
        if form.instance.card_number:
            card_number = form.instance.card_number.replace(' ', '')
            form.instance.card_number = ' '.join([card_number[i:i+4] for i in range(0, len(card_number), 4)])

    return render(request, 'main/profile.html', {'form': form})

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.select_related('product').all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart.total_price,
        'cart_items_count': cart.total_items
    }
    return render(request, 'main/cart.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_items_count': cart.total_items
        })
    return redirect(request.META.get('HTTP_REFERER', 'catalog'))

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
@require_POST
def update_cart(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        data = json.loads(request.body)
        action = data.get('action')
        
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        
        cart_item.save()
        
        return JsonResponse({
            'success': True,
            'quantity': cart_item.quantity,
            'item_total': cart_item.total_price,
            'cart_total': cart_item.cart.total_price,
            'cart_items_count': cart_item.cart.total_items
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})