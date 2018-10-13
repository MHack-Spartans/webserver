from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserCreationForm 
from django.shortcuts import redirect

def home(request):
    return render(request, 'index.html', {})

def learn(request):
    return render(request, 'learn_more.html', {})

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('register_success')
    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})

def register_success(request):
    return render(request, 'registration/register_success.html')