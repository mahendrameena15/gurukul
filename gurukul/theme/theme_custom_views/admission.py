from django.shortcuts import render,redirect
from theme.forms import AdmissionForm
import random,string
from admin_panel.models import Student_Admission
from django.http import HttpResponse
from datetime import datetime
def admission_form(request): 
    if request.method == "POST":    
        form = AdmissionForm(request.POST)
        if form.is_valid():    
            student = Student_Admission(
                student_name=form.cleaned_data['student_name'],
                parent_name=form.cleaned_data['parent_name'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                email=form.cleaned_data['email'],
                state=form.cleaned_data['state'],
                district=form.cleaned_data['district'],
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number'],
                class_passed_in_2023=form.cleaned_data['class_passed_in_2023'],
                percentage_scored=form.cleaned_data['percentage_scored'],
                language_medium=form.cleaned_data['language_medium'],
                reason_for_choice=form.cleaned_data['reason_for_choice']
            )
            student.save()
            return render(request,'thankyou.html',{'data':student})      
        else:
           return render(request, 'admission-form.html', {'form': form, 'form_errors': form.errors}) 
    else:  
        form=AdmissionForm() 
        page_title = "Admission Form"
        context = {'page_title':page_title} 
        return render(request, 'admission-form.html', context)