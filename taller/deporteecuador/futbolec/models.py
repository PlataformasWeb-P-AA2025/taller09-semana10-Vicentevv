from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    username_x = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s" % (self.nombre,
                             self.siglas,
                             self.username_x)
    

class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    numero = models.IntegerField()
    sueldo = models.IntegerField()
    equipo = models.CharField(max_length=30)

    def __str__(self):
        return " %s %s %s %s %s" % (self.nombre,
                                    self.posicion,
                                    self.numero,
                                    self.sueldo,
                                    self.equipo)
    

class Campeonato(models.Model):
    nombre = models.CharField(max_length=30)
    auspiciante = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s " % (self.nombre,
                           self.auspiciante)
    
class CampeonatoEquipos(models.Model):
    anio = models.CharField(max_length=30)
    equipo = models.CharField(max_length=30)
    campeonato = models.CharField(max_length=30)

    def __str__(self):
        return " %s %s %s" % (self.anio,
                              self.equipo,
                              self.campeonato)
    