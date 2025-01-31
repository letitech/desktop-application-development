from tkinter import Tk, Label, Button, Entry

def validacion():
    usuario = entrada1.get()
    contra = entrada2.get()
    
    if usuario == "" or contra == "":
        etiqueta3.config(text="Rellena todos los campos")
    else:
        if usuario != "admin" or contra != "admin":
            etiqueta3.config(text="Usuario o contraseña inválidos")
        else:
            etiqueta3.config(text=f"Bienvenido {usuario}", fg="green", font=("Arial", 16))

def limpiar():
    entrada1.delete(0, "end")     
    entrada2.delete(0, "end")     

ventana = Tk()
ventana.title("Inicio de sesión")
ventana.geometry("300x200")

etiqueta1 = Label(ventana, text="Usuario")
etiqueta1.pack()

entrada1 = Entry(ventana)
entrada1.pack()

etiqueta2 = Label(ventana, text="Contaseña")
etiqueta2.pack()

entrada2 = Entry(ventana)
entrada2.pack()

etiqueta3 = Label(ventana)
etiqueta3.config(fg="red")
etiqueta3.pack()

boton = Button(ventana, text="Inicio", command=validacion)
boton.pack()
boton2 = Button(ventana, text="Limpiar", command=limpiar)
boton2.pack()

ventana.mainloop()