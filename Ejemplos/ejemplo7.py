import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect('lista_tareas.db')

# Crear un cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""CREATE TABLE tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    estado TEXT NOT NULL,
    prioridad TEXT NOT NULL,
    fecha_creacion TEXT NOT NULL
)""")

cursor.execute("""INSERT INTO tareas (nombre, estado, prioridad, fecha_creacion) 
               VALUES ('Tarea 1', 'pendiente', 'alta', '2021-09-01')
               """)

tareas = cursor.execute("""SELECT * FROM tareas""")

print(tareas.fetchall())
conexion.commit()
# Cerrar la conexión
conexion.close()