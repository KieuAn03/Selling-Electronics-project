# Generated by Django 4.1.9 on 2023-07-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_info',
            name='Email',
        ),
        migrations.AlterField(
            model_name='cart_info',
            name='Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cart_info',
            name='Phone_num',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
