"""Interfaz Gráfica:
Utilizar Tkinter para crear la interfaz de usuario.
La aplicación debe tener un campo de entrada (Entry) para escribir nuevas tareas.
Incluir botones para "Añadir Tarea", "Marcar como Completada" y "Eliminar Tarea".
Mostrar las tareas actuales en un componente de lista (p. ej., Listbox o Treeview).

Manejador de Eventos:
Implementar manejadores de eventos para los botones y la entrada de texto.
Permitir la adición de tareas presionando la tecla Enter después de escribir una tarea.
Opcional: Implementar eventos adicionales de tu elección para mejorar la funcionalidad (p. ej)"""

import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista de Tareas
        self.tasks = []

        # Campo de Entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Añadir tarea con la tecla Enter

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind("<Double-Button-1>", self.complete_task)  # Marcar como completada al hacer doble clic

    def add_task(self, event=None):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Error", "No se puede agregar una tarea vacía")

    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = f"{task} (Completada)"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Error", "Por favor, selecciona una tarea para completar")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Error", "Por favor, selecciona una tarea para eliminar")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
