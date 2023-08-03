from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from jsonfield import JSONField
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField

class Student_Admission(models.Model):
    student_name = models.CharField(max_length=100,default="")
    parent_name = models.CharField(max_length=100,default="")
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(unique=True,null=True)
    state = models.CharField(max_length=100,default="")
    district = models.CharField(max_length=100,default="")
    address = models.CharField(max_length=200,default="")
    phone_number = models.CharField(max_length=10,default="")
    date_of_birth = models.DateField(null=True)
    class_passed_in_2023 = models.CharField(max_length=10, choices=[('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th')],null=True)
    # percentage_scored = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],null=True)
    percentage_scored = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        help_text=""
    )
    language_medium = models.CharField(max_length=20,null=True, choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Marathi', 'Marathi'), ('Bengali', 'Bengali'), ('Odia', 'Odia'), ('Other', 'Other')])
    reason_for_choice = models.TextField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.student_name

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    COURSES = [
        ('Category 1', 'Category 1'),
        ('Category 2', 'Category 2'),
        ('Category 3', 'Category 3'),
    ]

    courses = models.CharField(max_length=10,null=True,choices=COURSES)
    title = models.CharField(max_length=100,default="")
    author = models.CharField(max_length=100,default="")
    picture = models.ImageField(upload_to ='images/',default='null')
    description = models.TextField(max_length=200,default="") 
    meta = models.TextField(max_length=160,default='null',blank=True)
   
    
    def __str__(self):
        return self.author

class Course_Seo(models.Model):
    meta_title=models.CharField(max_length=100,default="")
    meta_description=models.CharField(max_length=200,default="")
    meta_keywords=models.TextField(default="")


# class Users(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=8)
#     phone = models.CharField(max_length=15)
#     status = models.BooleanField()
#     meta = models.TextField(blank=True, null=True)
#     role = models.CharField(max_length=20)
#     meta = JSONField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']
    
class Category_Seo(models.Model):
    meta_title=models.CharField(max_length=100,default="")