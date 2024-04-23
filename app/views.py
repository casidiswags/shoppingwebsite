from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product

import random  # Importing random for generating random prices

def index_view(request):
    # Fetch 16 products to display on the homepage
    products = Product.objects.all()[:16]
    for product in products:
        # Generate random price for each product in pounds
        product.price = round(random.uniform(5, 7), 2)
    return render(request, 'index.html', {'products': products})

def product_list(request):
    products = Product.objects.all()  # Retrieve all products from the database
    # Add quantity of each product in the cart
    for product in products:
        product.quantity_in_cart = get_quantity_in_cart(product.id)  # Implement this function to get the quantity in cart
    return render(request, 'product_list.html', {'products': products})

def cart_view(request):
    # Assuming you have fetched cart items
    cart_items = get_cart_items(request)
    
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    
    return render(request, 'cart.html', {'cart_items': cart_items})

def register_view(request):
    # Implement logic for registering users
    return render(request, 'register.html')

def login_view(request):
    # Implement logic for user login
    return render(request, 'login.html')

def product_search(request):
    query = request.GET.get('query')  # Get the search query from the GET parameters
    if query:
        # Filter products based on the search query
        products_list = Product.objects.filter(title__icontains=query)
    else:
        products_list = Product.objects.all()  # If no query, display all products

    paginator = Paginator(products_list, 30)  # Show 30 products per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'product_search_results.html', {'products': products})

def get_quantity_in_cart(product_id):
    # Implement logic to get the quantity of a product in the cart
    return 0  # Placeholder, replace with actual implementation

def get_cart_items(request):
    # Implement logic to fetch cart items from the database based on the user's session or other criteria
    # Replace this with your actual implementation
    return []

def checkout_view(request):
    # Implement logic for the checkout page
    return render(request, 'checkout.html')
