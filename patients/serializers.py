from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=1, max_value=120, help_text="Patient age (1-120)")
    
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make fields optional during partial updates
        if self.instance is not None:
            for field_name in self.fields:
                if field_name not in self.Meta.read_only_fields:
                    self.fields[field_name].required = False

    def validate_age(self, value):
        if value and (value <= 0 or value > 120):
            raise serializers.ValidationError("Age must be between 1 and 120.")
        return value

    def validate_gender(self, value):
        if value:
            allowed = ['male', 'female', 'other']
            if value.lower() not in allowed:
                raise serializers.ValidationError(f"Invalid gender. Must be one of {allowed}.")
            return value.lower()
        return value

    def validate_name(self, value):
        if value and len(value) < 2:
            raise serializers.ValidationError("Patient name must be at least 2 characters long.")
        return value

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Patient name must be at least 2 characters long.")
        return value