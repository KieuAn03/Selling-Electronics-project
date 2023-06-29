# Generated by Django 4.1.9 on 2023-06-29 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_delete_product_delete_tablet_delete_watch'),
        ('home', '0010_phoneoptionhard_remove_phoneoptionstorage_phone_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabletOptionHard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_add', models.IntegerField(blank=True, null=True)),
                ('Tablet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tablet')),
                ('ram', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletram')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tabletstorage')),
            ],
        ),
        migrations.RemoveField(
            model_name='tabletoptionstorage',
            name='Tablet_id',
        ),
        migrations.RemoveField(
            model_name='tabletoptionstorage',
            name='storage',
        ),
        migrations.AlterField(
            model_name='phoneoptionhard',
            name='Storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.phonestorage'),
        ),
        migrations.AlterField(
            model_name='phoneoptionhard',
            name='ram',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.phoneram'),
        ),
        migrations.DeleteModel(
            name='TabletOptionRam',
        ),
        migrations.DeleteModel(
            name='TabletOptionStorage',
        ),
    ]
