from django.test import TestCase
from django.urls import reverse
from .models import Product, CartItem
from django.contrib.auth.models import User


class CartTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(
            product_id=1,
            title="Test Product",
            price=10.0,
            image_url="test_image_url.jpg"
        )
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=2)

    def test_add_to_cart(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_to_cart'), {'product_id': self.product.id, 'quantity': 2})
        self.assertEqual(response.status_code, 302)  # Redirects after adding to cart
        self.assertTrue(CartItem.objects.filter(user=self.user, product=self.product, quantity=2).exists())

    def test_remove_from_cart(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('remove_from_cart', kwargs={'item_id': self.cart_item.id}))
        self.assertEqual(response.status_code, 302)  # Redirects after removing from cart
        self.assertFalse(CartItem.objects.filter(user=self.user, product=self.product).exists())
