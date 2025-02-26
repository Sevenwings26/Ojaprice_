from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=256, blank=True, null=True, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    star_count = [
        (1, "One"),
        (2, "Two"),
        (3, "Three"),
        (4, "Four"),
        (5, "Five"),
    ]
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to="product_img/")
    rating_count = models.IntegerField(choices=star_count, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} sold at {self.price} per unit"


