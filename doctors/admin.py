from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'hospital']
    list_filter = ['specialization', 'hospital']
    search_fields = ['name', 'specialization']
    ordering = ['name']