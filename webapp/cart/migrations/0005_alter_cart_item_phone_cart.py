# Generated by Django 4.1.9 on 2023-07-08 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_item_phone_delete_cart_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item_phone',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
    ]
