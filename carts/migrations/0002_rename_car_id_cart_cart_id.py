# Generated by Django 4.1.7 on 2023-03-25 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='car_id',
            new_name='cart_id',
        ),
    ]
