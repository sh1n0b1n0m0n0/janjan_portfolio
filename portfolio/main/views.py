from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def ave_cicero(request):
    return render(request, 'main/ave.html')


def kill_cicero(request):
    return render(request, 'main/kill.html')