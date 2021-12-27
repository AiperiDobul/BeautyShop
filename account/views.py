from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from .forms import *
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

class RegisterView(View):
    form_class = RegistrationForm
    template_name = 'account/registration.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('register-success'))
        return render(request, self.template_name, {'form': form})


class ActivationView(View):
    def get(self, request, *args, **kwargs):
        code = kwargs.get('code')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html')


class SuccessfulRegistration(TemplateView):
    template_name = 'account/successful_registration.html'


class SignInView(LoginView):
    template_name = 'account/sign_in.html'