from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate_age(self, value):
        if value <= 0 or value > 120:
            raise serializers.ValidationError("Age must be between 1 and 120.")
        return value

    def validate_gender(self, value):
        allowed = ['male', 'female', 'other']
        if value.lower() not in allowed:
            raise serializers.ValidationError(f"Invalid gender. Must be one of {allowed}.")
        return value.lower()

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Patient name must be at least 2 characters long.")
        return value