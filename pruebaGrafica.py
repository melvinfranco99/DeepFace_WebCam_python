import tkinter as tk
from tkinter import messagebox, Menu
import cv2

# Función para mostrar el directo de la WebCam
def verDirectoWebCam():
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0) # Este es el numero que hay que cambiar para cambiar la cama (ir probando 0, 1, 2...)


    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('img', img)
        k = cv2.waitKey(30)
        if k == 27: #27 es la tecla ESC
            break

    cap.release()

    
# Función para mostrar el directo de TAPO
def verDirectoTAPO():
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(2) # Este es el numero que hay que cambiar para cambiar la cama (ir probando 0, 1, 2...)


    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('img', img)
        k = cv2.waitKey(30)
        if k == 27: #27 es la tecla ESC
            break

    cap.release()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica de Prueba")
ventana.geometry("800x300")  # Dimensiones de la ventana

# Crear la barra de menú
menu_barra = Menu(ventana)

# Menú Archivo
menu_archivo = Menu(menu_barra, tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Abrir")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Herramientas
menu_herramientas = Menu(menu_barra, tearoff=0)
menu_herramientas.add_command(label="Configuración")
menu_barra.add_cascade(label="Herramientas", menu=menu_herramientas)

# Menú Documentación
menu_documentacion = Menu(menu_barra, tearoff=0)
menu_documentacion.add_command(label="Guía de Usuario")
menu_barra.add_cascade(label="Documentación", menu=menu_documentacion)

# Menú Ayuda
menu_ayuda = Menu(menu_barra, tearoff=0)
menu_ayuda.add_command(label="Acerca de")
menu_barra.add_cascade(label="Ayuda", menu=menu_ayuda)

# Configurar la barra de menú
ventana.config(menu=menu_barra)

# Crear el botón 
boton_webCam = tk.Button(ventana, text="Comenzar Directo con Reconocimiento Facial en WebCam", command=verDirectoWebCam)
boton_webCam.pack(expand=True)

# Crear el botón en el centro de la ventana
boton_TAPO = tk.Button(ventana, text="Comenzar Directo con Reconocimiento Facial en TAPO", command=verDirectoTAPO)
boton_TAPO.pack(expand=True)

# Ejecutar el bucle principal
ventana.mainloop()
