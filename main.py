#Juan Carlos Neíl Palacios Escobar -- 202008022
#Joel Juan Pablo Gramajo Chan -- 202008025
import numpy as np
import sqlite3
import sounddevice as sd
import tkinter as tk
from tkinter import ttk
from PDFGenerator import generar_pdf_audiometria

def generar_reporte():
    resultados_audiometria = [
        (250, 10),
        (500, 5),
        (1000, 15),
        (2000, 25),
        (4000, 35),
        (8000, 50)
    ]
    generar_pdf_audiometria(resultados_audiometria)


def play_frequency(frequency:float, duration:float, intensity:float):
    # Generar la señal de audio
    t = np.linspace(0, duration, int(duration * 44100), endpoint=False)
    audio_signal = np.sin(2 * np.pi * frequency * t)*intensity
    
    # Reproducir la señal de audio
    sd.play(audio_signal, 44100)
    sd.wait()

# Creamos la ventana principal
root = tk.Tk()
root.geometry("300x400")
root.title("Audiometro")

# Creamos el Notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Creamos los frames para cada menú
menu1 = ttk.Frame(notebook)
menu2 = ttk.Frame(notebook)
menu3 = ttk.Frame(notebook)
menu4 = ttk.Frame(notebook)

# Añadimos los frames al Notebook con sus respectivas pestañas
notebook.add(menu1, text='Paciente')
notebook.add(menu2, text='Mediciones')
notebook.add(menu3, text='Sesion')
notebook.add(menu4, text='Reporte')

# Creamos los widgets del primer menú
label1 = ttk.Label(menu1, text='Nombre Completo')
label1.pack(pady=5)
entry1 = ttk.Entry(menu1)
entry1.pack(pady=5)
label2 = ttk.Label(menu1, text='Edad')
label2.pack(pady=5)
entry2 = ttk.Entry(menu1)
entry2.pack(pady=5)
label3 = ttk.Label(menu1, text='Email')
label3.pack(pady=5)
entry3 = ttk.Entry(menu1)
entry3.pack(pady=5)
button1 = ttk.Button(menu1, text='Guardar Paciente')
button1.pack(pady=5)

# Creamos los widgets del segundo menú
label3 = ttk.Label(menu2, text='Frecuencia')
label3.pack(pady=5)
entry3 = ttk.Entry(menu2)
entry3.pack(pady=5)
label4 = ttk.Label(menu2, text='Duración')
label4.pack(pady=5)
entry4 = ttk.Entry(menu2)
entry4.pack(pady=5)
label5 = ttk.Label(menu2, text='Intensidad')
label5.pack(pady=5)
entry5 = ttk.Entry(menu2)
entry5.pack(pady=5)
label6 = ttk.Label(menu2, text='Sesión')
label6.pack(pady=5)
entry6 = ttk.Combobox(menu2)
entry6.pack(pady=5)
button2 = ttk.Button(menu2, text='Guardar Medición')
button2.pack(pady=5)

# Creamos los widgets del tercer menú
label8 = ttk.Label(menu3, text='Medico')
label8.pack(pady=5)
entry8 = ttk.Entry(menu3)
entry8.pack(pady=5)
label9 = ttk.Label(menu3, text='Paciente')
label9.pack(pady=5)
entry9 = ttk.Combobox(menu3)
entry9.pack(pady=5)
button3 = ttk.Button(menu3, text='Guardar Sesión')
button3.pack(pady=5)

# Creamos los widgets del cuarto menú
label10 = ttk.Label(menu4, text='Reporte')
label10.pack(pady=5)
button4 = ttk.Button(menu4, text='Generar Reporte', command=generar_reporte)
button4.pack(pady=5)

root.mainloop()