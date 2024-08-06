# Preguntas de "Si" o "No" para armar los gustos del usuario
preguntas = [
    "¿Tienes habilidades para resolver problemas lógicos? (S/N): ",
    "¿Disfrutas trabajar en equipo? (S/N): ",
    "¿Tienes habilidades artísticas? (S/N): ",
    "¿Te interesan las ciencias? (S/N): ",
    "¿Disfrutas trabajando con números? (S/N): ",
    "¿Te interesa la tecnología y cómo funcionan los dispositivos? (S/N): ",
    "¿Disfrutas investigando y experimentando en el laboratorio? (S/N): ",
    "¿Te gustaría desarrollar nuevos productos o mejorar los existentes? (S/N): ",
    "¿Te sientes atraído/a por el mundo de los negocios y las finanzas? (S/N): ",
    "¿Tienes habilidades para comunicarte y negociar con otras personas? (S/N): ",
    "¿Te atrae el diseño gráfico y la creación visual? (S/N): ",
    "¿Te gusta trabajar con herramientas y software de diseño? (S/N): ",
    "¿Disfrutas creando soluciones estéticas y/o funcionales? (S/N): ",
    "¿Te interesa la biología y la investigación científica? (S/N): ",
    "¿Te gustaría descubrir nuevos conocimientos en el campo de la química? (S/N): ",
    "¿Tienes habilidades para analizar datos y realizar experimentos científicos? (S/N): "
]

# Las preguntas se agrupan dependiendo del area vocacional, donde Sí = 1 y No = 0
carreras = {
    "Ingeniería": [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    "Negocios y Finanzas": [0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    "Arte y Diseño": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    "Ciencias": [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1]
}

# Inicia las puntuaciones
puntuaciones = {carrera: 0 for carrera in carreras}

# Realiza el test comparando las respuestas con la agrupación de area vocacional
for pregunta in preguntas:
    respuesta = input(pregunta)
    for carrera, puntajes in carreras.items():
        if respuesta.lower() == "s":
            puntuaciones[carrera] += puntajes[preguntas.index(pregunta)]

# Obtiene la carrera que más se acerque a la agrupacion de area vocacional
carrera_recomendada = max(puntuaciones, key=puntuaciones.get)

# Muestra cuál carrera se asemeja más por los gustos del usuario
print("Tu carrera recomendada es:", carrera_recomendada)
