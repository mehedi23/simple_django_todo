from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from .models import *
from .forms import *

def index(request):
    form = TaskForm()
    completed_task = Task.objects.filter(complete=True)
    uncompleted_task = Task.objects.filter(complete=False)

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/')

    context = {
        'completed_task' : completed_task,
        'uncompleted_task' : uncompleted_task,
        'form' : form
    }

    return render(request, 'list.html', context)




def update_task(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')


    context = {
        'form' : form,
        'id' : pk
    }

    return render(request, 'update.html', context)



def delete (request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')
