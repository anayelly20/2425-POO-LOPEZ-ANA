# Importamos la librería tkinter y el módulo de mensajes
import tkinter as tk
from tkinter import messagebox

# Función para agregar un dato desde el campo de texto a la lista
def agregar_dato():
    dato = entry_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entry_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Creamos la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")
root.geometry("400x300")  # Tamaño de la ventana

# Etiqueta de título
label_titulo = tk.Label(root, text="Ingrese Información:")
label_titulo.pack(pady=5)

# Campo de texto para ingresar datos
entry_dato = tk.Entry(root, width=40)
entry_dato.pack(pady=5)

# Botón para agregar dato
btn_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Lista para mostrar los datos ingresados
lista_datos = tk.Listbox(root, width=50, height=10)
lista_datos.pack(pady=5)

# Botón para limpiar la lista
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Iniciamos el bucle principal de la aplicación
root.mainloop()