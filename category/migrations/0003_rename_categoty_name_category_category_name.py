# Generated by Django 4.1.7 on 2023-03-19 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoty_name',
            new_name='category_name',
        ),
    ]
