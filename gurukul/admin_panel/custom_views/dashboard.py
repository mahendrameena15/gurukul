from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dashboard(request):
    page_title = "Dashboard"
    context = {'page_title':page_title}
    return render(request, 'dashboard.html', context)