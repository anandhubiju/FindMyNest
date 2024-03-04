# Generated by Django 4.2.7 on 2024-02-08 03:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Customer', '0020_mortgagecalculation'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('monthly_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property_buying_city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('employment_type', models.CharField(max_length=100)),
                ('ongoing_emi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('credit_score', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Nominee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('nominee_email', models.EmailField(max_length=254)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.loanapplicant')),
            ],
        ),
    ]
