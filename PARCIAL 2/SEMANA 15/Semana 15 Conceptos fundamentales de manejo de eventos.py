import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    """Agrega una nueva tarea a la lista si el campo de entrada no está vacío."""
    tarea = entrada_tarea.get().strip()  # Obtener texto y eliminar espacios en blanco
    if tarea:
        lista_tareas.insert(tk.END, tarea)  # Añadir tarea al final de la lista
        entrada_tarea.delete(0, tk.END)  # Limpiar campo de entrada
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

def marcar_completada():
    """Marca la tarea seleccionada como completada agregando un símbolo de verificación."""
    try:
        seleccion = lista_tareas.curselection()[0]  # Obtener índice de la tarea seleccionada
        tarea = lista_tareas.get(seleccion)  # Obtener el texto de la tarea
        if not tarea.startswith("✔ "):
            lista_tareas.delete(seleccion)  # Eliminar tarea de la lista
            lista_tareas.insert(seleccion, f"✔ {tarea}")  # Volver a insertarla con marca de completada
        else:
            messagebox.showinfo("Información", "Esta tarea ya está marcada como completada")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

def eliminar_tarea():
    """Elimina la tarea seleccionada de la lista."""
    try:
        seleccion = lista_tareas.curselection()[0]  # Obtener índice de la tarea seleccionada
        lista_tareas.delete(seleccion)  # Eliminar la tarea de la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

def agregar_con_enter(event):
    """Permite agregar una tarea presionando la tecla Enter."""
    agregar_tarea()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")  # Título de la ventana
ventana.geometry("400x400")  # Tamaño de la ventana
ventana.resizable(False, False)  # Evitar que la ventana cambie de tamaño

# Etiqueta para el campo de entrada
etiqueta = tk.Label(ventana, text="Nueva Tarea:", font=("Arial", 12))
etiqueta.pack(pady=5)

# Campo de entrada de texto
entrada_tarea = tk.Entry(ventana, width=50, font=("Arial", 10))
entrada_tarea.pack(pady=5)
entrada_tarea.bind("<Return>", agregar_con_enter)  # Asociar tecla Enter con agregar tarea

# Botón para agregar tareas
boton_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea, width=20, font=("Arial", 10), bg="#4CAF50", fg="white")
boton_agregar.pack(pady=5)

# Botón para marcar tarea como completada
boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada, width=20, font=("Arial", 10), bg="#2196F3", fg="white")
boton_completar.pack(pady=5)

# Botón para eliminar tarea
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea, width=20, font=("Arial", 10), bg="#f44336", fg="white")
boton_eliminar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15, font=("Arial", 10))
lista_tareas.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

