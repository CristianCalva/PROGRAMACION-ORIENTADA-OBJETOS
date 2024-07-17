# calcular el are de un triangulo

def calcular_area_triangulo(base, altura):
    area = base * altura / 2
    return area

# Variables
base_triangulo = 6    # Tipo integer
altura_triangulo = 8  # Tipo interger

# Llamada a la función para calcular el área del triángulo
area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)

# Imprimir el área del triángulo
print(f'El área del triángulo con base {base_triangulo} y altura {altura_triangulo} es: {area_triangulo}')

# Ejemplo de variable tipo boolean
es_grande = area_triangulo > 20

# Imprimir otros tipos de datos
print(f'¿Es el área del triángulo mayor que 20? {es_grande}')