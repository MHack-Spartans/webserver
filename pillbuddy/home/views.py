from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .forms import UserCreationForm 
from django.shortcuts import redirect
from dashboard.models import Drug
from dashboard.models import Schedule
from .forms import SetUpDrugForm
from .forms import SetUpSchedule
import json
from django.views import generic

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

    drugform = SetUpDrugForm(request.POST or None)

    # If this is a POST request then process the Form data
    if request.method == 'POST' and drugform.is_valid():

        # Create a form instance and populate it with data from the request (binding):        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        try:
            drug1 = Drug.objects.get(slot = drugform.cleaned_data['Slot'])
        except:
            drug1 = Drug.objects.create(name = "advil",
                short_desc="pain rel.",
                per_day="12",
                pillsTaken="15",
                slot="1")
            drug1.save()
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

def schedule(request):

    scheduleForm = SetUpSchedule(request.POST or None)

    # If this is a POST request then process the Form data
    if request.method == 'POST' and scheduleForm.is_valid():

        # Create a form instance and populate it with data from the request (binding):        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        schedule1 = Schedule.objects.create(drug = "[advil]",
            frequency = "daily",
            next_dispense = datetime.now(),
            amount = 1
        )
        schedule1.save() 
        schedule1.drug = json.dumps(scheduleForm.cleaned_data['Medicine'])
        schedule1.frequency = scheduleForm.cleaned_data['Frequency']
        schedule1.next_dispense = datetime.combine(scheduleForm.cleaned_data['start_date'],scheduleForm.cleaned_data['start_time'])
        schedule1.amount =  scheduleForm.cleaned_data['amount']
        schedule1.save()
        # redirect to a new URL:
        return HttpResponseRedirect(reverse('home') )
    return render(request, 'setup.html', {"thing":scheduleForm})

from django.views import generic
from django.urls import reverse_lazy

class ScheduleListView(generic.ListView):
    model = Schedule
    paginate_by = 10

from django.views.generic.edit import CreateView, UpdateView, DeleteView
class ScheduleCreate(CreateView):
    model = Schedule
    fields = '__all__'

class ScheduleDelete(DeleteView):
    model = Schedule
    success_url = reverse_lazy('schedule_list')