from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView, name='index'),
    path('<int:pk>/', ProductDetailsView.as_view(), name='product-details'),
]