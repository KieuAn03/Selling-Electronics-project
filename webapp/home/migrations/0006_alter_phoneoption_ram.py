# Generated by Django 4.1.9 on 2023-06-25 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_delete_product_delete_tablet_delete_watch'),
        ('home', '0005_alter_phoneoption_color_alter_phoneoption_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneoption',
            name='ram',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.phoneram'),
            preserve_default=False,
        ),
    ]
