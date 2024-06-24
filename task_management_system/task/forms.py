from django import forms
from . models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ['is_completed']
        widgets = {
            'task_assign_date' : forms.DateInput(attrs={'type' : 'date'})
        }
        labels = {
            'task_title' : 'Task Title',
            'task_description' : 'Task Description',
            'is_completed' : 'Task Completed',
            'task_assign_date' : 'Task Assign Date',
            'category' : 'Category'
        }
      

   