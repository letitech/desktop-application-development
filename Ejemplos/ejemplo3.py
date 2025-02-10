from tkinter import Tk, Label, Button

def creador_botones(ventana):
    lista_botones = []
    for i in range(3):
        for j in range(3):
            boton = Button(ventana, text=f"{i + 1 + j * 3}", command=lambda numero=i + 1 + j * 3: mostrar_numero(numero))
            boton.grid(row=j + 1, column=i + 1)
            lista_botones.append(boton)
            
    boton_suma = Button(ventana, text="+", command=lambda: mostrar_numero("+"))
    boton_suma.grid(row=1, column=4)
    boton_resta = Button(ventana, text="-", command=lambda: mostrar_numero("-"))
    boton_resta.grid(row=2, column=4)
    boton_multiplicacion = Button(ventana, text="*", command=lambda: mostrar_numero("*"))
    boton_multiplicacion.grid(row=3, column=4)
    boton_division = Button(ventana, text="/", command=lambda: mostrar_numero("/"))
    boton_division.grid(row=4, column=4)
    boton_igual = Button(ventana, text="=", command=calcular)
    boton_igual.grid(row=4, column=3)
    boton_cero = Button(ventana, text="0", command=lambda: mostrar_numero(0))
    boton_cero.grid(row=4, column=2)
    boton_limpiar = Button(ventana, text="C", command=limpiar)
    boton_limpiar.grid(row=4, column=1)
    lista_botones.append(boton_suma)
    lista_botones.append(boton_resta)
    lista_botones.append(boton_multiplicacion)
    lista_botones.append(boton_division)
    lista_botones.append(boton_igual)
    lista_botones.append(boton_cero)
    lista_botones.append(boton_limpiar)
    
    return lista_botones
  
def mostrar_numero(numero):
    contenido = etiqueta.cget("text")
    contenido = contenido + str(numero)
    etiqueta.config(text=contenido)
    
def limpiar():
    etiqueta.config(text="")
    
def calcular():
    contenido = etiqueta.cget("text")
    resultado = eval(contenido) 
    etiqueta.config(text=resultado)
  
        
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("100x150")

etiqueta = Label(ventana)
etiqueta.grid(row=0, column=0, columnspan=4)
creador_botones(ventana)



ventana.mainloop()