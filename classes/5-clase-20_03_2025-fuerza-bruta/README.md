# Taller Fuerza Bruta

> Santiago Rivera Marin 

## Ejercicio 1

Desarrollar un algoritmo que diga cuántas posibilidades hay y muestre todas las posibilidades de otorgar las medallas de **Oro, Plata y Bronce** en una competencia con **n** atletas.

### Pseudocódigo

```pseint
int fact(E int n){
	"""Calcular el factorial de un número n"""
	factorial <- 0
	// Caso base
	SI n = 0 || n = 1 THEN
		factorial <- 1
	SINO
		// Caso recursivo
		factorial <- n * fact(n - 1)
	FIN SI
	RETURN factorial
}

----
// main()

DEFINIR n, m, possibilities COMO ENTERO

// Fórmula de la "Variación" (sin repeticiones)
possibilities <- (fact(m))/fact((m - n))
ESCRIBIR "Hay ", possibilities, " de otorgar las medallas a los atletas correspondientes"
```

## Ejercicio 2

Dado un conjunto de **n** elementos realizar un algoritmo el cual calcule todas las **variaciones combinatorias** de los **n** elementos **con repetición**.

Ejemplo:

`Entrada={a,b,c}`

Salida=

matriz[9][3]
| Columna1 | Columna2 | Columna3 |  
| --- | --- | --- |  
| aaa | baa | caa |  
| aab | bab | cab |  
| aac | bac | cac |  
| aba | bba | cba |  
| abb | bbb | cbb |  
| abc | bbc | cbc |  
| aca | bca | cca |  
| acb | bcb | ccb |  
| acc | bcc | ccc |

### Pseudocódigo

```pseudocode
DEFINIR m, n, col1, col2, col3 repetitions COMO ENTERO
DEFIRNI elements, generator COMO VECTOR[3]
DEFINIR output COMO MATRIZ[m][n]

# Para ciclo principal (i)
m:int <- 9

# Ciclo interno (j)
n:int <- 3

# Elementos con los cuales se trajará
elements <- ['a', 'b', 'c']

# Matriz "vacía" que almacenará la salida
output <- [[None] for _ in range(m)]

# Posiciones para obtener valores
col1 <- 0
col2 <- 0
col3 <- 0

PARA i <- 1 HASTA m CON PASO 1 HACER
	# Tratar de tener un generador (['aaa', 'baa', 'caa'])
	generator <- []
	# 3 Caracteres por cada columna
	PARA j <- 1 HASTA n CON PASO 1 HACER
		# Añadir cada columna al generador
		generator.append(elements[col1] + elements[col2] + elements[col3])
		# En cada vuelta, se muestra el siguiente elemento
		col1 <- col1 + 1
	# Column3 cambia por cada fila
	col3 <- col3 + 1
	# Cuando i es igual a 2 o 5 o 8
	# columna3 se reinicia y columna2 se "mueve" un elemento
	SI i = 2 || i = 5 || i = 8 THEN
		col3 <- 0
		# Cada 3 filas se hace el cambio de la columna 2
		col2 <- col2 + 1
	# "Agregar" el generador en la matriz
	output[i] <- generator
	# Reiniciar valor de col1
	col1 <- 0

ESCRIBIR(output)
```




## Ejercicio 3

Dado un conjunto de **m** elementos realizar un algoritmo el cual calcule todas las **combinaciones** de **n** elementos **SIN** repetición.

Ejemplo:

`Entrada={a,b,c}` la idea es formar tuplas de dos elementos

|Salida|
|--|
|ab|
|ac|
|bc|

### Pseudocódigo

```pseudocode
DEFINIR m, n COMO ENTERO
DEFINIR elements COMO VECTOR[m]
DEFINIR combinations COMO MATRIZ

# Número de elementos en el conjunto
m <- 3

# Número de elementos en cada combinación
n <- 2

# Elementos del conjunto
elements <- ['a', 'b', 'c']

# Función recursiva para generar combinaciones
FUNCION generar_combinaciones(elements, combinacion_actual, inicio, n)
    SI longitud(combinacion_actual) = n ENTONCES
        AGREGAR combinacion_actual A combinations
        RETORNAR
    FIN SI

    PARA i <- inicio HASTA longitud(elements) - 1 HACER
        nueva_combinacion <- combinacion_actual + elements[i]
        generar_combinaciones(elements, nueva_combinacion, i + 1, n)
    FIN PARA
FIN FUNCION

# Inicializar combinaciones
combinations <- []

# Llamar a la función para generar combinaciones
generar_combinaciones(elements, "", 0, n)

# Mostrar combinaciones
PARA cada combinacion EN combinations HACER
    ESCRIBIR combinacion
FIN PARA
```

