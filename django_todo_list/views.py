from django.http import HttpResponse
from django.shortcuts import render, redirect

def homepage(request):
    if request.user.is_authenticated:
        return redirect('tasks:list')
    else:
        return render(request, 'index.html')