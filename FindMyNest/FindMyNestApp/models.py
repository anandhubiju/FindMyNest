from django.db import models
from UserApp.models import CustomUser,UserProfile
from Customer.models import Property

# Create your models here.

VALIDITY_CHOICES = [
        ('1 MONTH', '1 MONTH'),
        ('2 MONTH', '2 MONTH'),
        ('3 MONTH', '3 MONTH'),
        ('4 MONTH', '4 MONTH'),
        ('5 MONTH', '5 MONTH'),
        ('6 MONTH', '6 MONTH'),
        ('7 MONTH', '7 MONTH'),
        ('8 MONTH', '8 MONTH'),
        ('9 MONTH', '9 MONTH'),
        ('10 MONTH', '10 MONTH'),
        ('11 MONTH', '11 MONTH'),
        ('12 MONTH', '12 MONTH'),
    ]

class Subscription(models.Model):  
    sub_type = models.CharField(max_length=40, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    validity = models.CharField(max_length=40, choices=VALIDITY_CHOICES, blank=True, null=True) 
    features = models.CharField(max_length=255 , blank=True, null=True) 

    def __str__(self):
        return f"{self.sub_type} Subscription"
    
    

