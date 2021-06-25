from django.db import models

# Create your models here.
from django.db import models


class Persona(models.Model):

    nombre = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    fecha_nac = models.DateField()
    ciudad = models.CharField(max_length=100, blank=True)


