from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if  form.is_valid():
            form.save()
        return redirect('/')

    context = {'todos':todos, 'form':form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, key):
    task = Todo.objects.get(id=key)
    form = TodoForm(instance=task)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if  form.is_valid():
            form.save()
            return redirect('/')

    
    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, key):
    task = Todo.objects.get(id=key)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    context = {'task':task}
    return render(request, 'tasks/delete.html', context)
    