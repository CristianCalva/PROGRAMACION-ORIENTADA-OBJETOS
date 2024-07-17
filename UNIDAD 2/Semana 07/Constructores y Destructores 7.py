# Ejemplo de Constructores y Destructores
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo         # Inicialización de atributos en el constructor
        self.año = año
        print(f"mi vehículo {self.año} {self.marca} {self.modelo}.")

    def __del__(self):              # Limpieza o iliminacion de recursos en el destructor
        print(f"mi vehículo {self.año} {self.marca} {self.modelo} está siendo eliminado...")

# Ejemplo de uso
coche1 = Vehiculo("Toyota", "Hilux", 2023)

# Simulación de finalización del programa (esto activará el destructor)
del coche1
