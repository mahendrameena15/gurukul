from django.shortcuts import render,redirect
from .forms import ContactForm
import random,string
from django.http import HttpResponse
from admin_panel.models import Student_Admission
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
def contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():    
            return render(request, 'home.html')
        else:
            for field in form.errors.keys():
                if field in form.cleaned_data:
                    del form.cleaned_data[field]
    else:
        form = ContactForm()
    return render(request, 'contact-us.html', {'form': form})