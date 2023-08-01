from django.shortcuts import render,redirect
from theme.forms import ContactForm
import phonenumbers
from django.contrib import messages
import random,string
from django.urls import reverse
from django.http import HttpResponse
from admin_panel.models import Student_Admission,ContactMessage
def contact_us(request):
    if request.method == 'POST':
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
            return render(request, 'contact-us.html', {'form': form, 'form_errors': form.errors}) 
    else: 
        form = ContactForm()
        page_title = "Contact Us"
        context = {'page_title':page_title}
        return render(request, 'contact-us.html',context)
def home(request):
    if request.method == 'POST':
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
            return render(request, 'home.html', {'form': form, 'form_errors': form.errors})    
    else:
        form = ContactForm()
        page_title = "Home"
        context = {'page_title':page_title}
        return render(request, 'home.html', context)
    # return render(request, 'home.html', {'form': form})
def about_us(request):
    if request.method == 'POST':
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
            return render(request, 'about.html', {'form': form, 'form_errors': form.errors})     
    else:
        form = ContactForm()
        page_title = "About Us"
        context = {'page_title':page_title}
        return render(request, 'about.html', context)
    # return render(request, 'about.html', {'form': form})
  
def about_admission(request):
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
            return render(request, 'admission.html', {'form': form, 'form_errors': form.errors})      
    else:
        form = ContactForm()
        page_title = "About-Admission"
        context = {'page_title':page_title}
        return render(request, 'admission.html', context)
    # return render(request, 'admission.html', {'form': form})