from django.db import models

from django.core.exceptions import ValidationError

from .utils.prefijos import PREFIJOS

from django.core.validators import RegexValidator

class TuModelo(models.Model):
  introducetunombre = models.CharField(max_length=30)
  introducetudireccindecorreoelectrnico = models.EmailField(max_length=254)
  prefijo_introducetunmerodetelfono = models.CharField(max_length=14, blank=True, choices=PREFIJOS)
  introducetunmerodetelfono = models.CharField(max_length=14, blank=True)
  eligetupeluqueroa = models.CharField(max_length=100, choices=[('Carlos', 'Carlos'),('Silvia', 'Silvia'),('Laura', 'Laura'),('Javier', 'Javier'),('Ana', 'Ana'),])
  eligelafechaparatucita = models.DateField()
  eligelahoraparatucita = models.CharField(max_length=100, choices=[('9:00', '9:00'),('10:00', '10:00'),('11:00', '11:00'),('12:00', '12:00'),('13:00', '13:00'),('16:00', '16:00'),('17:00', '17:00'),('18:00', '18:00'),('19:00', '19:00'),])
  indicalosserviciosquedeseas = models.CharField(max_length=100, blank=True, null=True)
  indicasitienesalgunapeticinespecial = models.CharField(max_length=100)
