#Programacion Tradicional

# Esta función solicita al usuario que ingrese las temperaturas diarias para 7 días
def ingresar_temperaturas():
    # Lista de temperaturas predefinidas para los 7 días de la semana
    temperaturas = [23.5, 24.0, 22.1, 21.5, 25.3, 24.8, 23.9]
    return temperaturas

# Esta función calcula y retorna el promedio de una lista de temperaturas
def calcular_promedio(temperaturas):
    if not temperaturas:
        return 0
    return sum(temperaturas) / len(temperaturas)


def main():
    print("Programa para calcular el promedio semanal de temperaturas.")

    # Llama a la función para ingresar las temperaturas diarias
    temperaturas = ingresar_temperaturas()

    # Llama a la función para calcular el promedio semanal
    promedio = calcular_promedio(temperaturas)

    # Muestra el resultado del promedio semanal
    print(f"El promedio semanal de las temperaturas ingresadas es: {promedio:.2f}°C")


# Ejecuta el programa
if __name__ == "__main__":
    main()
