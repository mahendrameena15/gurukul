from django.shortcuts import render
from django.http import HttpResponse
from admin_panel.models import Student_Admission
# Create your views here.
def add_user(request):
    page_title = "Add Users"
    context = {'page_title':page_title}
    return render(request, 'users/add.html', context)
def edit_user(request):
    page_title = "Edit Users"
    context = {'page_title':page_title}
    return render(request, 'users/edit.html', context)
def user_list(request):
    page_title = "Users List"
    context = {'page_title':page_title}
    return render(request, 'users/list.html', context)


def user_list_view(request):
    if request.method == 'GET':
        import pdb;
        pdb.set_trace()
        user_list=Student_Admission.objects.all()
        if user_list:
             return render(request,'users/list.html',{'user_list':user_list})
        else:
            error_message = "Data Not Found"
            return render(request, 'users/list.html', {'error_message': error_message})
    else:
        error_message = "Data Not Found"
    return render(request, 'users/list.html', {'error_message': error_message})
