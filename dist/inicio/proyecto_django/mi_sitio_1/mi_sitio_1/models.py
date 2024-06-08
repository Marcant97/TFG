from django.db import models

from django.core.exceptions import ValidationError

from django.core.validators import RegexValidator

class TuModelo(models.Model):
  introducetunombre = models.CharField(max_length=100)
  introducetudireccindecorreoelectrnico = models.EmailField(max_length=254)
  asunto = models.CharField(max_length=30)
  mensaje = models.CharField(max_length=500)
  aceptolascondicionesdeusoylapolticadeprivacidad = models.BooleanField(default=False)
