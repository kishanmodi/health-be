from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Doctor name must be at least 3 characters long.")
        return value