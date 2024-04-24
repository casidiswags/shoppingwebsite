from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    gender = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    usage = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    image_url = models.URLField()

    def __str__(self):
        return self.title

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        if self.user:
            return f"{self.quantity} of {self.product.title} in {self.user}'s cart"
        else:
            return f"{self.quantity} of {self.product.title} in session {self.session_id}"
