from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html', {})

def learn(request):
    return render(request, 'learn_more.html', {})