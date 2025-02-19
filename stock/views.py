from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from blogs.models import Blog

# 
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

# Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from .forms import RegistrationForm, LoginForm
# from django.contrib import messages

# # Authentication section
# def register_user(request):
#     """
#     Handling user signup
#     """
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success("Account successfully created.")
#             return redirect("/")  # home page
#     else:
#         form = RegistrationForm()
#     return render(request, "registration/register.html", {"form": form})


# def login_user(request):
#     """
#     Handling user login
#     """
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success("You are successfully logged in.")
#                 return redirect("/")  # home page
#             else:
#                 messages.error(request, "Invalid username or password.")
#     else:
#         form = LoginForm()
#     return render(request, "registration/login.html", {"form": form})


# def logout_user(request):
#     """
#     Handling user logout
#     """
#     logout(request)
#     messages.success(request, "You have been successfully logged out.")
#     return redirect("/login")  # home page

