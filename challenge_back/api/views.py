from rest_framework import viewsets, filters

from import_file import models
from . import serializers


class PersonaViewset(viewsets.ModelViewSet):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer
    http_method_names = ["get"]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['nombre', 'email', 'ciudad']

    ordering_fields = ['fecha_nac']
