from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin_panel.models import Student_Admission
from theme.forms import AdmissionForm
# Create your views here.
def add_user(request):
    page_title = "Add Users"
    if request.method == 'POST':
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
            return redirect('success')    
        else:
            return render(request, 'users/add.html', {'form': form, 'form_errors': form.errors,'page_title':page_title}) 
    else:  
        form=AdmissionForm() 
        return render(request, 'users/add.html', {'page_title':page_title})

def edit_user(request):
    page_title = "Edit Users"
    context = {'page_title':page_title}
    return render(request, 'users/edit.html', context)

def user_list(request):
    page_title = "Users List"  
    if request.method == 'GET':
        user_list=Student_Admission.objects.all()
        if user_list:
             return render(request,'users/list.html',{'user_list':user_list,'page_title':page_title})
        else:
            error_message = "Data Not Found"
            return render(request, 'users/list.html', {'error_message': error_message,'page_title':page_title})
    else:
        return render(request, 'users/list.html',{'page_title':page_title})  



