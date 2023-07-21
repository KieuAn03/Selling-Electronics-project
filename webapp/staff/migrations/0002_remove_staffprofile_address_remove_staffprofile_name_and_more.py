# Generated by Django 4.2.1 on 2023-07-20 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_is_admin_profile_is_customer_and_more'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='id_profile',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
            preserve_default=False,
        ),
    ]
