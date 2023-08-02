from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin_panel.forms import CourseForm
from admin_panel.models import Course
import json
def add_course(request):
    page_title = "Add Course"
    if request.method == 'POST':
        # import pdb;
        # pdb.set_trace()
        form = CourseForm(request.POST)
        if form.is_valid():    
            add_course=Course(
            title = form.cleaned_data['title'],
            courses = form.cleaned_data['courses'],
            author = form.cleaned_data['author'],
            description = form.cleaned_data['description'],
            meta = form.cleaned_data['meta'],
            seo = form.cleaned_data['seo'] )   
            add_course.save()         
            return redirect('success')
        else:  
            return render(request, 'courses/add.html', {'form': form, 'form_errors': form.errors,'page_title':page_title}) 
    else: 
        form = CourseForm()
        context = {'form': form, 'page_title': page_title}
        return render(request, 'courses/add.html', context)

def course_list(request):
    page_title = "Course List"  
    if request.method == 'GET':
        course_list=Course.objects.all()
        if course_list:
             return render(request,'courses/list.html',{'course_list':course_list,'page_title':page_title})
        else:
            error_message = "Data Not Found"
            return render(request, 'courses/list.html', {'error_message': error_message,'page_title':page_title})
    else:
        error_message = "Data Not Found"
        return render(request, 'courses/list.html',{'error_message': error_message,'page_title':page_title})  

def edit_course(request):
    page_title = "Edit Course"
    context = {'page_title':page_title}
    return render(request, 'courses/edit.html', context)