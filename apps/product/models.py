from datetime import datetime

from django.db import models
from apps.user.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.name}, {self.id}'


class BasketItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)