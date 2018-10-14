from django.contrib import admin

from .models import Drug, Schedule

@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_desc', 'per_day', 'pillsTaken', 'slot')
    fields = ['name', 'short_desc', 'per_day', 'pillsTaken', 'slot']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('drug', 'frequency', 'next_dispense', 'amount')
    fields = ['drug', 'frequency', 'next_dispense', 'amount']