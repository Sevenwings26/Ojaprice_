from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index"),
    path("product/<slug:slug>/", views.product_details, name="product_details"),
    # path("update_cart/", views.updateItem, name="update_cart"),

    # carting operations
    path('cart/', views.cart_summary, name="cart_summary"),
    path('cart_add/', views.cart_add, name="cart_add"),
]

