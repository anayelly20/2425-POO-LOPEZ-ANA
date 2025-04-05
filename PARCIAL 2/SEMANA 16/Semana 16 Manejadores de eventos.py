import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas con Eventos de Teclado y Mouse")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")

        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.add_button = tk.Button(self.button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(self.button_frame, text="Marcar Completada", command=self.mark_completed)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=60, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Instrucciones y eventos del mouse
        self.instructions = tk.Label(root, text="Instrucciones del Mouse:\n"
                                                "• Clic izquierdo: Detecta clic izquierdo.\n"
                                                "• Clic derecho: Detecta clic derecho.\n"
                                                "• Clic de scroll: Detecta clic de la rueda.\n"
                                                "• Mueve el mouse sobre este texto.",
                                     justify=tk.LEFT)
        self.instructions.pack(pady=10)

        # Vinculación de eventos del mouse al label de instrucciones
        self.instructions.bind("<Button-1>", self.on_left_click)
        self.instructions.bind("<Button-2>", self.on_middle_click)
        self.instructions.bind("<Button-3>", self.on_right_click)
        self.instructions.bind("<Enter>", self.on_mouse_enter)
        self.instructions.bind("<Leave>", self.on_mouse_leave)
        self.root.bind("<Motion>", self.on_mouse_move)

        # Mostrar coordenadas del mouse
        self.position_label = tk.Label(root, text="Posición del mouse: x=0, y=0")
        self.position_label.pack()

        # Atajos de teclado
        self.entry.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.mark_completed())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

    def mark_completed(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_list()
        else:
            messagebox.showinfo("Seleccionar tarea", "Selecciona una tarea para marcarla.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_task_list()
        else:
            messagebox.showinfo("Seleccionar tarea", "Selecciona una tarea para eliminarla.")

    def update_task_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display = task["text"]
            if task["completed"]:
                display = f"✔ {display}"
                self.listbox.insert(tk.END, display)
                self.listbox.itemconfig(tk.END, fg="gray", selectforeground="gray")
            else:
                self.listbox.insert(tk.END, display)
                self.listbox.itemconfig(tk.END, fg="black", selectforeground="black")

    # Eventos del mouse
    def on_left_click(self, event):
        self.instructions.config(text="Clic izquierdo detectado.")

    def on_right_click(self, event):
        self.instructions.config(text="Clic derecho detectado.")

    def on_middle_click(self, event):
        self.instructions.config(text="Clic con la rueda detectado.")

    def on_mouse_enter(self, event):
        event.widget.config(bg='lightblue')

    def on_mouse_leave(self, event):
        event.widget.config(bg='SystemButtonFace')

    def on_mouse_move(self, event):
        self.position_label.config(text=f"Posición del mouse: x={event.x}, y={event.y}")

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
