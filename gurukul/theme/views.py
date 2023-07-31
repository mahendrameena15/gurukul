from django.shortcuts import render,redirect
from .forms import ContactForm
import phonenumbers
from django.contrib import messages
import random,string
from django.http import HttpResponse
from admin_panel.models import Student_Admission,ContactMessage
def home(request):
    page_title = "Home"
    context = {'page_title':page_title}
    return render(request, 'home.html', context)
def about_us(request):
    page_title = "About Us"
    context = {'page_title':page_title}
    return render(request, 'about.html', context)
def contact_us(request):
    page_title = "Contact Us"
    context = {'page_title':page_title}
    return render(request, 'contact-us.html', context)
def admission_form(request):
    page_title = "Admission Form"
    context = {'page_title':page_title}
    return render(request, 'admission-form.html', context)
def gallery(request):
    page_title = "Gallery"
    context = {'page_title':page_title}
    return render(request, 'gallery.html', context)
def about_admission(request):
    page_title = "About-Admission"
    context = {'page_title':page_title}
    return render(request, 'admission.html', context)
def student_life(request):
    page_title = "Student Life"
    context = {'page_title':page_title}
    return render(request, 'life.html', context)
def calendar(request):
    page_title = "Calendar"
    context = {'page_title':page_title}
    return render(request, 'calendar.html', context)
def about_activities(request):
    page_title = "Activities"
    context = {'page_title':page_title}
    return render(request, 'activities.html', context)
def about_course(request):
    page_title = "Course"
    context = {'page_title':page_title}
    return render(request, 'course.html', context)
def donation(request):
    page_title = "Donation"
    context = {'page_title':page_title}
    return render(request, 'donation.html', context)
def error_page(request):
    page_title = "404 Error"
    context = {'page_title':page_title}
    return render(request, '404.html', context)
def class_routine(request):
    page_title = "Class Routine"
    context = {'page_title':page_title}
    return render(request, 'class-routine.html', context)
def thankyou(request):
    page_title = "Thankyou"
    context = {'page_title':page_title}
    return render(request, 'thankyou.html', context)
def success(request):
    page_title = "Thankyou"
    context = {'page_title':page_title}
    return render(request, 'success.html', context)
def contact_us_view(request):
    if request.method == 'POST':
        # import pdb;
        # pdb.set_trace()
        form = ContactForm(request.POST)
        if form.is_valid():    
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                message=message
            )
            return redirect('success')
        else:
            for field in form.errors.keys():
                if field in form.cleaned_data:
                    del form.cleaned_data[field]     
    else:
        form = ContactForm()
    return render(request, 'contact-us.html', {'form': form})
def home_get_in_touch(request):
    if request.method == 'POST':
        # import pdb;
        # pdb.set_trace()
        form = ContactForm(request.POST)
        if form.is_valid():    
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                message=message
            )
            return redirect('success')
        else:
            for field in form.errors.keys():
                if field in form.cleaned_data:
                    del form.cleaned_data[field]      
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
def about_get_in_touch(request):
    if request.method == 'POST':
        # import pdb;
        # pdb.set_trace()
        form = ContactForm(request.POST)
        if form.is_valid():    
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                message=message
            )
            return redirect('success')
        else:
            for field in form.errors.keys():
                if field in form.cleaned_data:
                    del form.cleaned_data[field]      
    else:
        form = ContactForm()
    return render(request, 'about.html', {'form': form})
  
def admission_get_in_touch(request):
    if request.method == 'POST':
        # import pdb;
        # pdb.set_trace()
        form = ContactForm(request.POST)
        if form.is_valid():    
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                message=message
            )
            return redirect('success')
        else:
            for field in form.errors.keys():
                if field in form.cleaned_data:
                    del form.cleaned_data[field]      
    else:
        form = ContactForm()
    return render(request, 'admission.html', {'form': form})