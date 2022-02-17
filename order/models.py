from django.db import models
from user.models import CustomerUser
from cart.models import Cart

# Create your models here.
# Create your models here.
class Order(models.Model):
    userID = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cartID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(default='', max_length=50)
    description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)