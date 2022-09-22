from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo
def home(request):
    todos = ToDo.objects.all()
    return render(request, 'todos/home.html', {
        'name':'Jakhonotin',
        'todos':todos
    })

def about(request):
    return render(request, 'todos/about.html')
def create_todo(request):
    ToDo.objects.create(title=request.POST.get('title', False))
    return redirect('home')
def completed(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.is_completed = True
    todo.save()
    return redirect('home')
def delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return redirect('home')