from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been created succesfully")
        return render(request, 'tool/login.html')
    else:
        return render(request, 'tool/registration.html')

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password= loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In")
            return render(request, 'tool/welcome.html')
    else:
        messages.success(request, "Invalid")
        return render(request, 'tool/login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, "Logged out!")
    return redirect('Register')

