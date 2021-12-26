from django.shortcuts import render
from .models import *

# Create your views here.

def indexView(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})