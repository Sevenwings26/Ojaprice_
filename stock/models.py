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
            self.slug = Slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} sold at {self.price} per unit"

    
    
    
    
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ""
    #     return url


# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


# class Order(models.Model):
#     customer = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True, blank=True
#     )
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, null=True, blank=True)
#     transaction_id = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return str(self.id)

#     # # to hide the shipping address if product is digital product
#     # @property
#     # def shipping(self):
#     #     shipping = False
#     #     orderitems = self.orderitem_set.all()
#     #     for i in orderitems:
#     #         if i.product.digital == False:
#     #             shipping = True
#     #     return shipping

#     # @property
#     # def get_cart_total(self):
#     #     orderitems = self.orderitem_set.all()
#     #     total = sum([item.get_total for item in orderitems])
#     #     return total

#     # @property
#     # def get_cart_items(self):
#     #     orderitems = self.orderitem_set.all()
#     #     total = sum([item.quantity for item in orderitems])
#     #     return total


# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     @property
#     def get_total(self):
#         total = self.quantity * self.product.price
#         return total


# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     address = models.CharField(max_length=200, null=False)
#     city = models.CharField(max_length=200, null=False)
#     state = models.CharField(max_length=200, null=False)
#     zipcode = models.CharField(max_length=200, null=False)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.address
