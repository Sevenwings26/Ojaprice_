from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from blogs.models import Blog

# Render Products to Templates
def index_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    # fetch recent 3 blogs  
    recent_blogs = Blog.objects.all()[:3]
    context = {
        "categories": categories,
        "products": products,
        "blogs":recent_blogs,
    }
    return render(request, "pages/index.html", context)


def product_details(request, slug):
    # product = Product.objects.get(slug=slug)
    product = get_object_or_404(Product, slug=slug)  # handles does not exist error
    context = {
        "product": product,
    }
    return render(request, "pages/product_detail.html", context)




"""
Work on the urls to use slug....
Thoughts --- 
    On click on category, display all products in category apart from the featured products: Use organi project setup to perform this....    

    combo products should be package products: hamper feels, combination of different food items....

"""
