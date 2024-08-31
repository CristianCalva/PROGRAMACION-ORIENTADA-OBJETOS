class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    # Métodos getters y setters
    def get_id(self):
        return self.id_producto

    def set_id(self, id_producto):
        self.id_producto = id_producto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open('Inventario.txt', 'r') as file:
                for line in file:
                    id, nombre, cantidad, precio = line.strip().split(',')
                    self.productos[id] = Producto(id, nombre, int(cantidad), float(precio))
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado, iniciando con inventario vacío.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open('Inventario.txt', 'w') as file:
                for producto in self.productos.values():
                    file.write(f'{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n')
            print("Inventario guardado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El ID del producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_inventario()
            print(f"Producto '{producto.get_nombre()}' añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("El producto no existe.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            self.guardar_inventario()
            print("Producto actualizado exitosamente.")
        else:
            print("El producto no existe.")

    def buscar_productos(self, nombre):
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
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
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Cantidad y precio deben ser números válidos.")

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            try:
                cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no actualizar): ")
                precio = input("Ingrese el nuevo precio (dejar en blanco para no actualizar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Cantidad y precio deben ser números válidos.")

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

if __name__ == "__main__":
    menu()
