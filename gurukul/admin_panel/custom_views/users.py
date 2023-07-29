from django.shortcuts import render
from django.http import HttpResponse
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