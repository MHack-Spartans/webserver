from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from . import mqtt
from dashboard.models import Drug

def dashboard(request):
    drug1 = Drug.objects.get(slot = 1)
    drug2 = Drug.objects.get(slot = 2)
    drug3 = Drug.objects.get(slot = 3)
    return render(request, 'dashboard.html', {'drug1':drug1,'drug2':drug2,'drug3':drug3})

def dispense(request, slot):
    print("Dispense slot:", slot)
    mqtt.publish_dispense_now(slot, 2)
    return HttpResponse("")