"""
Enunciado:
    Dado un conjunto de n elementos realizar un algoritmo el cual calcule todas las variaciones
    combinatorias de los n elementos con repetición.
"""

def pow(base:int, exponent:int) -> int:
	"""Calcular la potencia de un número 'base' elevado a un 'expontent'"""
	x:int = 1
	for i in range(exponent):
		x *= base
	return x

# Para ciclo principal (i)
m:int = 9

# Ciclo interno (j)
n:int = 4

# Elementos con los cuales se trajará
elements:list[str] = ['a', 'b', 'c', 'd']

# Matriz "vacía" que almacenará la salida
output: list[list[str]] = [[None] for _ in range(m)]

# Posiciones para obtener valores
col1:int = 0
col2:int = 0
col3:int = 0

for i in range(m):
	# Tratar de tener un generador (['aaa', 'baa', 'caa'])
	generator:list[str] = []
	# 3 Caracteres por cada columna
	for j in range(n):
		# Añadir cada columna al generador
		generator.append(f'{elements[col1]}{elements[col2]}{elements[col3]}')
		# En cada vuelta, se muestra el siguiente elemento
		col1 += 1
	# Column3 cambia por cada fila
	col3 += 1
	# Cuando i es igual a 2 o 5 o 8
	# columna3 se reinicia y columna2 se "mueve" un elemento
	if i in [2, 5, 8]:
		col3 = 0
		# Cada 3 filas se hace el cambio de la columna 2
		col2 += 1
	# "Agregar" el generador en la matriz
	output[i] = generator
	# Reiniciar valor de col1
	col1 = 0

print(output)