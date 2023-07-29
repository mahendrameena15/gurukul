from django.shortcuts import render,redirect
from django.http import HttpResponse 
import hashlib
from django.contrib.auth import authenticate,login

def login(request):
    page_title = "Admin Login"
    context = {'page_title':page_title}
    return render(request, 'login.html', context)

def admin_login(request):
    if request.method == 'POST':
        # import pdb;
        # pdb.set_trace()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            return redirect('dashboard') 
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
