from django.contrib import admin

# Register your models here.

## The following code is to allow admin to add products
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)