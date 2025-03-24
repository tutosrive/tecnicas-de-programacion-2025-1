"""
Enunciado:
    Desarrollar un algoritmo que diga cuántas posibilidades hay y muestre todas las
    posibilidades de otorgar las medallas de Oro, Plata y Bronce en una competencia con n atletas.
"""

def fact(n: int) -> int:
	"""Calcular el factorial de un número n"""
	factorial:int = 0
	# Caso base
	if n == 0 or n == 1:
		factorial = 1
	else:
		# Caso recursivo
		factorial = n * fact(n - 1)
	return factorial

n:int = 3 # Tamaño del conjunto de solución (medallas)
m:int = 4 # Cantidad de candidatos
# Fórmula de la "Variación" (sin repeticiones)
possibilities:int = fact(m) // fact(m - n)

print(f'Hay {possibilities} maneras de otorgar las medallas a los atletas correspondientes')