from lectura import comprobarDiccionario


miDiccionario0 = [
  {"tipo": "inventado"}
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
  {
    "tipo": "opcionMultiple",
    "titulo": "Pregunta multiopción",
    "opcionMultiple": False,
    "opciones": [
      {
        "opcion": "Opción 1",
        "answer": True
      },
      {
        "opcion": "Opción 2",
        "answer": False
      }
    ]
  },
  {
    "titulo": "Pregunta multiopción",
    "tipo": "opcionMultiple",
    "opcionMultiple": False,
    # falta el campo opciones
  }
]

miDiccionario33 = [
  {
    "tipo": "opcionMultiple",
    "titulo": "Pregunta multiopción",
    "opcionMultiple": "hola",
    "opciones": [
      {
        "opcion": "Opción 1",
        "answer": True
      },
      {
        "opcion": "Opción 2",
        "answer": False
      }
    ]
  }
]

miDiccionario4 = [
  {
    "tipo": "opcionMultiple",
    "titulo": "Pregunta multiopción",
    "opcionMultiple": False,
    "opciones": [
      {
        "opcion": "Opción 1"
        # falta campos answer
      },
      {
        "opcion": "Opción 2",
        "answer": False
      }
    ]
  }
]



# Comprobamos multiple answers, sólo puede haber una si está a false.
miDiccionario5 = [
  {
    "tipo": "opcionMultiple",
    "titulo": "Pregunta multiopción",
    "opcionMultiple": False,
    "opciones": [
      {
        "opcion": "Opción 1",
        "answer": True
      },
      {
        "opcion": "Opción 2",
        "answer": False
      },
      {
        "opcion": "Opción 3",
        "answer": True # fallo, ya hay 2 correctas
      }
    ]
  }
]




miDiccionario6 = [
  {
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




miDiccionario7 = [
  {
    "tipo": "casilla",
      "titulo": "Pregunta de selección múltiple",
      "content": [
        "Opción 1",
        "Opción 2",
        "Opción 3"
      ]
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



# DE MOMENTO, SÓLO HAY PRUEBAS PARA DEPURAR CON LOS TIPOS GENÉRICOS.
# comprobarDiccionario(miDiccionario0)
# comprobarDiccionario(miDiccionario1)
# comprobarDiccionario(miDiccionario2)
# comprobarDiccionario(miDiccionario22)
# comprobarDiccionario(miDiccionario3)
# comprobarDiccionario(miDiccionario33)
# comprobarDiccionario(miDiccionario4)
# comprobarDiccionario(miDiccionario5)
# comprobarDiccionario(miDiccionario6)
# comprobarDiccionario(miDiccionario7)