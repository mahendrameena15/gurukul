from django.shortcuts import render
from django.http import HttpResponse 
import hashlib
from admin_panel.forms import loginForm

def generate_sha256_hash(input_string):
    # Convert the input_string to bytes using UTF-8 encoding
    input_bytes = input_string.encode('utf-8')
    
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the input bytes
    sha256_hash.update(input_bytes)
    
    # Get the hexadecimal representation of the hash
    hex_hash = sha256_hash.hexdigest()
    
    return hex_hash


def login(request):
    page_title = "Admin Login"
    context = {'page_title':page_title}
    return render(request, 'login.html', context)

def loginPost(request):
    #  return HttpResponse(generate_sha256_hash("hello"))
    try:
        if request.method == 'POST':
            form = loginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                role=201
                check_user==Users.objects.filter(email=email) and Users.objects.filter(password=password) and Users.objects.filter(role=role).count
                if check_user:
                    return render(request, 'dashboard.html')
                else:
                    return render(request, 'login.html')
            else:
                form = loginForm()
                return render(request, 'login.html', {'form': form})
        else:
            form = loginForm()
            return render(request, 'login.html', {'form': form})
    except:
         return render(request, 'login.html')


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