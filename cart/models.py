from django.db import models
from user.models import CustomerUser
from product.models import Product
# Create your models here.
# Create your models here.
class Cart(models.Model):
    userID = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cartID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    itemID = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)