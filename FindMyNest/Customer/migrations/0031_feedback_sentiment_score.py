# Generated by Django 4.2.7 on 2024-02-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0030_alter_homeinteriors_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='sentiment_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
