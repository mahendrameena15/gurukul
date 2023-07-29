from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def add_course(request):
    page_title = "Add Course"
    context = {'page_title':page_title}
    return render(request, 'courses/add.html', context)
def edit_course(request):
    page_title = "Edit Course"
    context = {'page_title':page_title}
    return render(request, 'courses/edit.html', context)
def course_list(request):
    page_title = "Course List"
    context = {'page_title':page_title}
    return render(request, 'courses/list.html', context)