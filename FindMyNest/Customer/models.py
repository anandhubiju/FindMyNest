from django.db import models
from UserApp.models import CustomUser,UserProfile

# Create your models here.



class Property(models.Model):
    
    STATE_CHOICES = [
        ('', 'Select an option'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    ]
    
    TYPE_CHOICES = [
        ('', 'Select an option'),
        ('House', 'Houses'),
        ('Apartment', 'Apartment'),
        ('Villa', 'Villas'),
        ('Commercial', 'Commercial'),
        ('Garage', 'Garage'),
    ]
    
    TAX_CHOICE =[
        ('', 'Select an option'),
        ('Included', 'Included'),
        ('Not Included', 'Not Included'),
       ]
    
    STATUS_CHOICES = [
        ('', 'Select an option'),
        ('For Sale', 'For Sale'),
    ]
    
    BEDROOM_CHOICES = [
        ('', 'Select an option'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('More than 5', 'More than 5'),
    ]
    
    BATHROOM_CHOICES = [
        ('', 'Select an option'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('More than 5', 'More than 5'),
    ]
    
    FLOOR_CHOICES = [
        ('', 'Select an option'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    ]
    
    AFLOOR_CHOICES = [
    ('', 'Select an option'),
    ('0', 'Ground Floor'),
    ('1', '1 Floor'),
    ('2', '2 Floor'),
    ('3', '3 Floor'),
    ('4', '4 Floor'),
    ('5', '5 Floor'),
    ('6', '6 Floor'),
    ('7', '7 Floor'),
    ('8', '8 Floor'),
    ('9', '9 Floor'),
    ('10', '10 Floor'),
    ('11', '11 Floor'),
    ('12', '12 Floor'),
    ('13', '13 Floor'),
    ('14', '14 Floor'),
    ('15', '15 Floor'),
    ('16', '16 Floor'),
    ('17', '17 Floor'),
    ('18', '18 Floor'),
    ('19', '19 Floor'),
    ('20', '20 Floor'),
    ('21', '21 Floor'),
    ('22', '22 Floor'),
    ('23', '23 Floor'),
    ('24', '24 Floor'),
    ('25', '25 Floor'),
    ('26', '26 Floor'),
    ('27', '27 Floor'),
    ('28', '28 Floor'),
    ('29', '29 Floor'),
    ('30', '30 Floor'),
    ('31', '31 Floor'),
    ('32', '32 Floor'),
    ('33', '33 Floor'),
    ('34', '34 Floor'),
    ('35', '35 Floor'),
    ('36', '36 Floor'),
    ('37', '37 Floor'),
    ('38', '38 Floor'),
    ('39', '39 Floor'),
    ('40', '40 Floor'),
    ('41', '41 Floor'),
    ('42', '42 Floor'),
    ('43', '43 Floor'),
    ('44', '44 Floor'),
    ('45', '45 Floor'),
    ('46', '46 Floor'),
    ('47', '47 Floor'),
    ('48', '48 Floor'),
    ('49', '49 Floor'),
    ('50', '50 Floor'),
    ('51', '51 Floor'),
    ('52', '52 Floor'),
    ('53', '53 Floor'),
    ('54', '54 Floor'),
    ('55', '55 Floor'),
    ('56', '56 Floor'),
    ('57', '57 Floor'),
    ('58', '58 Floor'),
    ('59', '59 Floor'),
    ('60', '60 Floor'),
    ('61', '61 Floor'),
    ('62', '62 Floor'),
    ('63', '63 Floor'),
    ('64', '64 Floor'),
    ('65', '65 Floor'),
    ('66', '66 Floor'),
    ('67', '67 Floor'),
    ('68', '68 Floor'),
    ('69', '69 Floor'),
    ('70', '70 Floor'),
    ('71', '71 Floor'),
    ('72', '72 Floor'),
    ('73', '73 Floor'),
    ('74', '74 Floor'),
    ('75', '75 Floor'),
    ('76', '76 Floor'),
    ('77', '77 Floor'),
    ('78', '78 Floor'),
    ('79', '79 Floor'),
    ('80', '80 Floor'),
    ('81', '81 Floor'),
    ('82', '82 Floor'),
    ('83', '83 Floor'),
    ('84', '84 Floor'),
    ('85', '85 Floor'),
    ('86', '86 Floor'),
    ('87', '87 Floor'),
    ('88', '88 Floor'),
    ('89', '89 Floor'),
    ('90', '90 Floor'),
]


    
    
    
    AGE_CHOICES = [
        ('', 'Select an option'),
        ('0-1', '0-1'),
        ('2-5 ', '2-5'),
        ('6-10', '6-10'),
        ('11-15', '11-15'),
        ('16-20', '16-20'),
        ('More than 10 Years', 'More than 10 Years')
    ]
    
    RENOVATED_CHOICES = [
        ('', 'Select an option'),
        ('Not Yet Renovated', 'Not Yet Renovated'),
        ('1-5', '1-5 Year Before'),
        ('5-10', '5-10'),
        ('More than 10 Years Before', 'More than 10 Years Before')
    ]
    
    KM_CHOICES = [
        ('', 'Select an option'),
        ('0-1', '0-1'),
        ('2-5', '2-5'),
        ('6-10', '6-10'),
        ('11-15', '11-15'),
        ('16-20', '16-20'),
        ('More than 10 Kilometer', 'More than 10 Kilometer')
    ]
    
    GARAGE_CHOICES = [
        ('', 'Select an option'),
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('More than 2', 'More than 2')
        
    ]
    
    ROOM_CHOICES = [
        ('', 'Select an option'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('More than 8', 'More than 8'),
    ]
    
    FEATURES_CHOICES = [
    ('Air Condition', 'Air Condition'),
    ('Playing Area', 'Playing Area'),
    ('Well(Water Availability)', 'Well(Water Availability)'),
    ('Balcony ', 'Balcony '),
    ('Parking', 'Parking'),
    ('Concrete Flooring', 'Concrete Flooring'),
    ('Garden', 'Garden'),
    ('Internet ', 'Internet'),
    ('Furnished', 'Furnished'),
    ('Fireplace', 'Fireplace'),
    ('Security System', 'Security System'),
]
    PLACE_CHOICES = [
    ('Schools', 'Schools'),
    ('Hospitals Facilities', 'Hospitals Facilities'),
    ('Well(Water Availability)', 'Well(Water Availability)'),
    ('Shopping Centers', 'Shopping Centers'),
    ('Public Transportation', 'Public Transportation'),
    ('Restaurants and Dining', 'Restaurants and Dining'),
    ('Fitness Centers', 'Fitness Centers'),
    ('Major Roads and Highways', 'Major Roads and Highways'),
    ('Employment Centers', 'Employment Centers'),
    ('Beach', 'Beach:'),
    ('Shopping Complex', 'Shopping Complex'),
     ('Parks', 'Parks'),
    ('Transportation Hubs', 'Transportation Hubs'),
    ('Cinema Centers', 'Cinema Centers'),

]
    
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    thumbnail = models.FileField(upload_to='thumbnail/')
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    owner_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    Town = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    description = models.CharField(max_length=500)
    floor_plan = models.FileField(upload_to='floorplan/', default='',null=True, blank=True)
    whatsapp_no = models.IntegerField()
    nearby_place = models.CharField(max_length=255, default='',null=True, blank=True)
    features = models.CharField(max_length=255,default='',)
    price = models.IntegerField()
    area = models.CharField(max_length=100)
    property_type = models.CharField(max_length=40, choices=TYPE_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, blank=True, null=True)
    bedrooms = models.CharField(max_length=40, choices=BEDROOM_CHOICES, blank=True, null=True)
    bathrooms = models.CharField(max_length=40, choices=BATHROOM_CHOICES, blank=True, null=True)
    bathrooms_attached = models.CharField(max_length=40, choices=BATHROOM_CHOICES, blank=True, null=True)
    rooms = models.CharField(max_length=40, choices=ROOM_CHOICES, blank=True, null=True)
    state = models.CharField(max_length=40, choices=STATE_CHOICES, blank=True, null=True)
    garage = models.CharField(max_length=40, choices=GARAGE_CHOICES, blank=True, null=True)
    major_road = models.CharField(max_length=40, choices=KM_CHOICES, blank=True, null=True)
    near_hospital = models.CharField(max_length=40, choices=KM_CHOICES, blank=True, null=True,)
    near_supermarket = models.CharField(max_length=40, choices=KM_CHOICES, blank=True, null=True)
    bulding_age = models.CharField(max_length=40, choices=AGE_CHOICES, blank=True, null=True)
    floor = models.CharField(max_length=40, choices=FLOOR_CHOICES, blank=True, null=True)
    floor_no = models.CharField(max_length=40, choices=AFLOOR_CHOICES, blank=True, null=True)
    last_renovated = models.CharField(max_length=40, choices=RENOVATED_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    days_to_sell = models.PositiveIntegerField(default=0)
    property_tips = models.TextField(default='')
    sale_duration_tips = models.TextField(default='')
    tax_status= models.CharField(max_length=40, choices=TAX_CHOICE, blank=True, null=True)
    

    def __str__(self):
        return f"Property ID {self.pk}"

    


class Image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='property_images/', blank=True)  

    def __str__(self):
        return f"Image for {self.property.owner_name}" 
    
class PropertyView(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Feedback(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_feedbacks', blank=True)

    def __str__(self):
        return self.first_name
    
class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'property')

    def __str__(self):
        return f'{self.user.username} - {self.property.address}'

    
