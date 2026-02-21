from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import MappingSerializer
from doctors.serializers import DoctorSerializer
from patients.models import Patient


class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """User only sees mappings of their own patients."""
        return PatientDoctorMapping.objects.filter(patient__user=self.request.user).order_by('-assigned_at')

    def perform_create(self, serializer):
        """Assign doctor to patient with security check."""
        patient = serializer.validated_data['patient']

        # security check
        if patient.user != self.request.user:
            raise PermissionDenied("You cannot assign doctor to another user's patient.")

        serializer.save()

    @action(detail=False, methods=['get'], url_path=r'patient/(?P<patient_id>\d+)')
    def doctors_of_patient(self, request, patient_id=None):
        """Get all doctors assigned to a specific patient."""
        mappings = PatientDoctorMapping.objects.filter(
            patient_id=patient_id,
            patient__user=request.user
        )
        doctors = [m.doctor for m in mappings]
        return Response(DoctorSerializer(doctors, many=True).data)