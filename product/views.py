from django.shortcuts import render

from .models import *
from django.views.generic.detail import DetailView
from order.forms import AddToCartForm
from django.views.generic import ListView
from django.views import View
from django.db.models import Q


class IndexView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/index.html'
    context_object_name = 'products'
    paginate_by = 6


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cart_form'] = AddToCartForm()
        return context


#
class SearchResultView(View):
    def get(self, request):
        queryset = None
        search_param = request.GET.get('search')
        if search_param is not None:
            queryset = Product.objects.filter(Q(name__icontains=search_param))
        return render(request, 'product/index.html', {'products': queryset})
