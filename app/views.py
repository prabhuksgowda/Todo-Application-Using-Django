from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Task

# Create your views here.

class TaskView(CreateView,ListView):
    model = Task
    fields = ['task_title','task_description','status']
    template_name='index.html'
    ordering = ['-id']
    success_url ='/'
    context_object_name = 'task'
    
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['task_title','task_description','status']
    template_name='update.html'
    success_url ='/'

class TaskDeleteView(DeleteView):
    model = Task
    template_name='delete.html'
    success_url ='/'

