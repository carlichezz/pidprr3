from django.db import models

# Create your models here.

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=1)
    facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
    anno = models.CharField(max_length=1)

    def __str__(self):
        return self.facultad.nombre + self.anno + '0' + self.nombre
    
class Estudiante(models.Model):
    nombre = models.CharField (max_length=100)
    apellido = models.CharField (max_length=100)
    user = models.CharField (max_length=100)
    correo = models.CharField (max_length=100)
    ci = models.CharField (max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)