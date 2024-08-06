import sys
import os
def realizar_test():
    # Lista de preguntas
    preguntas = [
        "¿Te gusta resolver problemas prácticos?",
        "¿Disfrutas aprender sobre el cuerpo humano y sus procesos?",
        "¿Tienes habilidades creativas y te gusta el diseño?",
        "¿Te interesa el mundo de los negocios y las finanzas?",
        "¿Te apasiona investigar y contar historias?"
    ]
    respuestas = []
    
    # Realizar el test
    for pregunta in preguntas:
        respuesta = input(pregunta + " (sí/no): ").lower()
        while respuesta != "sí" and respuesta != "no":
            print("Respuesta inválida. Por favor, responde con 'sí' o 'no'.")
            respuesta = input(pregunta + " (sí/no): ").lower()
        respuestas.append(respuesta)

    return respuestas


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)   