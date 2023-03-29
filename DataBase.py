import sqlite3

# Creamos una conexión a la base de datos
conn = sqlite3.connect('database_Project.db')

# Creamos una tabla llamada "Mediciones"
conn.execute('''
             CREATE TABLE IF NOT EXISTS Mediciones
             (
                 id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 frecuencia FLOAT NOT NULL,
                 duracion FLOAT NOT NULL,
                 intensidad FLOAT NOT NULL,
                 createdAt DATETIME,
                 updatedAt DATETIME
             );
             ''')

# Agregamos un usuario a la tabla
conn.execute("INSERT INTO Mediciones (frecuencia, duracion, intensidad) VALUES (25.11, 55.01, 40)")

# Guardamos los cambios
conn.commit()

# Consultamos los usuarios en la tabla
cursor = conn.execute("SELECT * from Mediciones")
for fila in cursor:
    print(fila)

# Cerramos la conexión
conn.close()
