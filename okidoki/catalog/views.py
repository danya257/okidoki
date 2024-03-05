from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Modificators, CatMod
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'catalog/list.html', {'category': category, 'categories': categories, 'products': products,
                                                 'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    context = {'product': product}
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/detail.html', {'product': product, 'cart_product_form': cart_product_form})


def modifier_detail(request, modifier_id, modifier_slug):
    modifier = get_object_or_404(Modificators, id=modifier_id, slug=modifier_slug)
    return render(request, 'catalog/modifier_detail.html', {'modifier': modifier})
