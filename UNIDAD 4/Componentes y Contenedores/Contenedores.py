# tkinter






import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import date

# crear la v p
root = tk. Tk()
root.title("Agenda Personal")
root.geometry("800x500")


# crear contenedor
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, columnspan=2,sticky=tk.NSEW)

# Crear funciones
# Agregar el evento

def agregar_evento():
    fecha = data_picker.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    tree.insert("", "end", values=(fecha, hora, descripcion))

# Funcion eliminar evento
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirmacion=messagebox.askyesno("Esta segura de eliminar", "Esta seguro")
    if confirmacion:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Seleccione", "Seleccione un item")


# Crear titulo
titulo = ttk.Label(frame, text="Agenda Personal")
titulo.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)

# Crear etiqueta y l campo de fecha
data_picker = DateEntry(frame, date_pattern="y-mm-dd", width="12")
data_picker.set_date(date.today())
data_picker.grid(row=1, column=0, pady=5)

# Campo para hora
hora_label = ttk.Label(frame, text="Ingrese la hora: ")
hora_label.grid(row=2,column=0,pady=5)

hora_entry = ttk.Entry(frame)
hora_entry.grid(row=2,column=1)
# Realizar la descripcion
descripcion_label = ttk.Label(frame, text="Descripcion")
descripcion_label.grid(row=3,column=0,pady=5)

descripcion_entry = ttk.Entry(frame)
descripcion_entry.grid(row=3,column=1)

# Creacion de bonton para las accion de "Agregar"
agregar_boton = ttk.Button(frame, text="Agregar", command=agregar_evento)
agregar_boton.grid(row=4,column=0,pady=5)


# Eliminar boton
eliminar_boton = ttk.Button(frame, text="Eliminar", command=eliminar_evento)
eliminar_boton.grid(row=4, column=1, pady=5)


# Crear Treeview para mostrar la lista de eventos
tree = ttk.Treeview(frame, columns=("fecha", "hora", "descriccion"), show="headings")
tree.grid(row=5, column=0, columnspan=2, sticky="nsew")

# Botón para salir de la aplicación
salir_boton = ttk.Button(frame, text="Salir", command=root.quit)
salir_boton.grid(row=6, column=1, pady=5)

tree.heading("fecha", text="Fecha")
tree.heading("hora", text="hora")
tree.heading("descriccion", text="descriccion")

root.mainloop()

