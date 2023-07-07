# Generated by Django 4.1.9 on 2023-07-07 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_storage_tabletoptionhard_storage'),
        ('cart', '0003_remove_cart_item_user_alter_cart_item_quantity_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_item_phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.checkout')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.phoneoptioncolor')),
                ('hard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.phoneoptionhard')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.phone')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart_Item',
        ),
    ]
