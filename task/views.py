from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required
def index(request):
    
    form = TaskForm()
    completed_task = Task.objects.filter(complete=True, user=request.user)
    uncompleted_task = Task.objects.filter(complete=False, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user;
            obj.save()

        return redirect('/todo')

    context = {
        'completed_task' : completed_task,
        'uncompleted_task' : uncompleted_task,
        'form' : form
    }

    return render(request, 'list.html', context)



@login_required
def update_task(request, pk):

    task = Task.objects.get(id=pk, user=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/todo')


    context = {
        'form' : form,
        'id' : pk
    }

    return render(request, 'update.html', context)


@login_required
def delete (request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return redirect('/')
