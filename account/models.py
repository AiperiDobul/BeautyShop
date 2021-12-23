from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserManager(BaseUserManager):
    def _create(self,email, name, last_name, password, phone_number, **extra_fields):
        if not email:
            raise ValueError("Укажите свою электроную почту")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, last_name=last_name, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # creates usual users
    def create_user(self, email, name, last_name, password, phone_number, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        return self._create(email, name, last_name, password, phone_number, **extra_fields)

    # creates admin accounts
    def create_superuser(self,email, name, last_name, password, phone_number, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, name, last_name, password, phone_number, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False, region='KG')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff
    
    def create_activation_code(self):
        code = get_random_string(14)
        self.activation_code = code
        self.save()

    def send_activation_mail(self, action):
        if action.lower() == 'register':
            message = f'http://localhost:8000/account/activate/{self.activation_code}/'
        else:
            message = f'Ваш код подтверждения: {self.activation_code}'

        send_mail(
                'Активация аккаунта',
                message,
                'test@gmail.com',
                [self.email]
        )
