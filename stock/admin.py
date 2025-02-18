from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product

# Register your models here.
admin.site.register(Category)
# admin.site.register(models.Customer)
# admin.site.register(models.Order)
# admin.site.register(models.OrderItem)
# admin.site.register(models.ShippingAddress)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "price",
    ]
