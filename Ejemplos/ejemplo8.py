from tkinter import Tk, Label, Button, Entry, ttk, END
from sqlite3 import connect

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Aplicación con Tkinter y SQLite3")
        self.etiqueta = Label(ventana, text="Id:")
        self.etiqueta.grid(row=0, column=0)
        self.nombre = Entry(ventana)
        self.nombre.grid(row=0, column=1)
        self.etiqueta = Label(ventana, text="Nombre:")
        self.etiqueta.grid(row=1, column=0)
        self.edad = Entry(ventana)
        self.edad.grid(row=1, column=1)
        self.boton = Button(ventana, text="Guardar", command=self.guardar)
        self.boton.grid(row=2, column=0, columnspan=2)
        self.tabla = ttk.Treeview(ventana, columns=2)
        self.tabla.grid(row=3, column=0, columnspan=2)
        self.tabla.heading("#0", text="Id")
        self.tabla.heading("#1", text="Nombre")
        self.cargar()

    def guardar(self):
        conexion = connect("lista_tareas.db")
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            estado TEXT NOT NULL,
            prioridad TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL
        )""")
        cursor.execute("INSERT INTO tareas VALUES (?, ?, ?, ?, ?)", (self.nombre.get(), self.edad.get()))
        conexion.commit()
        conexion.close()
        self.cargar()

    def cargar(self):
        conexion = connect("lista_tareas.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tareas")
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for fila in cursor:
            self.tabla.insert("", END, text=fila[0], values=fila[1])
        conexion.close()
        
ventana = Tk()
app = Aplicacion(ventana)
ventana.mainloop()