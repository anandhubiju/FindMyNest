# Generated by Django 4.2.4 on 2023-09-15 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0016_delete_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='city',
            new_name='Twon',
        ),
    ]
