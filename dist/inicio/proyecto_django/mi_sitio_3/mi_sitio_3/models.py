from django.db import models

from django.core.exceptions import ValidationError

from django.core.validators import RegexValidator

class TuModelo(models.Model):
  seleccionaturangodeedad = models.CharField(max_length=100, choices=[('Menos de 18 años', 'Menos de 18 años'),('18-24 años', '18-24 años'),('25-34 años', '25-34 años'),('35-44 años', '35-44 años'),('45-54 años', '45-54 años'),('55-64 años', '55-64 años'),('65-74 años', '65-74 años'),('75 años o más', '75 años o más'),])
  eligetugnero = models.CharField(max_length=100, choices=[('Hombre', 'Hombre'),('Mujer', 'Mujer'),('Otro', 'Otro'),])
  quesloquemstehagustado = models.CharField(max_length=100, blank=True, null=True)
  eligedel110tugradodesatisfaccin = models.CharField(max_length=100, choices=[('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),])
  djanostussugerenciasfelicitacionesoquejas = models.CharField(max_length=500)
