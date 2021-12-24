from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})