# Generated by Django 4.1.7 on 2023-04-15 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]