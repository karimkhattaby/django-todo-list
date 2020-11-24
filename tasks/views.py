from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required(login_url='/accounts/login')
def get_all(request):
    if request.method == 'GET':
        categories = Category.objects.filter(owner=request.user)
        tasks = Task.objects.filter(owner=request.user, completed=False)
        context = {'tasks': tasks, 'categories': categories}
        return render(request, 'tasks/list.html', context)

@login_required(login_url='/accounts/login')
def get_category(request, cat_id):
    if request.method == 'GET':
        category = Category.objects.get(owner=request.user, id=cat_id)
        tasks = Task.objects.filter(owner=request.user, completed=False, category=category)
        context = {'tasks': tasks, 'category': category}
        return render(request, 'tasks/list_category.html', context)

@login_required(login_url='/accounts/login')
def add_task(request):
    if request.method == 'GET':
        form = TaskForm(request.user)
    elif request.method == 'POST':
        form = TaskForm(request.user, request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect('tasks:list')
    context = {'form': form}
    return render(request, 'tasks/create_task.html', context)

@login_required(login_url='/accounts/login')
def add_category(request):
    if request.method == 'GET':
        form = CategoryForm()
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect('tasks:list')
    context = {'form': form}
    return render(request, 'tasks/create_category.html', context)

@login_required(login_url='/accounts/login')
def update_task(request, task_id):
    task = Task.objects.get(owner=request.user, id=task_id)
    if request.method == 'GET':
        form = TaskForm(request.user, instance=task)
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:list')
    context = {'task': task, 'form': form}
    return render(request, 'tasks/update_task.html', context)

@login_required(login_url='/accounts/login')
def update_category(request, cat_id):
    category = Category.objects.get(owner=request.user, id=cat_id)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('tasks:get_category', cat_id=cat_id)
    context = {'category': category, 'form': form}
    return render(request, 'tasks/update_category.html', context)

@login_required(login_url='/accounts/login')
def delete_task(request, task_id):
    task = Task.objects.get(owner=request.user, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:list')
    context = {'task': task}
    return render(request, 'tasks/delete_task.html', context)

@login_required(login_url='/accounts/login')
def delete_category(request, cat_id):
    category = Category.objects.get(owner=request.user, id=cat_id)
    if request.method == 'POST':
        default_category = Category.objects.get(owner=request.user, name='Uncategorized')
        tasks = Task.objects.filter(owner=request.user, category=category)
        for task in tasks:
            task.category = default_category
            task.save()
        category.delete()
        return redirect('tasks:list')
    context = {'category': category}
    return render(request, 'tasks/delete_category.html', context)

@login_required(login_url='/accounts/login')
def mark_task_complete(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(owner=request.user, id=task_id)
        task.completed = True
        task.save()
        return redirect('tasks:list')

@login_required(login_url='/accounts/login')
def get_completed(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(owner=request.user, completed=True)
        context = {'tasks': tasks}
        return render(request, 'tasks/list_completed.html', context)