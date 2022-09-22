from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from todos.serializers import ToDoSerializer
from .models import ToDo
from rest_framework.response import Response
from rest_framework import status
def home(request):
    todos = ToDo.objects.all()
    return render(request, 'todos/home.html', {
        'name':'Jakhonotin',
        'todos':todos
    })

@api_view(['GET', 'POST'])
def todo_api(request, format=None):
    if request.method == 'GET':
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return JsonResponse({'todos': serializer.data})
    if request.method == 'POST':
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id, format=None):
    todo = ToDo.objects.get(pk=id)
    if request.method == 'GET':
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def about(request):
    return render(request, 'todos/about.html')
def create_todo(request):
    ToDo.objects.create(title=request.POST.get('title', ''))
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