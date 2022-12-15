from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)



def sign_up(request):
    context = {}
    return render(request, 'sign-up.html', context)