from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin_panel.forms import CourseForm
from admin_panel.models import Course
from django.shortcuts import get_object_or_404

def add_course(request):
    page_title = "Add Course"
    if request.method == 'POST':
        # import pdb;
        # pdb.set_trace()
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():    
            add_course=Course(
            title = form.cleaned_data['title'],
            courses = form.cleaned_data['courses'],
            author = form.cleaned_data['author'],
            description = form.cleaned_data['description'])
            if 'picture' in request.FILES:
                add_course.picture = request.FILES['picture'] 
            meta_data = form.cleaned_data['meta'] 
            if meta_data:
                add_course.meta = meta_data
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
    context={'page_title': page_title}
    return render(request, 'courses/edit.html', context)
    # course = get_object_or_404(Course, pk=id)

    # if request.method == 'POST':
    #     form = CourseForm(request.POST, request.FILES, instance=course)
    #     if form.is_valid():
    #         course.title = form.cleaned_data['title']
    #         course.courses = form.cleaned_data['courses']
    #         course.author = form.cleaned_data['author']
    #         course.description = form.cleaned_data['description']  
    #         if 'picture' in request.FILES:
    #             course.picture = request.FILES['picture']
    #         meta_data = form.cleaned_data['meta']
    #         if meta_data:
    #             course.meta = meta_data
    #         course.save()
    #         return redirect('success')
    #     else:
    #         return render(request, 'courses/edit.html', {'form': form, 'form_errors': form.errors, 'page_title': page_title, 'id':id})
    # else:
    #     form = CourseForm(instance=course)
        # context = {'form': form, 'page_title': page_title, 'id':id}
       
        # return render(request, 'courses/edit.html', context)
