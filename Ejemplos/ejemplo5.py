from tkinter import Tk, Label, Entry, Button

def mostrar():
    contenido = entrada.get()
    etiqueta2.config(text=contenido, fg="green", font=("Arial", 16))
    
ventana = Tk()

etiqueta1 = Label(ventana, text="Bienvenido")
etiqueta1.pack()

entrada = Entry(ventana)
entrada.pack()

boton = Button(ventana, text="Enviar", command=mostrar)
boton.pack()

etiqueta2 = Label(ventana, text="")
etiqueta2.pack()


ventana.mainloop()