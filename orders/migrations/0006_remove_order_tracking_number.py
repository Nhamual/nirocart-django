# Generated by Django 4.1.7 on 2023-05-10 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_tracking_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tracking_number',
        ),
    ]
