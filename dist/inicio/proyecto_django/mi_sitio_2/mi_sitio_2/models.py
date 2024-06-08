from django.db import models

from django.core.exceptions import ValidationError

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
  eligetugnero = models.CharField(max_length=100, choices=[('Hombre', 'Hombre'),('Mujer', 'Mujer'),('Otro', 'Otro'),])
  introducetudni = models.CharField(max_length=9, validators=[validar_dni])
  introducetudireccindecorreoelectrnico = models.EmailField(max_length=254)
  prefijo_introducetunmerodetelfono = models.CharField(max_length=14, blank=True, choices=PREFIJOS)
  introducetunmerodetelfono = models.CharField(max_length=14, blank=True)
  introducetudireccin = models.CharField(max_length=100)
  introducetucdigopostal = models.IntegerField()
  introduceunnombredeusuario = models.CharField(max_length=200, validators=[RegexValidator(regex='^[a-zA-Z0-9_-]{3,16}$', message='Introduzca un valor que cumpla la expresión regular: ^[a-zA-Z0-9_-]{3,16}$')])
  aceptolascondicionesdeusoylapolticadeprivacidad = models.BooleanField(default=False)
