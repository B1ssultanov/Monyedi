# Generated by Django 4.1.7 on 2023-03-08 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_computers_headphones_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computers',
            options={'verbose_name': 'Computer', 'verbose_name_plural': 'Computers'},
        ),
        migrations.AlterModelOptions(
            name='headphones',
            options={'verbose_name': 'Headphone', 'verbose_name_plural': 'Headphones'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]