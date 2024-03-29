from django.db import models

# Create your models here.
class Reto(models.Model):
    nombre = models.CharField(max_length=30)
    minutos_jugados = models.IntegerField()

class Jugadores(models.Model):
    grupo = models.CharField(max_length=2)
    num_lista = models.IntegerField()

class Usuarios(models.Model):
    password = models.CharField(max_length=10)

class Partidas(models.Model):
    fecha = models.DateField()
    id_usuario = models.CharField(max_length=5)
    minutos_jugados = models.IntegerField()
    puntaje = models.IntegerField()

class Partida_Jugadores(models.Model):
    fecha = models.DateField()
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE) 
    minutos_jugados = models.IntegerField()
    puntaje = models.IntegerField()

