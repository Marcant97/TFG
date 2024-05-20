from lectura import comprobarDiccionario

# tipo no existe
miDiccionario0 = [
  {"tipo": "inventado",
   "titulo": "inventado"}
]

# falta el tipo
miDiccionario00 = [
  {"titulo": "inventado"}
]

# falta el titulo
miDiccionario000 = [
  {"tipo": "texto"}
]


miDiccionario1 = [
  {
    "tipo": "texto",
    "titulo": "Nombre",
    "limite": 20
  },
  { # limitee incorrecto
    "tipo": "texto",
    "titulo": "Nombre",
    "limitee": 20
  }
]



miDiccionario2 = [
  {
    "tipo": "numero",
    "titulo": "Edad",
    "valorMinimo": 0,
    "valorMaximo": 100
  },
  {  # campo con contenido no válido
    "tipo": "numero",
    "titulo": "Edad",
    "minimo": "hola"
  }
]


miDiccionario22 = [
  {
    "tipo": "numero",
    "titulo": "Edad",
    "valorMinimo": 0,
    "valorMaximo": 100
  },
  {  # campo con contenido no válido
    "tipo": "numero",
    "titulo": "Edad",
    "valorMinimo": "hola"
  }
]




miDiccionario3 = [
  { # correcto
    "tipo": "desplegable",
      "titulo": "Pregunta desplegable",
      "opciones": [
        "Opción 1",
        "Opción 2",
        "Opción 3"
      ]
  },
  {
    "tipo": "desplegable",
      "titulo": "Pregunta desplegable",
      "content": [ # nombre del campo incorrecto
        "Opción 1",
        "Opción 2",
        "Opción 3"
      ]
  }
]

miDiccionario33 = [
  {
    "tipo": "desplegable",
    "titulo": "Pregunta desplegable"
  } # falta el campo opciones, que es obligatorio
]

miDiccionario333 = [
  {
    "tipo": "desplegable",
    "titulo": "Pregunta desplegable",
    "opciones": "Opción" # opciones debe ser un array
  }
]

miDiccionario3333 = [
  {
    "tipo": "desplegable",
    "titulo": "Pregunta desplegable",
    "opciones": ["Opción", True, 2] # opciones debe ser un array de strings.
  }
]




miDiccionario4= [
  {
    "tipo": "casilla",
    "titulo": "Pregunta de selección múltiple",
  },
  {
    "tipo": "casilla",
    "titulo": "Pregunta de selección múltiple",
    "opciones": [ # nombre del campo incorrecto
      "Opción 1",
      "Opción 2",
      "Opción 3"
    ]
  }
]

miDiccionario44= [
  {
    "tipo": "casilla",
    "titulo": "Pregunta de selección múltiple",
    "obligatorio": "True" # campo no válido
  }
]

miDiccionario444= [
  {
    "tipo": "casilla",
    "titulo": "Pregunta de selección múltiple",
    "obligatorio": False # campo correcto
  }
]


# email
miDiccionario5 = [
  { # correcto
    "tipo": "email",
    "titulo": "Introduce tu correo electrónico"
  },
  {
    "tipo": "email",
    "titulo": "Introduce tu correo electrónico",
    "dominiosDisponibles": "gmail.com" # dominiosDisponibles debe ser un array
  }
]

miDiccionario55 = [
  {
    "tipo": "email",
    "titulo": "Introduce tu correo electrónico",
    "dominiosDisponibles": ["gmail.com"]
  },
    {
    "tipo": "email",
    "titulo": "Introduce tu correo electrónico",
    "dominios": ["gmail.com"] # campo incorrecto, dominios no existe
  }
]


miDiccionario555 = [
  {
    "tipo": "email",
    "titulo": "Introduce tu correo electrónico",
    "dominiosDisponibles": ["gmail.com", 2, 3] # dominiosDisponibles debe ser una lista de strings
  }
]

miDiccionario6 = [
  { # correcto
    "tipo": "dni",
    "titulo": "Introduce tu DNI"
  }
]

miDiccionario66 = [
  { # correcto
    "tipo": "dni",
    "titulo": "Introduce tu DNI",
    "campoNoValido": "hola" # campo incorrecto
  }
]

miDiccionario7 = [
  { # correcto
    "tipo": "telefono",
    "titulo": "Introduce tu número de teléfono"
  }
]

miDiccionario77 = [
  { # correcto
    "tipo": "telefono",
    "titulo": "Introduce tu número de teléfono",
    "campoNoValido": "hola" # campo incorrecto
  }
]

# fecha
miDiccionario8 = [
  { # correcto
    "tipo": "fecha",
    "titulo": "Introduce tu fecha de nacimiento"
  },
  { # formato de campo opcional correcto (los guiones)
    "tipo": "fecha",
    "titulo": "Introduce tu fecha de nacimiento",
    "ultimaFecha": "01-01-2022"
  },
  { # campo opcional correcto
    "tipo": "fecha",
    "titulo": "Introduce tu fecha de nacimiento",
    "primeraFecha": "01/01/1900",
    "ultimaFecha": "1/1/2022" # sólo un dígito. Formato correcto.
  }
]

miDiccionario88 = [
  { # formato de campo opcional incorrecto, formato está al revés.
    "tipo": "fecha",
    "titulo": "Introduce tu fecha de nacimiento",
    "primeraFecha": "1-1-1900", # sólo un dígito con guiones, correcto.
    "ultimaFecha": "2022/01/01" # incorrecto
  }
]

miDiccionario888 = [
  { # campo 'misFechas' no válido
    "tipo": "fecha",
    "titulo": "Introduce tu fecha de nacimiento",
    "misFechas": "2022/01/01"
  }
]

miDiccionario8888 = [
  { # campo no válido
    "tipo": "fecha",
    "titulo": "Introduce tu fecha de nacimiento",
    "ultimaFecha": ["2022/01/01"] # no se puede pasar un array, sólo una string
  }
]

# campo especial
miDiccionario9 = [
  {
    "tipo": "campoEspecial",
    "titulo": "Introduce tu nombre de usuario (aluxxxxxxxxxx)"
    # falta expresión regular
  } 
]

miDiccionario99 = [
  { # correcto
    "tipo": "campoEspecial",
    "titulo": "Introduce tu nombre de usuario (aluxxxxxxxxxx)",
    "expresionRegular": "^alu\d{10}$"
  }
]

miDiccionario999 = [
  { # campo expresión no existe
    "tipo": "campoEspecial",
    "titulo": "Introduce tu nombre de usuario (aluxxxxxxxxxx)",
    "expresion": "^alu\d{10}$"
  }
]

miDiccionario9999 = [
  { # expresión pasada como array de string, no se permite.
    "tipo": "campoEspecial",
    "titulo": "Introduce tu nombre de usuario (aluxxxxxxxxxx)",
    "expresionRegular": ["^alu\d{10}$"]
  }
]




# DE MOMENTO, SÓLO HAY PRUEBAS PARA DEPURAR CON LOS TIPOS GENÉRICOS.
# comprobarDiccionario(miDiccionario0)
# comprobarDiccionario(miDiccionario00)
# comprobarDiccionario(miDiccionario000)

# comprobarDiccionario(miDiccionario1)

# comprobarDiccionario(miDiccionario2)
# comprobarDiccionario(miDiccionario22)

# comprobarDiccionario(miDiccionario3)
# comprobarDiccionario(miDiccionario33)
# comprobarDiccionario(miDiccionario333)
# comprobarDiccionario(miDiccionario3333)

# comprobarDiccionario(miDiccionario4)
# comprobarDiccionario(miDiccionario44)
# comprobarDiccionario(miDiccionario444)

# comprobarDiccionario(miDiccionario5)
# comprobarDiccionario(miDiccionario55)
# comprobarDiccionario(miDiccionario555)

# comprobarDiccionario(miDiccionario6)
# comprobarDiccionario(miDiccionario66)
# comprobarDiccionario(miDiccionario7)
# comprobarDiccionario(miDiccionario77)

# comprobarDiccionario(miDiccionario8)
# comprobarDiccionario(miDiccionario88)
# comprobarDiccionario(miDiccionario888)
# comprobarDiccionario(miDiccionario8888)

# comprobarDiccionario(miDiccionario9)
# comprobarDiccionario(miDiccionario99)
# comprobarDiccionario(miDiccionario999)
# comprobarDiccionario(miDiccionario9999)
