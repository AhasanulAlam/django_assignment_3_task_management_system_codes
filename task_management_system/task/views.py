from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_task(request):
    if request.method =='POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form' : task_form})

def edit_task(request, id):
    task = models.Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)

    if request.method =='POST': # user sent POST request
        task_form = forms.TaskForm(request.POST, instance=task)  # capture the user post data
        if task_form.is_valid(): # checking the post data validation
            task_form.save() # if data valid save in the database
            return redirect('show_tasks')  # redirect to the page 
    return render(request, 'add_task.html', {'form' : task_form})

def complete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.is_completed = True  # update the is_completed field
    task.save() # if data valid save in the database
    return redirect('show_tasks')  # redirect to the page 

def delete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('show_tasks')  # redirect to the page 