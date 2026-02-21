from rest_framework import serializers
from .models import PatientDoctorMapping

class MappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        read_only_fields = ['assigned_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make fields optional during partial updates
        if self.instance is not None:
            for field_name in self.fields:
                if field_name not in self.Meta.read_only_fields:
                    self.fields[field_name].required = False

    def validate(self, data):
        """Prevent duplicate patient-doctor mappings."""
        patient = data.get('patient') or (self.instance.patient if self.instance else None)
        doctor = data.get('doctor') or (self.instance.doctor if self.instance else None)
        if patient and doctor:
            # Exclude current instance from duplicate check during updates
            query = PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor)
            if self.instance:
                query = query.exclude(pk=self.instance.pk)
            if query.exists():
                raise serializers.ValidationError("This doctor is already assigned to this patient.")
        return data