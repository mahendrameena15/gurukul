from django.shortcuts import render
from django.http import HttpResponse
from admin_panel.forms import CourseForm
def add_course(request):
    page_title = "Add Course"
    if request.method == 'POST':
        # import pdb;
        # pdb.set_trace()
        form = CourseForm(request.POST)
        if form.is_valid():    
            
            title = form.cleaned_data['title']
            courses = form.cleaned_data['courses']
            author = form.cleaned_data['author']
            description = form.cleaned_data['description']
            meta = form.cleaned_data['meta']
            seo = form.cleaned_data['seo']
            Course.objects.create(
                author=author,
                courses=courses,
                title=title,
                description=description,
                meta=meta,
                seo=seo             )
            return redirect('success')
        else:  
            return render(request, 'courses/add.html', {'form': form, 'form_errors': form.errors,'page_title':page_title}) 
    else: 
        form = CourseForm()
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