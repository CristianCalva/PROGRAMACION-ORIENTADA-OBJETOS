import tkinter as tk

# Crear la ventana principal
app=tk. Tk()
app.geometry("600x600")
app.title("Interfaz grafica")
app.configure(background="blue")

# Variables
entrada = tk.StringVar(app)
lista_datos = []

# Funcion para agregar datos ala lista
def agregar_datos():
    texto_ingresado=entrada.get()
    if texto_ingresado:
        lista.insert(tk.END,texto_ingresado)
        entrada.set("")
    else:
        print("NO EXISTE DATO")

# Función para limpiar todos los datos de la lista
def limpiar_lista():
    lista.delete(0, tk.END)


# componentes
tk .Label(app,text = "ingrese el valor : ",font=("Arial",18)).pack(pady=10)
tk.Entry(app,fg="black",bg="red",font=("Arial",12), textvariable=entrada).pack(pady=10)
tk.Button(app,text="Agregar",font=("Arial",12),bg="yellow", fg="blue", command=agregar_datos). pack(pady=10)

# # Lista para agregar datos
lista = tk.Listbox(app,font=("Arial",12),width=40,height=20)
lista.pack(pady=10)

# Botón para limpiar todos los datos de la lista
tk.Button(app, text="Limpiar", font=("Arial", 12), bg="green", fg="black", command=limpiar_lista).pack(pady=10)

# Inicia el bucle principal de la aplicación
app.mainloop()
