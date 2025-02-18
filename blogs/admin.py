from django.contrib import admin
from . models import Category, Blog

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = [
    #     'id',
    #     'name',
    # ]

    def has_add_permission(self, request):
        return True
        # return super().has_add_permission(request)


admin.site.register(Blog)
# class ProductAdmin()