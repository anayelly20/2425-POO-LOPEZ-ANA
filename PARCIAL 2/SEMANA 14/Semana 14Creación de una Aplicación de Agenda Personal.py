# Tarea: Creación de una Aplicación de Agenda Personal
# Objetivo: Aplicación GUI en Tkinter que permite agregar, ver y eliminar eventos

import tkinter as tk
from tkinter import ttk, messagebox, Menu, scrolledtext

# ===================== FUNCIONES =====================

# Agrega un nuevo evento a la lista
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Campos Vacíos", "Por favor completa todos los campos.")
        return

    tree.insert('', 'end', values=(fecha, hora, descripcion))
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Elimina el evento seleccionado con confirmación
def eliminar_evento():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Ninguna Selección", "Selecciona un evento para eliminar.")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")
    if confirmar:
        tree.delete(seleccionado)

# Acción ficticia del menú
def menu_accion():
    messagebox.showinfo("Menú", "Opción del menú seleccionada")

# Salir de la aplicación
def salir():
    root.quit()

# ===================== VENTANA PRINCIPAL =====================

root = tk.Tk()
root.title("Agenda Personal con Componentes GUI")
root.geometry("800x600")

# ===================== MENÚ SUPERIOR =====================

barra_menu = Menu(root)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=menu_accion)
menu_archivo.add_command(label="Guardar", command=menu_accion)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
root.config(menu=barra_menu)

# ===================== FRAME DE EVENTOS =====================

frame_eventos = tk.LabelFrame(root, text="Eventos Programados", padx=10, pady=10)
frame_eventos.pack(fill="both", expand=True, padx=10, pady=5)

columnas = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(frame_eventos, columns=columnas, show="headings")
for col in columnas:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_eventos, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# ===================== FRAME DE ENTRADA =====================

frame_entrada = tk.LabelFrame(root, text="Agregar Nuevo Evento", padx=10, pady=10, bg="#eef")
frame_entrada.pack(fill=tk.X, padx=10, pady=5)

# Etiqueta y campo de fecha (sustituto de DatePicker)
tk.Label(frame_entrada, text="Fecha (YYYY-MM-DD):", bg="#eef").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5)

# Etiqueta y campo de hora
tk.Label(frame_entrada, text="Hora:", bg="#eef").grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=0, column=3, padx=5)

# Etiqueta y campo de descripción
tk.Label(frame_entrada, text="Descripción:", bg="#eef").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_descripcion = tk.Entry(frame_entrada, width=40)
entry_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# ===================== FRAME DE ACCIONES =====================

frame_acciones = tk.LabelFrame(root, text="Acciones", padx=10, pady=10, bg="#dfd")
frame_acciones.pack(fill=tk.X, padx=10, pady=5)

btn_agregar = tk.Button(frame_acciones, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(side=tk.LEFT, padx=10)

btn_eliminar = tk.Button(frame_acciones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.pack(side=tk.LEFT, padx=10)

btn_salir = tk.Button(frame_acciones, text="Salir", command=salir)
btn_salir.pack(side=tk.RIGHT, padx=10)

# ===================== PANEL EXTRA (OPCIONAL) =====================

panel_extra = tk.LabelFrame(root, text="Panel de Componentes Extras", bg="#ffe", padx=10, pady=10)
panel_extra.pack(fill="both", expand=True, padx=10, pady=5)

# Lista desplegable
tk.Label(panel_extra, text="Seleccione opción:", bg="#ffe").pack(anchor="w")
opciones_combobox = ["Prioridad Alta", "Media", "Baja"]
combobox = ttk.Combobox(panel_extra, values=opciones_combobox)
combobox.current(0)
combobox.pack(fill="x", padx=5, pady=5)

# Área de texto adicional
tk.Label(panel_extra, text="Notas adicionales:", bg="#ffe").pack(anchor="w")
area_texto = scrolledtext.ScrolledText(panel_extra, height=5)
area_texto.pack(fill="both", expand=True, padx=5, pady=5)

# ===================== EJECUCIÓN =====================
root.mainloop()
