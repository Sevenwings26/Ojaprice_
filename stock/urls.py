from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index"),
    path("product/<slug:slug>/", views.product_details, name="product_details"),
]

