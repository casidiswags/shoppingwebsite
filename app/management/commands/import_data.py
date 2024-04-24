import os
import csv
from django.core.management.base import BaseCommand
from app.models import Product

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **kwargs):
        csv_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', '..', 'data', 'fashion.csv')
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product_id = row['ProductId']
                # Check if product with the same product_id exists
                if not Product.objects.filter(product_id=product_id).exists():
                    product = Product(
                        product_id=product_id,
                        gender=row['Gender'],
                        category=row['Category'],
                        subcategory=row['SubCategory'],
                        product_type=row['ProductType'],
                        colour=row['Colour'],
                        usage=row['Usage'],
                        title=row['ProductTitle'],
                        image_url=row['ImageURL']
                    )
                    product.save()
                else:
                    self.stdout.write(self.style.WARNING(f"Skipping duplicate product_id: {product_id}"))
