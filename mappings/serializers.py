from rest_framework import serializers
from .models import PatientDoctorMapping

class MappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        read_only_fields = ['assigned_at']

    def validate(self, data):
        """Prevent duplicate patient-doctor mappings."""
        patient = data.get('patient')
        doctor = data.get('doctor')
        if patient and doctor:
            if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
                raise serializers.ValidationError("This doctor is already assigned to this patient.")
        return data