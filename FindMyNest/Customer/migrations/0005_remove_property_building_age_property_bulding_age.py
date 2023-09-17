# Generated by Django 4.2.4 on 2023-09-08 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_remove_property_bulding_age_property_building_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='building_age',
        ),
        migrations.AddField(
            model_name='property',
            name='bulding_age',
            field=models.CharField(blank=True, choices=[('Less than one year', 'Less than one year'), ('1-5 Year', '1-5 Year'), ('5-10 Years', '5-10 Years'), ('More than 10 Years', 'More than 10 Years')], max_length=40, null=True, verbose_name='Select Type'),
        ),
    ]
