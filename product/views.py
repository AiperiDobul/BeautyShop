from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from order.forms import AddToCartForm

def indexView(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cart_form'] = AddToCartForm()
        return context