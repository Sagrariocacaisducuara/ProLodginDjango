from django.db import models

class usuarios(models.Model):
    Nr_doc=models.CharField(max_length=38, null=True)
    Nombre=models.CharField(max_length=38, null=True)
    Contraseña=models.CharField(max_length=38, null=True)
    Id_rol=models.CharField(max_length=38, null=True)    


# Create your models here.
