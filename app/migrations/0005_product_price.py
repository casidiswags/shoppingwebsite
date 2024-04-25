# Generated by Django 4.1.2 on 2024-04-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_cartitem_id_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10),
            preserve_default=False,
        ),
    ]