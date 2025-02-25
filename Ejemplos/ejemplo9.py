from tkinter import Tk, Label, Button, Entry, ttk, END
from sqlite3 import connect

def conexion_db():
    conexion = connect("lista_tareas.db")
    cursor = conexion.cursor()
    return conexion, cursor

def crear_tabla_db():
    conexion, cursor = conexion_db()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        estado TEXT NOT NULL,
        prioridad TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
    )""")
    conexion.commit()
    conexion.close()
    
def insertar_tarea(nombre, descripcion, estado, prioridad, fecha_creacion):
    conexion, cursor = conexion_db()
    cursor.execute(f"""INSERT INTO tareas (nombre, descripcion, estado, prioridad, fecha_creacion) 
                   VALUES ('{nombre}', '{descripcion}', '{estado}', '{prioridad}', '{fecha_creacion}')""")
    conexion.commit()
    conexion.close()
    
def cargar_tareas(tabla):
    conexion, cursor = conexion_db()
    cursor.execute("SELECT * FROM tareas")
    for fila in tabla.get_children():
        tabla.delete(fila)
    for fila in cursor:
        tabla.insert("", END, text=fila[0], values=fila[1:])
    conexion.close()
    
def guardar():
    nombre = entrada_nombre.get()
    descripcion = entrada_descripcion.get()
    estado = entrada_estado.get()
    prioridad = entrada_prioridad.get()
    fecha_creacion = entrada_fecha_creacion.get()
    insertar_tarea(nombre, descripcion, estado, prioridad, fecha_creacion)
    cargar_tareas(tabla)

def crear_ventana():
    ventana = Tk()
    ventana.title("Aplicación con Tkinter y SQLite3")
    return ventana

def crear_etiqueta(ventana, texto, fila, columna):
    etiqueta = Label(ventana, text=texto)
    etiqueta.grid(row=fila, column=columna)
    return etiqueta

def crear_entrada(ventana, fila, columna):
    entrada = Entry(ventana)
    entrada.grid(row=fila, column=columna)
    return entrada

def crear_boton(ventana, texto, fila, columna, comando):
    boton = Button(ventana, text=texto, command=comando)
    boton.grid(row=fila, column=columna)
    return boton

def crear_tabla(ventana):
    tabla = ttk.Treeview(ventana, columns=5)
    tabla.grid(row=6, column=0, columnspan=2)
    tabla.heading("#0", text="Id")
    tabla.heading("#1", text="Nombre")
    # tabla.heading("#2", text="Descripción")
    # tabla.heading("#3", text="Estado")
    # tabla.heading("#4", text="Prioridad")
    # tabla.heading("#5", text="Fecha de creación")
    return tabla

ventana = crear_ventana()
crear_tabla_db()
crear_etiqueta(ventana, "Nombre:", 0, 0)
entrada_nombre = crear_entrada(ventana, 0, 1)
crear_etiqueta(ventana, "Descripción:", 1, 0)
entrada_descripcion = crear_entrada(ventana, 1, 1)
crear_etiqueta(ventana, "Estado:", 2, 0)
entrada_estado = crear_entrada(ventana, 2, 1)
crear_etiqueta(ventana, "Prioridad:", 3, 0)
entrada_prioridad = crear_entrada(ventana, 3, 1)
crear_etiqueta(ventana, "Fecha de creación:", 4, 0)
entrada_fecha_creacion = crear_entrada(ventana, 4, 1)
crear_boton(ventana, "Guardar", 5, 0, guardar)
tabla = crear_tabla(ventana)
cargar_tareas(tabla)

ventana.mainloop()