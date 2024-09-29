import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Tareas")

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)  # Permitir añadir tarea al presionar Enter

        # Botón para añadir tareas
        self.add_button = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Botón para marcar como completada
        self.complete_button = tk.Button(master, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar tareas
        self.delete_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(tk.END, f"{task} (completada)")
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()
