# Generated by Django 4.2.7 on 2024-02-22 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0026_property_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Customer'), (2, 'Admin'), (4, 'Executive')], default=1),
        ),
    ]
