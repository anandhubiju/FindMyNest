# Generated by Django 4.2.4 on 2023-10-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0016_property_tax_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bathrooms_attached',
            field=models.CharField(blank=True, choices=[('', 'Select an option'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('More than 5', 'More than 5')], max_length=40, null=True),
        ),
    ]
