from django.db import models

from django.core.exceptions import ValidationError

from django.core.validators import MinValueValidator, MaxValueValidator

from django.core.validators import EmailValidator
from django.core.validators import validate_email
def fintroducetudireccindecorreoelectrnico_email(value):
    if not value.endswith('ull.edu.es') and not value.endswith('ull.es'):
        raise ValidationError('El correo electrónico debe ser del dominio [ull.edu.es, ull.es]')

def validar_dni(value):

  abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
  letras_validacion = 'TRWAGMYFPDXBNJZSQVHLCKE'

  if len(value) != 9:
    raise ValidationError('El DNI debe tener 9 caracteres')

  else:

    if (value[0] not in 'XYZ') and (value[:8].isdigit()) and (value[-1] in abecedario):
      #* se divide el número/23 y se coge el resto
      resto = int(value[:8]) % 23
      if value[-1] == letras_validacion[resto]:
        return 0 #dni valido
      else:
        raise ValidationError('DNI con formato español no válido')

    elif (value[0] in 'XYZ') and (value[1:8].isdigit()) and (value[-1] in abecedario):
      # print('DNI válido extranjero')
      copia_dni = value
      copia_dni = copia_dni.replace('X', '0')
      copia_dni = copia_dni.replace('Y', '1')
      copia_dni = copia_dni.replace('Z', '2')
      #* se divide el número/23 y se coge el resto
      resto = int(copia_dni[:8]) % 23
      if value[-1] == letras_validacion[resto]:
        return 0 # dni válido
      else:
        raise ValidationError('DNI con formato extranjero no válido')

    else:
      raise ValidationError('Formato de DNI no válido')

from .utils.prefijos import PREFIJOS

from django.core.validators import RegexValidator

class TuModelo(models.Model):
  introducetunombreyapellidos = models.CharField(max_length=100)
  introducetufechadenacimiento = models.DateField()
  introducetuedad = models.IntegerField(validators=[MinValueValidator(14), MaxValueValidator(100)])
  introducetualu = models.CharField(max_length=200, validators=[RegexValidator(regex='^alu[0-9]{10}$', message='Introduzca un valor que cumpla la expresión regular: ^alu[0-9]{10}$')])
  prefijo_introducetunmerodetelfono = models.CharField(max_length=14, blank=True, choices=PREFIJOS)
  introducetunmerodetelfono = models.CharField(max_length=14, blank=True)
  introducetudireccindecorreoelectrnico = models.EmailField(max_length=254, validators=[validate_email,fintroducetudireccindecorreoelectrnico_email])
  introducetudni = models.CharField(max_length=9, validators=[validar_dni])
  seleccionatutalladecamiseta = models.CharField(max_length=100, choices=[('XS', 'XS'),('S', 'S'),('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL'),])
  aceptoelreglamentodelaprueba = models.BooleanField(default=False)
