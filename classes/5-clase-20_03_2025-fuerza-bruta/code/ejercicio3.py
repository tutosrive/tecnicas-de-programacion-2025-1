"""
Enunciado:
    Dado un conjunto de m elementos realizar un algoritmo el cual calcule todas las
    combinaciones de n elementos SIN repetición.
"""

# Definir el número de elementos en el conjunto
m = 3

# Definir el número de elementos en cada combinación
n = 2

# Elementos del conjunto
elements = ['a', 'b', 'c']

# Función recursiva para generar combinaciones
def generar_combinaciones(elements, combinacion_actual, inicio, n, combinations):
    if len(combinacion_actual) == n:
        combinations.append(combinacion_actual)
        return

    for i in range(inicio, len(elements)):
        nueva_combinacion = combinacion_actual + elements[i]
        generar_combinaciones(elements, nueva_combinacion, i + 1, n, combinations)

# Inicializar combinaciones
combinations = []

# Llamar a la función para generar combinaciones
generar_combinaciones(elements, "", 0, n, combinations)

# Mostrar combinaciones
for combinacion in combinations:
    print(combinacion)