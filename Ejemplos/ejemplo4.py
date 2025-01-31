from tkinter import Tk, Label, Button, Entry, OptionMenu, StringVar

def mostrar_tareas(ventana):
    contenido_nombre = Label(ventana, text="Nombre")
    contenido_nombre.grid(row=2, column=0)
    contenido_prioridad = Label(ventana, text="Prioridad")
    contenido_prioridad.grid(row=2, column=1)
    contenido_estado = Label(ventana, text="Estado")
    contenido_estado.grid(row=2, column=2)
    
    with open("tareas.txt", "r") as archivo:
        tareas = archivo.readlines()
        for i, tarea in enumerate(tareas):
            nombre, prioridad, estado = tarea.split(" - ")
            contenido_nombre = Label(ventana, text=nombre)
            contenido_nombre.grid(row=i + 3, column=0)
            contenido_prioridad = Label(ventana, text=prioridad)
            contenido_prioridad.grid(row=i + 3, column=1)
            contenido_estado = Label(ventana, text=estado)
            contenido_estado.grid(row=i + 3, column=2)
    
def registrar_tarea():
    ventana2.deiconify()

def guardar_tarea():
    nombre_tarea = nombre.get()
    prioridad_tarea = priodidad.get()
    estado_tarea = estado.get()

    if nombre_tarea == "" or prioridad_tarea == "Selecciona la prioridad" or estado_tarea == "Selecciona el estado":
        return
    
    with open("tareas.txt", "a") as archivo:
        archivo.write(f"{nombre_tarea} - {prioridad_tarea} - {estado_tarea}\n")
    ventana2.withdraw()

ventana1 = Tk()
ventana1.title("Lista de tareas")
ventana1.geometry("300x300")

ventana2 = Tk()
ventana2.title("Agregar tarea")
ventana2.geometry("300x200")
ventana2.withdraw()

# Widgets de la ventana 1
nueva_tarea = Button(text="Nueva tarea", command=registrar_tarea)
nueva_tarea.grid(row=0, column=0)

etiqueta1 = Label(ventana1, text="Listado de tareas")
etiqueta1.grid(row=1, column=0)

mostrar_tareas(ventana1)

# Widgets de la ventana 2
etiqueta2 = Label(ventana2, text="Registrar tarea")
etiqueta2.grid(row=0, column=0, columnspan=2)

etiqueta_nombre = Label(ventana2, text="Nombre")
etiqueta_nombre.grid(row=1, column=0)
nombre = Entry(ventana2)
nombre.grid(row=1, column=1)

etiqueta_prioridad = Label(ventana2, text="Prioridad")
etiqueta_prioridad.grid(row=2, column=0)
priodidad = StringVar()
priodidad.set("Selecciona la prioridad")
priodidades = OptionMenu(ventana2, priodidad, "Alta", "Media", "Baja")
priodidades.grid(row=2, column=1)

etiqueta_estado = Label(ventana2, text="Estado")
etiqueta_estado.grid(row=3, column=0)
estado = StringVar()
estado.set("Selecciona el estado")
estados = OptionMenu(ventana2, estado, "Pendiente", "En proceso", "Terminada")
estados.grid(row=3, column=1)

guardar = Button(ventana2, text="Guardar", command=guardar_tarea)
guardar.config(fg="blue")
guardar.grid(row=4, column=0)

canelar = Button(ventana2, text="Cancelar", command=ventana2.withdraw)
canelar.config(fg="red")
canelar.grid(row=4, column=1)

ventana1.mainloop()