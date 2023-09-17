# Generated by Django 4.2.4 on 2023-09-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0008_alter_image_images_alter_property_bathrooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='features',
            field=models.CharField(blank=True, choices=[('Air Condition', 'Air Condition'), ('Playing Area', 'Playing Area')], max_length=255),
        ),
    ]
