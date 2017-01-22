from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, 'navigation/index.html')

def victorian_health(request):
    return render(request, 'navigation/victorian_health.html')

def victorian_communication(request):
    return render(request, 'navigation/victorian_communication.html')

def reflections(request):
    return render(request, 'navigation/reflections.html')
