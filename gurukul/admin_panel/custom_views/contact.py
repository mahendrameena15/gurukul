from django.shortcuts import render,redirect
from django.http import HttpResponse
from theme.forms import ContactForm
from admin_panel.models import ContactMessage
def add_contact(request):
    page_title = "Add Contact"
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():    
            add_contact=ContactMessage(
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            email = form.cleaned_data['email'],
            phone_number = form.cleaned_data['phone_number'],
            message=form.cleaned_data['message'])   
            add_contact.save()         
            return redirect('success')
        else:  
            return render(request, 'contact/add.html', {'form': form, 'form_errors': form.errors,'page_title':page_title}) 
    else: 
        form = ContactForm()
        context = {'form': form, 'page_title': page_title}
        return render(request, 'contact/add.html', context)

def contact_list(request):
    page_title = "Contact List"  
    if request.method == 'GET':
        contact_list=ContactMessage.objects.all()
        if contact_list:
             return render(request,'contact/list.html',{'contact_list':contact_list,'page_title':page_title})
        else:
            error_message = "Data Not Found"
            return render(request, 'contact/list.html', {'error_message': error_message,'page_title':page_title})
    else:
        error_message = "Data Not Found"
        return render(request, 'contact/list.html',{'error_message': error_message,'page_title':page_title})  
