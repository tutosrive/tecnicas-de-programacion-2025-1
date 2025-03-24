"""
Enunciado:
    Para el ejercicio de la **contraseña**, permitir que el usuario defina los caracteres a usar y
    quedetermine el tamaño de la contraseña. Decir cuantas posibilidades hay y mostrarlas.
"""

# Leer los caracteres a usar
caracteres: list[str] = list(input("Ingrese los caracteres a usar: "))

# Leer el tamaño de la contraseña
tamaño: int = int(input("Ingrese el tamaño de la contraseña: "))

# Calcular el total de posibilidades
total_posibilidades: int = len(caracteres) ** tamaño

# Función recursiva para generar combinaciones
def generar_combinaciones(caracteres: list[str], combinacion_actual: str, tamaño: int, combinaciones: list[str]) -> None:
    if len(combinacion_actual) == tamaño:
        combinaciones.append(combinacion_actual)
        return

    for i in range(len(caracteres)):
        nueva_combinacion: str = combinacion_actual + caracteres[i]
        generar_combinaciones(caracteres, nueva_combinacion, tamaño, combinaciones)

# Inicializar combinaciones
combinaciones: list[str] = []

# Llamar a la función para generar combinaciones
generar_combinaciones(caracteres, "", tamaño, combinaciones)

# Mostrar el total de posibilidades
print("Total de posibilidades:", total_posibilidades)

# Mostrar combinaciones
for combinacion in combinaciones:
    print(combinacion)