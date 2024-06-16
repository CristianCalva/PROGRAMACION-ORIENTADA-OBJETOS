#programacion orientada a objetos

class ClimaDiario:
    def __init__(self):          # Llama al constructor de la clase base
        self.temperaturas = []

    def ingresar_temperaturas(self):
        # Lista de temperaturas predefinidas para los 7 días de la semana
        self.temperaturas = [23.5, 24.0, 22.1, 21.5, 25.3, 24.8, 23.9]  # Aqui se aplica el polimorfismo en protecion de datos

    def calcular_promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)


def main():
    print("Programa para calcular el promedio semanal de temperaturas.")

    # Crear una instancia de ClimaDiario
    clima = ClimaDiario()

    # Ingresar temperaturas diarias
    clima.ingresar_temperaturas()

    # Calcular el promedio semanal
    promedio = clima.calcular_promedio()

    # Mostrar el resultado
    print(f"El promedio semanal de las temperaturas ingresadas es: {promedio:.2f}°C")


# Ejecutar el programa
if __name__ == "__main__":
    main()
