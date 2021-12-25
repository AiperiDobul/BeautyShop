from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

from account.models import User

class Category(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name





class Product(models.Model):
    CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(choices=CHOICES, max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} от бренда \"{self.brand.name}\""

class ProductReview(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Комментарий юзера {self.user.email}"