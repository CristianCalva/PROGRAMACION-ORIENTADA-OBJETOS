# Definición de la clase base
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre # Atributos protegidos, utilizando un guion bajo (_) para indicar encapsulación
        self._edad = edad

    # Método para describir al animal
    def describir(self):
        return f"Animal: {self._nombre}, Edad: {self._edad}"

    # Método que será sobrescrito en la clase derivada (demostración de polimorfismo)
    def sonido(self):
        pass

# Definición de la clase derivada que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self._raza = raza

    # Método para describir al perro, sobrescribe el método de la clase base (polimorfismo)
    def describir(self):
        return f"Perro: {self._nombre}, Edad: {self._edad}, Raza: {self._raza}"

    # Método específico de la clase Perro, sobrescribe el método de la clase base
    def sonido(self):
        return "Guau guau"

# Definición de otra clase derivada que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        self._color = color

    # Método para describir al gato, sobrescribe el método de la clase base (polimorfismo)
    def describir(self):
        return f"Gato: {self._nombre}, Edad: {self._edad}, Color: {self._color}"

    # Método específico de la clase Gato, sobrescribe el método de la clase base
    def sonido(self):
        return "Miau miau"

# Creación de instancias de las clases y demostración de la funcionalidad

# Instancia de Perro
mi_perro = Perro("Toby", 5, "Labrador")
print(mi_perro.describir())
print(mi_perro.sonido())

# Instancia de Gato
mi_gato = Gato("Garfil", 3, "Negro")
print(mi_gato.describir())
print(mi_gato.sonido())

# Ejemplo de polimorfismo
animales = [mi_perro, mi_gato]

for animal in animales:
    print(animal.sonido())  # Demuestra el polimorfismo, llama al método adecuado según la instancia
