from django.contrib import admin
from django.db import models
from . models import Student_Admission

class student(admin.ModelAdmin):
    list_display=('id','student_name','parent_name','date_of_birth','email')
admin.site.register(Student_Admission,student)

