import os

# Función para mostrar el código de un script dado su ruta
def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():                # Función para mostrar el menú y manejar las elecciones del usuario
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {                    # Define las opciones del menú con rutas relativas de los scripts
        '1': 'UNIDAD 1/Semana 02/Tecnica de Abstraccion/abstraccion.py',
        '2': 'UNIDAD 1/Semana 02/Tecnica de Encapsulacion/encapsulacion.py',
        '3': 'UNIDAD 1/Semana 02/Tecnica de Herencia/herencia.py',
        '4': 'UNIDAD 1/Semana 02/Tecnica de Polimorfismo/polimorfismo.py',
        '5': 'UNIDAD 1/Semana 03/programacion Poo.py',
        '6': 'UNIDAD 1/Semana 03/programacion tradicional.py',
        '7': 'UNIDAD 1/Semana 04/Ejemplos de mundo real/cuenta_bancaria.py',
        '8': 'UNIDAD 2/Semana 05/tipo de datos, identificadores.py',
        '9': 'UNIDAD 2/Semana 06/objetos, clases, herencia y polimorfirmos.py',
        '10': 'UNIDAD 2/Semana 07/Constructores y Destructores 7.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

        # Ejecutar el dashboard si este archivo se ejecuta como un script
# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()