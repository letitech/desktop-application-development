from tkinter import Tk, Menu, Text

def nuevo():
    texto.delete("1.0", "end")

def guardar():
    contenido = texto.get("1.0", "end-1c")
    with open("archivo.txt", "w") as archivo:
        archivo.write(contenido)

ventana = Tk()
ventana.title("Bloc de Notas")
ventana.geometry("400x400")

menu_principal = Menu(ventana)
ventana.config(menu=menu_principal)

menu_archivo = Menu(menu_principal, tearoff=0)
menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+N", command=nuevo)
menu_archivo.add_command(label="Abrir", accelerator="Ctrl+O")
menu_archivo.add_command(label="Guardar", accelerator="Ctrl+S", command=guardar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", accelerator="Ctrl+Q", command=ventana.quit)

menu_editar = Menu(menu_principal, tearoff=0)
menu_editar.add_command(label="Cortar", accelerator="Ctrl+X")
menu_editar.add_command(label="Copiar", accelerator="Ctrl+C")
menu_editar.add_command(label="Pegar", accelerator="Ctrl+V")

menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_principal.add_cascade(label="Editar", menu=menu_editar)

texto = Text(ventana)
texto.pack(expand=True, fill="both")

ventana.bind("<Control-n>", lambda e: nuevo())
ventana.bind("<Control-o>", lambda e: print("Abrir"))
ventana.bind("<Control-s>", lambda e: guardar())
ventana.bind("<Control-q>", lambda e: ventana.quit())

ventana.mainloop()