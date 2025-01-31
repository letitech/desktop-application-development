from tkinter import Tk, Label, Button

def creador_botones(ventana):
    lista_botones = []
    for i in range(3):
        for j in range(3):
            boton = Button(ventana, text=f"{i + 1 + j * 3}", command=lambda numero=i + 1 + j * 3: mostrar_numero(numero))
            boton.grid(row=j + 1, column=i + 1)
            lista_botones.append(boton)
    return lista_botones
    
def mostrar_numero(numero):
    contenido = etiqueta.cget("text")
    contenido = contenido + str(numero)
    etiqueta.config(text=contenido)    
        
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("100x100")

etiqueta = Label(ventana)
etiqueta.grid(row=0, column=0, columnspan=3)
creador_botones(ventana)


ventana.mainloop()