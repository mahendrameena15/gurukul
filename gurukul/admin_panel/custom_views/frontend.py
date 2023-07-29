from django.shortcuts import render,redirect
from django.http import HttpResponse 
import hashlib
# from admin_panel.forms import LoginForm
from django.contrib.auth import authenticate,login

def login(request):
    page_title = "Admin Login"
    context = {'page_title':page_title}
    return render(request, 'login.html', context)

def admin_login(request):
    if request.method == 'POST':
        # import pdb;
        # pdb.set_trace()
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

    #         import pdb;
    #         pdb.set_trace()
    #         form = AuthenticationForm(request, data=request.POST)
    #         if form.is_valid():
    #             email = form.cleaned_data['email']
    #             password = form.cleaned_data['password']
    #             # role=201
    #             user=authenticate(email=email,password=password)
    #             if user:
    #                 login(request, user)
    #                 return redirect('dashboard')
    #             else:
    #                 form.add_error(None, "Invalid username or password.")
    #         else:
    #             for field in form.errors.keys():
    #                  if field in form.cleaned_data:
    #                      del form.cleaned_data[field]
    # else:
    #     form = LoginForm()
    # return render(request, 'login.html', {'form': form})
   

    # if request.method=="POST":
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')
    #     role=201
    #     check_user=Users.objects.filter(email=email) and Users.objects.filter(password=password) and Users.objects.filter(role=role).count
    #     print (check_user)
    #     if check_user:
    #         return redirect(url'dashboard')
    #     else:
    #        return redirect(url'login')