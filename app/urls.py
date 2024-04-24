from django.urls import path
from .views import index_view, product_list, cart_view, register_view, login_view, product_search, checkout_view, add_to_cart  # Import the add_to_cart view function

urlpatterns = [
    path('', index_view, name='index'),  # URL pattern for the root URL
    path('products/', product_list, name='product_list'),
    path('cart/', cart_view, name='cart'),  # URL pattern for the cart page
    path('register/', register_view, name='register'),  # URL pattern for the register page
    path('login/', login_view, name='login'),  # URL pattern for the login page
    path('search/', product_search, name='product_search'),  # URL pattern for product search
    path('checkout/', checkout_view, name='checkout'),  # URL pattern for the checkout page
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart')

    # Add more URL patterns as needed
]
