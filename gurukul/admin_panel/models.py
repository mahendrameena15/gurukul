from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from jsonfield import JSONField
class Student_Admission(models.Model):
    student_name = models.CharField(max_length=100,null=True,blank=True)
    parent_name = models.CharField(max_length=100,null=True,blank=True)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(unique=True,null=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    district = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    phone_number = models.CharField(max_length=10,null=True,blank=True)
    date_of_birth = models.DateField(null=True)
    class_passed_in_2023 = models.CharField(max_length=10, choices=[('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th')],null=True)
    percentage_scored = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],null=True)
    language_medium = models.CharField(max_length=20,null=True, choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Marathi', 'Marathi'), ('Bengali', 'Bengali'), ('Odia', 'Odia'), ('Other', 'Other')])
    reason_for_choice = models.TextField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.student_name
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
    
    