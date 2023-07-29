from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def add_category(request):
    page_title = "Add Category"
    context = {'page_title':page_title}
    return render(request, 'categories/add.html', context)
def edit_category(request):
    page_title = "Edit Category"
    context = {'page_title':page_title}
    return render(request, 'categories/edit.html', context)
def category_list(request):
    page_title = "Category List"
    context = {'page_title':page_title}
    return render(request, 'categories/list.html', context)