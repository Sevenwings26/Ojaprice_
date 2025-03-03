from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Product
from blogs.models import Blog
import json
# from .models import Order, OrderItem
# from .utils import cartData

# Render Products to Templates
def index_page(request):
    # data = cartData(request)
    # cartItems = data["cartItems"]
    # items = data["items"]
    # order = data["order"]

    categories = Category.objects.all()
    products = Product.objects.all()

    # fetch recent 3 blogs  
    recent_blogs = Blog.objects.all()[:3]
    context = {
        "categories": categories,
        "products": products,
        "blogs":recent_blogs,

        # "cartItems":cartItems,
    }
    return render(request, "pages/index.html", context)


def product_details(request, slug):
    # product = Product.objects.get(slug=slug)
    product = get_object_or_404(Product, slug=slug)  # handles does not exist error
    context = {
        "product": product,
    }
    return render(request, "pages/product_detail.html", context)


from .cart import Cart
from .models import Product
from django.http import JsonResponse

# def cart_add(request):
#     # get the cart   
#     cart = Cart(request)
#     # test post 
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('product_id'))
#         product = get_object_or_404(Product, id=product_id)
#         # Save to Session
#         cart.add(product=product)  


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity', 1))  # Ensure quantity is an integer
        product = get_object_or_404(Product, id=product_id)
        
        # Add product to cart
        cart.add(product=product, quantity=quantity)  

        # Get total cart quantity
        cart_quantity = sum(item['quantity'] for item in cart.cart.values())

        # Return JSON response including updated cart quantity
        response = JsonResponse({
            "Product name": product.name,
            "Product price": str(product.price),
            "Product ID": product.id,
            "Quantity": quantity,
            "cart_quantity": cart_quantity,  # Include total cart quantity
        })
        return response



def cart_update(request):
    pass

def cart_delete(request):
    pass

def cart_summary(request):
    return render(request, "pages/products/cart_summary.html")


def checkout(request):
    pass

# To add to cart
# def updateItem(request):
#     # data sent from the frontend
#     data = json.loads(request.body)
#     productId = data["productId"]
#     action = data["action"]
#     print("ProductId", productId)
#     print("Action", action)

#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)

#     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

#     if action == "add":
#         orderItem.quantity += 1
#     elif action == "remove":
#         orderItem.quantity -= 1
#     orderItem.save()

#     if orderItem.quantity <= 0:
#         orderItem.delete()

#     return JsonResponse("Item was added", safe=False)

# from .models import Product
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from .cart import Cart

# def updateItem(request):
#     # Get the cart 
#     cart = Cart(request)
#     # test post
#     if request.POST.get('action') == 'post':
#         # Get stuff
#         product_id = int(request.POST.get('product_id'))
#         # lookup produc in DB 
#         product = get_object_or_404(Product, id=product_id)

#         cart.add(product=product)

#         response = JsonResponse({'Product Name': product})
#         return response
        

    # data = json.loads(request.body)
    # productId = data["productId"]
    # action = data["action"]
    # print("ProductId", productId)
    # print("Action", action)

    # customer = request.user.customer
    # product = Product.objects.get(id=productId)
    # order, created = Order.objects.get_or_create(customer=customer, complete=False)

    # orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    # if action == "add":
    #     orderItem.quantity += 1
    # elif action == "remove":
    #     orderItem.quantity -= 1
    # orderItem.save()

    # if orderItem.quantity <= 0:
    #     orderItem.delete()

    # return JsonResponse("Item was added", safe=False)

"""
Work on the urls to use slug....
Thoughts --- 
    On click on category, display all products in category apart from the featured products: Use organi project setup to perform this....    

    combo products should be package products: hamper feels, combination of different food items....

"""
