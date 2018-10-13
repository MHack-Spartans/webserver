from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from . import mqtt
from dashboard.models import Drug

def dashboard(request):
    drug1 = Drug.objects.get_or_None(slot=1)
    return render(request, 'dashboard.html', {'drug1':drug1})

def dispense(request, slot):
    print("Dispense slot:", slot)
    mqtt.publish_dispense_now(slot, 2)
    return HttpResponse("")