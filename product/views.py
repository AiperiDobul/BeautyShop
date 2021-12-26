from django.shortcuts import render
from .models import *

def indexView(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})
