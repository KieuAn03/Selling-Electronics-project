# Generated by Django 4.1.9 on 2023-06-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='image0',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='image1',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='image2',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image0',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image1',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image2',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='image0',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='image1',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='image2',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='image0',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='image1',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='image2',
            field=models.ImageField(upload_to='products/'),
        ),
    ]