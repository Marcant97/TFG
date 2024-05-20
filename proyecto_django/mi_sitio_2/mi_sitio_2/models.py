from django.db import models

from django.core.exceptions import ValidationError

from django.core.validators import RegexValidator

class TuModelo(models.Model):
  casilladeseleccin = models.CharField(max_length=100, blank=True, null=True)
