from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register/success/', SuccessfulRegistration.as_view(), name='register-success'),
    path('activate/<str:code>/', ActivationView.as_view(), name='activate'),
    path('sign_in/', SignInView.as_view(), name='sign-in'),
    path('logout/', LogoutView.as_view(), name='logout'),
]