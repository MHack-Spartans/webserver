from django.contrib import admin

from .models import Drug

@admin.register(Drug)
class RFIDAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_desc', 'per_day', 'pillsTaken')
    fields = ['name', 'short_desc', 'per_day', 'pillsTaken']