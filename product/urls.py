from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<int:pk>/', ProductDetailsView.as_view(), name='product-details'),
]