from audioop import reverse
from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from itertools import product
from operator import mod
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

from Accounts.models import CustomUser


# class CustomDateTimeField(models.DateTimeField):
#     def value_to_string(self, obj):
#         val = self.value_from_object(obj)
#         if val:
#             val.replace(microsecond=0)
#             return val.isoformat()
#         return ''


class Category(models.Model):
    name = models.CharField(max_length = 255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('priceBetaApp:category_list', args=[self.slug])


class Store(models.Model):
    name = models.CharField(max_length=225, db_index=True)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'stores'

    def __str__(self):
        return self.name



store_cat = models.ForeignKey(Store, related_name='product', on_delete=models.CASCADE, default='store name', blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length = 255, db_index=True)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    image_url = models.CharField(max_length = 250, null=True)
    image = models.ImageField(upload_to='product_images', default='null')
    brand = models.CharField(max_length = 100)
    store1 = models.ForeignKey(Store, related_name='store1-product+', on_delete=models.CASCADE, default=None, blank=True, null=True)
    store1_price = models.DecimalField(max_digits=100, decimal_places=2)
    store1_url = models.CharField(max_length = 250, null=True)
    store2 = models.ForeignKey(Store, related_name='store2-product+', on_delete=models.CASCADE, default=None, blank=True, null=True)
    store2_price = models.DecimalField(max_digits=100, decimal_places=2)
    store2_url = models.CharField(max_length = 250, null=True)
    store3 = models.ForeignKey(Store, related_name='store3-product+', on_delete=models.CASCADE, default=None, blank=True, null=True)
    store3_price = models.DecimalField(max_digits=100, decimal_places=2)
    store3_url = models.CharField(max_length = 250, null=True)
    best_price = models.DecimalField(max_digits=100, decimal_places=2)
    rating = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, default='slug')
    in_stock = models.BooleanField(default=True)

    
        
        

    class Meta:
        verbose_name_plural = 'products'
        # ordering = ('-created')

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    wishlist_name = models.CharField(max_length=255, db_index=True)
# <<<<<<< Updated upstream
    user = models.ForeignKey(CustomUser, related_name='wishlist', on_delete=models.CASCADE)
# =======
    # user = models.ForeignKey(User, related_name='wishlist', on_delete=models.CASCADE)
# >>>>>>> Stashed changes
    item = models.ForeignKey(Product, related_name='wishlist', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name_plural = 'wishlists'

    def __str__(self):
        return self.wishlist_name
