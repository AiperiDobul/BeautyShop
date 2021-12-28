from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import AddToCartForm
from django.urls import reverse_lazy

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        quantity = data.get('quantity')
    cart.add(product=product, quantity=quantity)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    cart = Cart(request)
    print(cart)
    return render(request, 'order/cart_detail.html', {'cart': cart.cart})

@login_required
def item_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect(reverse_lazy('cart_detail'))

