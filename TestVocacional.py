import tkinter as tk
from PIL import ImageTk, Image
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def realizar_test():
    global pregunta_idx, respuestas, label_pregunta, btn_si, btn_no, label_titulo

    # Ocultar el botón de "Comenzar Test" y mostrar el título
    btn_comenzar.pack_forget()
    label_titulo.pack()

    # Inicializar variables
    pregunta_idx = 0
    respuestas = []

    # Configurar la interfaz para la primera pregunta
    label_pregunta.config(text=preguntas[pregunta_idx])
    btn_si.pack()
    btn_no.pack()

def responder(respuesta):
    global pregunta_idx, respuestas, label_pregunta, btn_si, btn_no, btn_repetir

    # Guardar la respuesta
    respuestas.append(respuesta)

    # Pasar a la siguiente pregunta
    pregunta_idx += 1

    if pregunta_idx < len(preguntas):
        label_pregunta.config(text=preguntas[pregunta_idx])
    else:
        # Todas las preguntas han sido respondidas
        carrera_sugerida = determinar_carrera(respuestas)
        mostrar_resultado(carrera_sugerida)

def determinar_carrera(respuestas):
    puntajes = {
        "Ingeniería": 0,
        "Medicina": 0,
        "Artes y Diseño": 0,
        "Negocios y Finanzas": 0,
        "Periodismo": 0
    }

    # Incrementar los puntajes según las respuestas
    for i, respuesta in enumerate(respuestas):
        if respuesta == "sí":
            if i == 0:
                puntajes["Ingeniería"] += 1
            elif i == 1:
                puntajes["Medicina"] += 1
            elif i == 2:
                puntajes["Artes y Diseño"] += 1
            elif i == 3:
                puntajes["Negocios y Finanzas"] += 1
            elif i == 4:
                puntajes["Periodismo"] += 1

    # Determinar la carrera con el puntaje máximo
    carrera_sugerida = max(puntajes, key=puntajes.get)
    return carrera_sugerida

def mostrar_resultado(carrera_sugerida):
    # Ocultar botones de respuesta
    btn_si.pack_forget()
    btn_no.pack_forget()

    # Mostrar resultado
    label_pregunta.config(text=f"¡Test Finalizado!\nTu carrera sugerida es: {carrera_sugerida}")

    # Mostrar imagen correspondiente a la carrera sugerida
    try:
        if carrera_sugerida == "Ingeniería":
            imagen = Image.open(resource_path("IMG/ingeniero.png"))
        elif carrera_sugerida == "Medicina":
            imagen = Image.open(resource_path("IMG/medico.png"))
        elif carrera_sugerida == "Artes y Diseño":
            imagen = Image.open(resource_path("IMG/arte.JPG"))
        elif carrera_sugerida == "Negocios y Finanzas":
            imagen = Image.open(resource_path("IMG/negocios.PNG"))
        elif carrera_sugerida == "Periodismo":
            imagen = Image.open(resource_path("IMG/periodismo.PNG"))

        imagen = imagen.resize((300, 300))

        imagen_tk = ImageTk.PhotoImage(imagen)
        imagen_label.config(image=imagen_tk)
        imagen_label.image = imagen_tk
        imagen_label.pack(pady=10)

        # Mostrar botón para repetir el test
        btn_repetir.pack(pady=10)

    except Exception as e:
        print("Error al cargar la imagen:", e)

def repetir_test():
    # Reiniciar la aplicación
    imagen_label.pack_forget()
    btn_repetir.pack_forget()
    realizar_test()

# Lista de preguntas
preguntas = [
    "¿Te gusta resolver problemas prácticos?",
    "¿Disfrutas aprender sobre el cuerpo humano y sus procesos?",
    "¿Tienes habilidades creativas y te gusta el diseño?",
    "¿Te interesa el mundo de los negocios y las finanzas?",
    "¿Te apasiona investigar y contar historias?"
]

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Test Vocacional")

# Título grande
label_titulo = tk.Label(ventana, text="Test de Python", font=("Helvetica", 24, "bold"))
label_titulo.pack(pady=10)

# Etiqueta para mostrar las preguntas
label_pregunta = tk.Label(ventana, text="Haz clic en 'Comenzar Test' para empezar", wraplength=400, font=("Helvetica", 14))
label_pregunta.pack(pady=20)

# Botones de respuesta
btn_si = tk.Button(ventana, text="Sí", command=lambda: responder("sí"), font=("Helvetica", 12), width=10, bg="#4CAF50", fg="white")
btn_no = tk.Button(ventana, text="No", command=lambda: responder("no"), font=("Helvetica", 12), width=10, bg="#F44336", fg="white")

# Botón para comenzar el test
btn_comenzar = tk.Button(ventana, text="Comenzar Test", command=realizar_test, font=("Helvetica", 14), width=20, bg="#2196F3", fg="white")
btn_comenzar.pack(pady=20)

# Etiqueta para mostrar la imagen
imagen_label = tk.Label(ventana)

# Botón para repetir el test
btn_repetir = tk.Button(ventana, text="Repetir Test", command=repetir_test, font=("Helvetica", 14), width=20, bg="#FFC107", fg="black")

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
