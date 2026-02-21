from rest_framework import serializers
from .models import PatientDoctorMapping

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'