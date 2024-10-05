""" Interfaz Gráfica:

    Utilizar Tkinter para crear la interfaz de usuario.
    Implementar un campo de entrada (Entry) para añadir nuevas tareas.
    Incluir botones para añadir tareas, marcar como completadas, y eliminar tareas.
    Mostrar las tareas en una lista o algún componente adecuado.

Manejo de Eventos de Clic:

    Asignar funciones que se ejecutarán cuando los usuarios interactúen con los botones.

Atajos de Teclado:

    Permitir añadir una nueva tarea presionando la tecla "Enter" después de escribir en el campo de entrada.
    Implementar un atajo de teclado para marcar la tarea seleccionada como completada (por ejemplo, tecla "C").
    Implementar un atajo de teclado para eliminar la tarea seleccionada (por ejemplo, tecla "Delete" o "D").
    Permitir cerrar la aplicación usando la tecla "Escape".
"""


import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x500")

        # Lista de Tareas
        self.tasks = []

        # Campo de Entrada
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        # Añadir tarea al presionar "Enter"
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Lista de Tareas
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(pady=10)

        # Botones
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=10)

        self.complete_button = tk.Button(self.root, text="Completar Tarea", command=self.complete_task)
        self.complete_button.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=10)

        # Atajos del Teclado
        root.bind("<c>", lambda event: self.complete_task())  # Completar tarea con la tecla "C"
        root.bind("<d>", lambda event: self.delete_task())  # Eliminar tarea con la tecla "D"
        root.bind("<Delete>", lambda event: self.delete_task())  # Eliminar tarea con la tecla "Delete"
        root.bind("<Escape>", lambda event: self.root.quit())  # Cerrar la aplicación con "Escape"

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada después de agregar
        else:
            messagebox.showerror("Error", "No se puede añadir una tarea vacía")

    def complete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.update_task_listbox()
        else:
            messagebox.showerror("Error", "No se ha seleccionado ninguna tarea para completar")

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showerror("Error", "No se ha seleccionado ninguna tarea para eliminar")

    def update_task_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display_task = task["task"]
            if task["completed"]:
                display_task += " (Completada)"
            self.listbox.insert(tk.END, display_task)

if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()
