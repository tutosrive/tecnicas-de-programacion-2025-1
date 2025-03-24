# Taller Fuerza Bruta

> 55296 - Santiago Rivera Marin 

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

Entrada={a,b,c}

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

a = i; a = ?; a = ?;

9     +  9  +   9  = 27

### Pseudocódigo (No es la versión final... Falta...)

```pseint
int pow(E int base, E int exponent){
	"""Calcular la potencia de un número 'base' elevado a un 'expontent'"
	x <- 1
	PARA i <- 1 HASTA exponent CON PASO 1 HACER
		x <- x * base
	FIN PARA
	RETURN x
}

bool mod(E int dividendo, E int divisor){
	"""Se plantea una manera de saber si el residuo de un dividendo sobre su divisor es 0"""
	cociente <- dividendo / divisor

	// Un cociente entero indica división exacta
	SI data_type(cociente) = 'int' THEN
		RETURN True
	SINO
		RETURN False
	FIN SI
}

---
// main()

DEFINIR m, n, col1, col2, col3 repetitions COMO ENTERO
DEFIRNI input, generator COMO VECTOR[3]
DEFINIR output COMO MATRIZ[m][n]

// Para ciclo principal (i)
m <- 9

// Ciclo interno (j)
n <- 3

// Elementos con los cuales se trajará
input <- ['a', 'b', 'c']

// Cantidad de variaciones que deben resultar (solo para comprobar longitud...)
repetitions <- pow(m, n)

// Posiciones para obtener valores
col1 <- 0
col2 <- 1
col3 <- 0

PARA i <- 1 HASTA m CON PASO 1 HACER
	col1 <- i
	PARA j <- 1 HASTA n CON PASO 1 HACER
		// En cada iteración de "j" columna 3 cambia
		col3 <- j
		// Tratar de tener un generador (['a', 'a', 'a'])
		generator <- [input[col1], input[col2], input[col3]]
	FIN PARA

	SI mod(i, 3) = 0 THEN
		// Cada 3 filas se hace el cambio de la columna 2
		col2 <- col2 + 1

	// "Poner" el generador en la matriz
	output[i] = generator
FIN PARA
```