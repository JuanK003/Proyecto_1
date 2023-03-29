import sqlite3
from datetime import datetime

def InsertMedicion(frecuencia, duracion, intensidad):
    conn = sqlite3.connect('database_Project.db')
    c = conn.cursor()

    medicion = (frecuencia, duracion, intensidad, datetime.now(), datetime.now())

    c.execute(f"INSERT INTO Mediciones (frecuencia, duracion, intensidad, createdAt, updatedAt) VALUES ({frecuencia}, {duracion}, {intensidad}, '{datetime.now()}', '{datetime.now()}')")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    pass