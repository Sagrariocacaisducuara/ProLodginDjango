from django.db import models

class usuarios(models.Model):
    Nr_doc=models.IntegerField(primary_key=True)
    Nombre=models.CharField(max_length=38, null=True)
    Contraseña=models.CharField(max_length=38, null=True)
    Id_rol=models.CharField(max_length=38, null=True)    


# Create your models here.
