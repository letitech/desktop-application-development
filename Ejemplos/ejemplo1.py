import tkinter as tk

def mostrar_nombre():
    texto = entrada.get()
    if texto == "":
        etiqueta2["text"] = "Introduce un nombre"
    else:
        etiqueta2["text"] = f"Bienvenido {texto}"
    
# Crear la ventana principal
ventana = tk.Tk()

# Configurar título y tamaño
ventana.title("Mi Primera App")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="Introduce tu nombre")
etiqueta.config(font=("Arial", 16), fg="blue")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack(pady=10)

boton = tk.Button(ventana, text="Enviar", command=mostrar_nombre)
boton.config(bg="gray", fg="white")
boton.pack(pady=10)

etiqueta2 = tk.Label(ventana)
etiqueta2.config(font=("Arial", 20), fg="blue")
etiqueta2.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()