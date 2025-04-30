from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from main.models import Product, ProductCategory
from main.forms import ProductForm, ProfileForm



def admin_required(view_func):
    decorated_view_func = login_required(user_passes_test(lambda u: u.is_staff)(view_func))
    return decorated_view_func

@admin_required
def admin_product_list(request):
    products = Product.objects.all()
    return render(request, 'main/admin_product_list.html', {'products': products})

@admin_required
def admin_product_add_panel(request):
    from main.forms import ManagerProductForm, ProductSpecsForm
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm()
    return render(request, 'main/admin_product_add_panel.html', {'form': form, 'action': 'Добавить товар'})

@admin_required
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_product_list'))
    else:
        form = ProductForm()
    return render(request, 'main/admin_product_form.html', {'form': form, 'action': 'Создать'})

@admin_required
def admin_product_create_simple(request):
    if request.method == 'POST':
        form = ManagerProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            # Присвоить категорию по умолчанию, если не указана
            default_category = ProductCategory.objects.first()
            if default_category:
                product.category = default_category
            product.save()
            return redirect(reverse('admin_product_list'))
    else:
        form = ManagerProductForm()
    return render(request, 'main/admin_product_form.html', {'form': form, 'action': 'Создать', 'simple_form': True})

@admin_required
def admin_product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_product_list'))
    else:
        form = ProductForm(instance=product)
    return render(request, 'main/admin_product_form.html', {'form': form, 'action': 'Редактировать'})

@admin_required
def admin_product_edit_specs(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductSpecsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_product_list'))
    else:
        form = ProductSpecsForm(instance=product)
    return render(request, 'main/admin_product_edit_specs.html', {'form': form, 'product': product, 'action': 'Редактировать характеристики'})

@admin_required
def admin_product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect(reverse('admin_product_list'))
    return render(request, 'main/admin_product_confirm_delete.html', {'product': product})
