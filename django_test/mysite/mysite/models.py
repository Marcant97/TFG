from django.db import models

from django.core.exceptions import ValidationError

from django.core.validators import RegexValidator

class TuModelo(models.Model):
  introducetunombre = models.CharField(max_length=100)
  eligetutalladecamiseta = models.CharField(max_length=100, choices=[('XS', 'XS'),('S', 'S'),('M', 'M'),('XL', 'XL'),])
  aceptoelreglamentodelaprueba = models.BooleanField(default=False)
