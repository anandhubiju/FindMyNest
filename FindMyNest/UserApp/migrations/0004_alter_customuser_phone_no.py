# Generated by Django 4.2.4 on 2023-09-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
