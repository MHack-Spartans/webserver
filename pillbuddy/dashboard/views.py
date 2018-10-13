from django.shortcuts import render
from django.http import HttpResponse
from . import mqtt

def dashboard(request):
    return render(request, 'dashboard.html')

def dispense(request, slot):
    print("Dispense slot:", slot)
    mqtt.publish_dispense_now(slot, 1)
    return HttpResponse("")