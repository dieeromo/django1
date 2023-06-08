from django.db import models
from django.contrib.auth.models import User


class empresa(models.Model):
    nombreEmpresa = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombreEmpresa

class proveedoresProd(models.Model):
    nombreProveedor = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombreProveedor