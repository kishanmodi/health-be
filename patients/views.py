from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)