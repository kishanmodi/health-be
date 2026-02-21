from rest_framework import viewsets
from .models import PatientDoctorMapping
from .serializers import MappingSerializer

class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer