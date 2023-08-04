from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from admin_panel.forms import CategoryForm
from admin_panel.models import Category
def add_category(request):
    page_title = "Add Category"
    if request.method == 'POST':
        # import pdb;
        # pdb.set_trace()
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():    
            add_category=Category(
            title = form.cleaned_data['title'],
            category = form.cleaned_data['category'],
            author = form.cleaned_data['author'],
            description = form.cleaned_data['description'])
            if 'picture' in request.FILES:
                add_category.picture = request.FILES['picture'] 
            meta_data = form.cleaned_data['meta'] 
            if meta_data:
                add_category.meta = meta_data
            add_category.save()         
            return redirect('success')
        else:  
            return render(request, 'categories/add.html', {'form': form, 'form_errors': form.errors,'page_title':page_title}) 
    else: 
        form = CategoryForm()
        context = {'form': form, 'page_title': page_title}
        return render(request, 'categories/add.html', context)

    
def edit_category(request):
    page_title = "Edit Category"
    context = {'page_title':page_title}
    return render(request, 'categories/edit.html', context)

def category_list(request):
    page_title = "Category List" 
    if request.method == 'GET':
        category_list=Category.objects.all()
        if category_list:
             return render(request,'categories/list.html',{'category_list':category_list,'page_title':page_title})
        else:
            error_message = "Data Not Found"
            return render(request, 'categories/list.html', {'error_message': error_message,'page_title':page_title})
    else:
        error_message = "Data Not Found"
        return render(request, 'categories/list.html',{'error_message': error_message,'page_title':page_title})  

