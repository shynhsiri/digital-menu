# Generated by Django 5.0.4 on 2024-04-15 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_product_description_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
