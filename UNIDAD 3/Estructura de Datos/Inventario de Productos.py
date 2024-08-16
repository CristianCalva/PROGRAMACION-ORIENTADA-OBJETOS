# Clase Productos de una Tienda

# Inicializa un producto con su ID, nombre, cantidad y precio
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Representación en string del producto para facilitar la visualización
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

# Definición de la clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

        # Productos con ID, nombre, cantidad y precio
        producto1 = Producto("001", "Manzanas", 50, 0.50)
        producto2 = Producto("002", "Plátanos", 30, 0.30)
        producto3 = Producto("003", "Naranjas", 40, 0.60)
        producto4 = Producto("004", "Leche", 20, 1.20)
        producto5 = Producto("005", "Pan", 15, 0.80)

        # Añadiendo productos al inventario
        self.añadir_producto(producto1)
        self.añadir_producto(producto2)
        self.añadir_producto(producto3)
        self.añadir_producto(producto4)
        self.añadir_producto(producto5)

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El ID del producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"Producto '{producto.nombre}' añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado exitosamente.")
        else:
            print("El producto no existe.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].cantidad = nueva_cantidad
            if nuevo_precio is not None:
                self.productos[id_producto].precio = nuevo_precio
            print("Producto actualizado exitosamente.")
        else:
            print("El producto no existe.")

    def buscar_productos(self, nombre):
        encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                encontrados.append(producto)
        if encontrados:
            print("Productos encontrados:")
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            print("Inventario completo:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

# Función principal para manejar la interfaz de usuario
def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no actualizar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no actualizar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_productos(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventarios.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejecutar
if __name__ == "__main__":
    menu()
