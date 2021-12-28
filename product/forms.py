import django_filters
from django import forms

from .models import Product, ProductReview


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('user', 'product', 'text')

    widgets = {
        'user': forms.TextInput(attrs={'class': 'form-control'}),
        'product': forms.TextInput(attrs={'class': 'form-control'}),
        'text': forms.Textarea(attrs={'class': 'form-control'}),
    }


class ProductFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')

    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    category__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'price', 'brand']