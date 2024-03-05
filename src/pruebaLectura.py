from lectura import comprobarDiccionario


miDiccionario0 = [
  {"type": "inventado"}
]


miDiccionario1 = [
  {
    "type": "text",
    "title": "Nombre",
    "limit": 20
  },
  { # limite incorrecto
    "type": "text",
    "title": "Nombre",
    "limite": 20
  }
]



miDiccionario2 = [
  {
    "type": "number",
    "title": "Edad",
    "minValue": 0,
    "maxValue": 100
  },
  {  # campo con contenido no válido
    "type": "number",
    "title": "Edad",
    "minimo": "hola"
  }
]


miDiccionario22 = [
  {
    "type": "number",
    "title": "Edad",
    "minValue": 0,
    "maxValue": 100
  },
  {  # campo con contenido no válido
    "type": "number",
    "title": "Edad",
    "minValue": "hola"
  }
]



miDiccionario3 = [
  {
    "type": "multipleChoice",
    "title": "Pregunta multiopción",
    "multipleAnswers": False,
    "choices": [
      {
        "choice": "Opción 1",
        "answer": True
      },
      {
        "choice": "Opción 2",
        "answer": False
      }
    ]
  },
  {
    "title": "Pregunta multiopción",
    "type": "multipleChoice",
    "multipleAnswers": False,
    # falta el campo choices
  }
]

miDiccionario33 = [
  {
    "type": "multipleChoice",
    "title": "Pregunta multiopción",
    "multipleAnswers": "hola",
    "choices": [
      {
        "choice": "Opción 1",
        "answer": True
      },
      {
        "choice": "Opción 2",
        "answer": False
      }
    ]
  }
]

miDiccionario4 = [
  {
    "type": "multipleChoice",
    "title": "Pregunta multiopción",
    "multipleAnswers": False,
    "choices": [
      {
        "choice": "Opción 1"
        # falta campos answer
      },
      {
        "choice": "Opción 2",
        "answer": False
      }
    ]
  }
]



# Comprobamos multiple answers, sólo puede haber una si está a false.
miDiccionario5 = [
  {
    "type": "multipleChoice",
    "title": "Pregunta multiopción",
    "multipleAnswers": False,
    "choices": [
      {
        "choice": "Opción 1",
        "answer": True
      },
      {
        "choice": "Opción 2",
        "answer": False
      },
      {
        "choice": "Opción 3",
        "answer": True # fallo, ya hay 2 correctas
      }
    ]
  }
]




miDiccionario6 = [
  {
    "type": "dropdown",
      "title": "Pregunta desplegable",
      "choices": [
        "Opción 1",
        "Opción 2",
        "Opción 3"
      ]
  },
  {
    "type": "dropdown",
      "title": "Pregunta desplegable",
      "content": [ # nombre del campo incorrecto
        "Opción 1",
        "Opción 2",
        "Opción 3"
      ]
  }
]




miDiccionario7 = [
  {
    "type": "checkbox",
      "title": "Pregunta de selección múltiple",
      "content": [
        "Opción 1",
        "Opción 2",
        "Opción 3"
      ]
  },
  {
    "type": "checkbox",
      "title": "Pregunta de selección múltiple",
      "choices": [ # nombre del campo incorrecto
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