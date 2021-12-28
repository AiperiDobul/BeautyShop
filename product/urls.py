from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<int:pk>/', ProductDetailsView.as_view(), name='product-details'),
    path('search/', SearchResultView.as_view(), name='search'),
    path('create/', CreateProductView.as_view(), name='create'),
    path('<int:id>/update/', UpdateProductView.as_view(), name='product-update'),
    path('<int:id>/delete/', DeleteProductView.as_view(), name='delete'),
]
