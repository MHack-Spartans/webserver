from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from . import mqtt
from dashboard.models import Drug

def dashboard(request):
    advil = Drug(name='advil')
    return render(request, 'dashboard.html', {'drug':advil})

def dispense(request, slot):
    print("Dispense slot:", slot)
    mqtt.publish_dispense_now(slot, 1)
    return HttpResponse("")