from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from . import mqtt
from datetime import datetime,timedelta
from dashboard.models import Drug
from dashboard.models import Schedule
import pytz
from . import twilio

from dashboard.models import Reset

def dashboard(request):
    try:
        a = Reset.objects.get(name = '1')
    except:
        a = Reset.objects.create(name = '1', val = 'false')
        a.save()
    if datetime.now().hour == 0 and a.reset == 'false':
        for item in Drug.objects.all():
            item.pillsTaken = 0
        a.val = 'true'
    if datetime.now().hour != 0:
        a.val = 'false'
    a.save()


    drug1 = Drug.objects.get(slot = 1)
    drug2 = Drug.objects.get(slot = 2)
    drug3 = Drug.objects.get(slot = 3)
    a = Schedule.objects.all()
    send = None
    drug = None
    for item in a:
        if item.next_dispense is not None:
            utc=pytz.UTC
            a = item.next_dispense
            b = utc.localize(datetime.now()) 
            if a < b:
                send = item
                twilio.send(send.frequency, send.drug)
    if send is not None:
        if send.frequency == 'weekly':
            send.next_dispense = send.next_dispense+timedelta(days=7)
        else:
            send.next_dispense = send.next_dispense+timedelta(days=1)
        send.save()
        drug = {'slot' : Drug.objects.get(name = send.drug).slot}
    return render(request, 'dashboard.html', {'drug1':drug1,'drug2':drug2,'drug3':drug3,'notify':send,'slot':drug})

def dispense(request, slot, amount):
    print("Dispense slot:", slot)
    d = Drug.objects.get(slot = slot)
    d.pillsTaken += amount
    d.save()
    mqtt.publish_dispense_now(slot, amount)
    drug1 = Drug.objects.get(slot = 1)
    drug2 = Drug.objects.get(slot = 2)
    drug3 = Drug.objects.get(slot = 3)
    a = Schedule.objects.all()
    send = None
    drug = None
    for item in a:
        if item.next_dispense is not None:
            if item.next_dispense < datetime.now():
                send = item
                print(send)
    if send is not None:
        if send.frequency == 'weekly':
            send.next_dispense = send.next_dispense+timedelta(days=7)
        else:
            send.next_dispense = send.next_dispense+timedelta(days=1)
        send.save()
        drug = {'slot' : Drug.objects.get(name = send.drug).slot}
    return render(request, 'dashboard.html', {'drug1':drug1,'drug2':drug2,'drug3':drug3,'notify':send,'slot':drug})