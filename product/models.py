from unicodedata import category
from django.db import models

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


# Create your models here.
class Product(models.Model):
    title = models.CharField(default='', max_length=50)
    price = models.FloatField(default=0)
    discount_price = models.FloatField(default=0)
    description = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    image = models.ImageField()
    
