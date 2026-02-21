from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make fields optional during partial updates
        if self.instance is not None:
            for field_name in self.fields:
                self.fields[field_name].required = False
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Doctor name must be at least 3 characters long.")
        return value