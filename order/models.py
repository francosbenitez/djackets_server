# ## For connecting 'orders' to 'users'
# from django.contrib.auth.models import User

# from django.db import models

# ## Import the product model because the items
# ## are connected to a product
# from product.models import Product

# # Create your models here.

# class Order(models.Model):

#   ## To connect the user to the order
#   user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)

#   first_name = models.CharField(max_length=100)
#   last_name = models.CharField(max_length=100)
#   email = models.CharField(max_length=100)
#   address = models.CharField(max_length=100)
#   zipcode = models.CharField(max_length=100)
#   place = models.CharField(max_length=100)
#   phone = models.CharField(max_length=100)
#   created_at = models.DateTimeField(auto_now_add=True)
#   paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
#   stripe_token = models.CharField(max_length=100)

#   class Meta:
#     ordering = ['-created_at',]

#   ## Add a simple string representation for the object
#   def __str__(self):
#     return self.first_name

# ## We want 'OrderItem' as a separated model as well
# class OrderItem(models.Model):
#   order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#   product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
#   price = models.DecimalField(max_digits=8, decimal_places=2)
#   quantity = models.IntegerField(default=1)

#   ## The string representation, to be easier
#   ## to see in the backend, is the 'id'
#   def __str__(self):
#     return '%s' % self.id

   
from django.contrib.auth.models import User
from django.db import models

from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id