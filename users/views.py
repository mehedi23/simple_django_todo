from django.shortcuts import render, redirect
from .form import Sign_Up_form
from django.contrib.auth import authenticate , login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def home(request):

    if request.user.is_authenticated : 
        return redirect('/todo')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('/todo')
        else :
            messages.error(request, "Something went wrong")
            return redirect('/')

    form = AuthenticationForm()
    context = {
        'form' : form
    }

    return render(request, 'home.html', context)



def sign_up(request):
    if request.user.is_authenticated : 
        return redirect('/todo')
    
    form = Sign_Up_form()

    if request.method == 'POST':
        form = Sign_Up_form(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form
    }

    return render(request, 'sign-up.html', context)



def log_out(request):
    auth_logout(request)
    return redirect('/')
