# Generated by Django 4.1.7 on 2023-04-12 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='createed_at',
            new_name='created_at',
        ),
    ]