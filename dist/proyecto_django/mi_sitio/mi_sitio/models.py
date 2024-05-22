from django.db import models

from django.core.exceptions import ValidationError

from django.core.validators import MinValueValidator, MaxValueValidator

from django.core.validators import EmailValidator
from django.core.validators import validate_email
def fintroduceunadireccindecorreoelectrnicosloullesoulledues_email(value):
    if not value.endswith('ull.es') and not value.endswith('ull.edu.es'):
        raise ValidationError('El correo electrónico debe pertenecer a uno de los siguientes dominios [ull.es, ull.edu.es]')

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
  introducetunombre = models.CharField(max_length=15)
  introducetusapellidos = models.CharField(max_length=100)
  introducetuedad = models.IntegerField()
  introducetunmerodehermanos = models.IntegerField(validators=[MinValueValidator(0)])
  introducetunotamedia = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
  seleccionatunivelmximodeestudios = models.CharField(max_length=100, choices=[('Sin estudios', 'Sin estudios'),('Educación primaria', 'Educación primaria'),('Educación secundaria', 'Educación secundaria'),('Bachillerato', 'Bachillerato'),('Formación Profesional', 'Formación Profesional'),('Grado', 'Grado'),('Máster', 'Máster'),('Doctorado', 'Doctorado'),])
  indicasiposeesalgncarnetdeconducir = models.BooleanField(default=False)
  quactividadeshasrealizadoestasemana = models.CharField(max_length=100, blank=True, null=True)
  introduceunadireccindecorreoelectrnico = models.EmailField(max_length=254)
  introduceunadireccindecorreoelectrnicosloullesoulledues = models.EmailField(max_length=254, validators=[validate_email,fintroduceunadireccindecorreoelectrnicosloullesoulledues_email])
  introduceundnivlido = models.CharField(max_length=9, validators=[validar_dni])
  prefijo_introduceunnmerodetelfono = models.CharField(max_length=14, blank=True, choices=PREFIJOS)
  introduceunnmerodetelfono = models.CharField(max_length=14, blank=True)
  introducetufechadenacimientoslomayoresdeedad = models.DateField()
  introduceunnombredeusuario = models.CharField(max_length=200, validators=[RegexValidator(regex='^[a-zA-Z0-9_-]{3,16}$', message='Introduzca un valor que cumpla la expresión regular: ^[a-zA-Z0-9_-]{3,16}$')])
  aceptoqueseenvenmisdatos = models.BooleanField(default=False)
