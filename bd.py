import sqlite3

# Creamos una conexión a la base de datos
conn = sqlite3.connect('BD.db')

# Creamos una tabla llamada "Paciente"
conn.execute('''
             CREATE TABLE Paciente
             (
                 id INT AUTO_INCREMENT,
                 nombreCompleto TEXT(1024) NOT NULL,
                 edad INT NOT NULL,
                 email TEXT NOT NULL,
                 createdAt DATETIME,
                 updatedAt DATETIME,
                 PRIMARY KEY(id)
             );
             ''')

# Creamos una tabla llamada "Sesion"
conn.execute('''
             CREATE TABLE Sesion
             (
                 id INT AUTO_INCREMENT,
                 medico TEXT(1024) NOT NULL,
                 Paciente_ID INT NOT NULL,
                 createdAt DATETIME,
                 updatedAt DATETIME,
                 PRIMARY KEY(id),
                 FOREIGN KEY(Paciente_ID) REFERENCES Paciente(id)
             );
             ''')

# Creamos una tabla llamada "Mediciones"
conn.execute('''
             CREATE TABLE Mediciones
             (
                 id INT AUTO_INCREMENT,
                 frecuencia FLOAT NOT NULL,
                 duracion FLOAT NOT NULL,
                 intensidad FLOAT NOT NULL,
                 Sesion_ID INT NOT NULL,
                 createdAt DATETIME,
                 updatedAt DATETIME,
                 PRIMARY KEY(id),
                 FOREIGN KEY(Sesion_ID) REFERENCES Sesion(id)
             );
             ''')

# Agregamos un usuario a la tabla
conn.execute("INSERT INTO Paciente (nombreCompleto, edad, email) VALUES ('Pedro', 19, 'pedi@gmail.com')")

# Guardamos los cambios
conn.commit()

# Consultamos los usuarios en la tabla
cursor = conn.execute("SELECT * from Paciente")
for fila in cursor:
    print(fila)

# Cerramos la conexión
conn.close()