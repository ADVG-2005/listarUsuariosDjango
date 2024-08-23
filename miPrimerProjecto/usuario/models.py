from django.db import models

# Create your models here.
class Persona(models.Model):
    ESTADO_CHOICES = [
        ('activo','Activo'),
        ('inactivo','Inactivo')
    ]
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=11)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    estado=models.CharField(max_length=50,choices=ESTADO_CHOICES,default='activo')
    fechaCreate =models.DateField(auto_now=True) 
    
    def __str__(self):
        return self.nombre