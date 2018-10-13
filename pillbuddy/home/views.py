from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserCreationForm 
from django.shortcuts import redirect
from dashboard.models import Drug
from .forms import SetUpDrugForm

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

def login(request):
    return render(request, 'registration/login.html',{})

def setup(request):
    try:
        drug1 = Drug.objects.get(slot = 1)
    except:
        drug1 = Drug.objects.create(name = "advil",
        short_desc="pain rel.",
        per_day="12",
        pillsTaken="15",
        slot="1")
        drug1.save()
    drugform = SetUpDrugForm(request.POST or None)

    # If this is a POST request then process the Form data
    if request.method == 'POST' and drugform.is_valid():

        # Create a form instance and populate it with data from the request (binding):        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        drug1.name = drugform.cleaned_data['Name']
        drug1.short_desc = drugform.cleaned_data['Description']
        drug1.per_day = drugform.cleaned_data['MaxPerDay']
        drug1.pillsTaken = drugform.cleaned_data['TakenToday']
        drug1.slot = drugform.cleaned_data['Slot']
        drug1.save()

        # redirect to a new URL:
        return HttpResponseRedirect(reverse('home') )
    else:
        context =  SetUpDrugForm()

    return render(request, 'setup.html', {"thing":context})


