from .cart import Cart

# Create context  processor so our cart can worj on all pages   
def cart(request):
    # return the default data from cart  
    return {'cart': Cart(request)}
