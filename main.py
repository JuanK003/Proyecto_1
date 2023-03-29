#Juan Carlos Neíl Palacios Escobar -- 202008022
#Joel Juan Pablo Gramajo Chan -- 202008025

import numpy as np
import sounddevice as sd
import tkinter as tk
from tkinter import ttk
from PDFGenerator import generar_pdf_audiometria
from DatabaseUtils import InsertMedicion

def InserMedicion(frequency:float, duration:float, intensity:float):
    frequency = 2.55
    duration = 1
    intensity = 55
    InsertMedicion(frequency, duration, intensity)

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

# Añadimos los frames al Notebook con sus respectivas pestañas
notebook.add(menu1, text='Mediciones')
notebook.add(menu2, text='Reporte')

# Creamos los widgets del segundo menú
label1 = ttk.Label(menu1, text='Frecuencia')
label1.pack(pady=5)
entry1 = ttk.Entry(menu1)
entry1.pack(pady=5)
label3 = ttk.Label(menu1, text='Duración')
label3.pack(pady=5)
entry2 = ttk.Entry(menu1)
entry2.pack(pady=5)
label4 = ttk.Label(menu1, text='Intensidad')
label4.pack(pady=5)
entry3 = ttk.Entry(menu1)
entry3.pack(pady=5)
button1 = ttk.Button(menu1, text='Guardar Medición', command=InserMedicion(2.55, 7.66, 2))
button1.pack(pady=5)

# Creamos los widgets del cuarto menú
label6 = ttk.Label(menu2, text='Reporte')
label6.pack(pady=5)
button2 = ttk.Button(menu2, text='Generar Reporte', command=generar_reporte)
button2.pack(pady=5)

root.mainloop()