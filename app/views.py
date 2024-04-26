from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, CartItem
from django.http import JsonResponse
import random  # Importing random for generating random prices

def index_view(request):
    # Fetch 16 products to display on the homepage
    products = Product.objects.all()[:30]
    for product in products:
        # Generate random price for each product in pounds
        product.price = round(random.uniform(5, 7), 2)
    return render(request, 'index.html', {'products': products})

def product_list(request):
    products = Product.objects.all()  # Retrieve all products from the database
    # Add quantity of each product in the cart
    for product in products:
        product.quantity_in_cart = get_quantity_in_cart(request, product.id)
    return render(request, 'product_list.html', {'products': products})

def cart_view(request):
    # Fetch cart items associated with the user's session
    cart_items = get_cart_items(request)
    
    total_price = 0  # Initialize total price
    
    # Calculate the total price for each item in the cart
    for item in cart_items:
        # Retrieve the product associated with the cart item
        product = item.product
        # Check if the product exists and has a price attribute
        if product and hasattr(product, 'price'):
            item.total_price = product.price * item.quantity
            total_price += item.total_price  # Accumulate total price
        else:
            # If the product or price attribute is missing, set the total price to 0
            item.total_price = 0
    
    # Render the cart page with cart items and total price
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def calculate_total_price(cart_items):
    """
    Calculate the total price for all items in the cart.
    """
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.quantity
    return total_price

def add_to_cart(request, product_id):
    # Retrieve the product object
    product = get_object_or_404(Product, id=product_id)
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product
        )
    else:
        # If user is not authenticated, use session ID
        session_id = request.session.session_key
        cart_item, created = CartItem.objects.get_or_create(
            session_id=session_id,
            product=product
        )
    
    # Increment quantity if the item is already in the cart
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    # Count total items in the cart
    total_items_in_cart = get_cart_items_count(request)
    
    # Return JSON response with updated cart item count
    return JsonResponse({'cartItemCount': total_items_in_cart})

def remove_from_cart(request, item_id):
    # Retrieve the cart item
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    # Check if the cart item belongs to the current user or session
    if cart_item.user == request.user or cart_item.session_id == request.session.session_key:
        cart_item.delete()  # Delete the cart item
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

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

def get_quantity_in_cart(request, product_id):
    # Implement logic to get the quantity of a product in the cart
    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(product_id=product_id, user=request.user).first()
    else:
        cart_item = CartItem.objects.filter(product_id=product_id, session_id=request.session.session_key).first()
    if cart_item:
        return cart_item.quantity
    return 0

def get_cart_items(request):
    # Fetch cart items associated with the user's session
    if request.user.is_authenticated:
        return CartItem.objects.filter(user=request.user)
    else:
        session_key = request.session.session_key
        return CartItem.objects.filter(session_id=session_key)

def get_cart_items_count(request):
    # Fetch cart items count associated with the user's session
    if request.user.is_authenticated:
        return CartItem.objects.filter(user=request.user).count()
    else:
        session_key = request.session.session_key
        return CartItem.objects.filter(session_id=session_key).count()

def checkout_view(request):
    # Fetch cart items associated with the user's session
    cart_items = get_cart_items(request)
    
    total_price = 0  # Initialize total price
    
    # Calculate the total price for each item in the cart
    for item in cart_items:
        # Retrieve the product associated with the cart item
        product = item.product
        # Check if the product exists and has a price attribute
        if product and hasattr(product, 'price'):
            item.total_price = product.price * item.quantity
            total_price += item.total_price  # Accumulate total price
        else:
            # If the product or price attribute is missing, set the total price to 0
            item.total_price = 0
    
    if total_price == 0:  # If cart is empty
        return render(request, 'cart_empty.html')  # Render cart empty page
    else:
        return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})

def purchase_view(request):
    # Implement logic for the purchase page
    return render(request, 'purchase.html')

