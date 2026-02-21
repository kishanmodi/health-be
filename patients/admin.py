from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'user', 'created_at']
    list_filter = ['gender', 'created_at', 'user']
    search_fields = ['name', 'user__username']
    ordering = ['-created_at']