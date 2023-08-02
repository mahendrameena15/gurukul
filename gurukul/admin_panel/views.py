from django.shortcuts import render

# Create your views here.
def dashboard(request):
    page_title = "Dashboard"
    context = {'page_title':page_title}
    return render(request, 'dashboard.html', context)   
def success(request):
    page_title = "Success"
    context = {'page_title':page_title}
    return render(request,'success.html', context)