class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.informacion = (titulo, autor) # Información del libro almacenada como una tupla

    def __str__(self):
        return f'ISBN: {self.isbn}, Titulo: {self.titulo}, Autor: {self.autor}, Categoria: {self.categoria}'


class Usuario:                # Clase que representa un usuario de la biblioteca
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar los libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        return f'Usuario: {self.nombre}, ID: {self.id_usuario}'


class Biblioteca:   # Clase que representa la biblioteca
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f'El Libro "{libro.titulo}" ya existe.')
        else:
            self.libros[libro.isbn] = libro
            print(f'El Libro "{libro.titulo}" fue agregado.')

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f'El Libro "{libro.titulo}" fue eliminado.')
        else:
            print(f'El Libro con ISBN {isbn} no existe.')

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f'El Usuario "{usuario.nombre}" ya existe.')
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f'El Usuario "{usuario.nombre}" fue agregado al sistema.')

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios.pop(id_usuario)
            print(f'El usuario "{usuario.nombre}" fue dado de baja.')
        else:
            print(f'El usuario con ID {id_usuario} no existe.')

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f'El usuario con ID {id_usuario} no existe.')
        elif isbn not in self.libros:
            print(f'El libro con ISBN {isbn} no existe.')
        else:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.prestar_libro(libro)
            print(f'Al usuario "{usuario.nombre}" le fue prestado el libro "{libro.titulo}".')

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro_a_devolver = None
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    libro_a_devolver = libro
                    break

            if libro_a_devolver:
                usuario.devolver_libro(libro_a_devolver)
                self.libros[isbn] = libro_a_devolver
                print(f'El libro "{libro_a_devolver.titulo}" fue devuelto por "{usuario.nombre}".')
            else:
                print(f'El usuario "{usuario.nombre}" no tiene prestado el libro con ISBN {isbn}.')
        else:
            print(f'Usuario con ID {id_usuario} no encontrado.')

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if (criterio == 'titulo' and valor.lower() in libro.titulo.lower()) or \
                    (criterio == 'autor' and valor.lower() in libro.autor.lower()) or \
                    (criterio == 'categoria' and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)

        if resultados:
            print('Libros encontrados:')
            for libro in resultados:
                print(libro)
        else:
            print(f'No se encontraron libros bajo el criterio: {criterio} con valor "{valor}".')

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f'Libros prestados a "{usuario.nombre}":')
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f'El usuario "{usuario.nombre}" no tiene libros prestados.')
        else:
            print(f'Usuario con ID {id_usuario} no encontrado.')

    # Función del menu de la biblioteca
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Menú de la Biblioteca Digital ---")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados a un usuario")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == '2':
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == '3':
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '4':
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == '5':
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '6':
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == '7':
            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            valor = input(f"Ingrese el {criterio} a buscar: ")
            biblioteca.buscar_libro(criterio, valor)

        elif opcion == '8':
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == '9':
            print("Saliendo del sistema de la biblioteca. ¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 9.")


# Ejecucion el menú
if __name__ == "__main__":
    menu()
