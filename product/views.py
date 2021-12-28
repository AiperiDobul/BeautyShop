from .forms import ProductReviewForm, CreateProductForm, UpdateProductForm
from .models import *

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.views import View

from django.shortcuts import redirect

from order.forms import AddToCartForm
from .models import Product

from django.shortcuts import render


class IndexView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/index.html'
    context_object_name = 'products'
    paginate_by = 6


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/products_list.html', context)


class ProductsListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/products_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(brand__slug=slug)
        return queryset


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cart_form'] = AddToCartForm()
        return context


class CreateProductView(CreateView):
    model = Product
    template_name = 'create.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'update.html'
    form_class = UpdateProductForm
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    pk_url_kwarg = 'product_id'
    success_url = 'home'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('home')


class AddProductReviewView(CreateView):
    model = ProductReview
    form_class = ProductReviewForm
    # fields = '__all__'
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['product_id']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


#
class SearchResultView(View):
    def get(self, request):
        queryset = None
        search_param = request.GET.get('search')
        if search_param is not None:
            queryset = Product.objects.filter(Q(name__icontains=search_param))
        return render(request, 'product/index.html', {'products': queryset})
