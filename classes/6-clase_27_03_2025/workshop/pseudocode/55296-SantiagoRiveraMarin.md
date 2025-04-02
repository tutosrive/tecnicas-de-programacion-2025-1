# Taller Fuera Bruta (Parte 2)

## Ejercicio 6

Dados 3 vectores de entrada los cuales representar el nombre, valores en “**x**” y “**y**” de unas 
coordenadas de puntos en el plano cartesiano bidimensional, realice un algoritmo por fuerza 
bruta, el cual encuentre los dos puntos más cercanos. La salida del algoritmo debe ser el 
nombre de los 2 puntos cercanos.

**Ejemplo**:

**Entrada**: 

- **nombre**= {A,B,C,D},
- **x**= {3,2,4,-1}
- **y** = {1,5,2,4}

**Salida**: “Los 2 puntos mas cercanos son ”: A,C

---

**Pre**: {
  - `E string points_names[3]`: Nombres de los puntos
  - `E int vals_x[3]`: Valores de **x**
  - `E vals_y[3]`: Valores de **y**

}

**Pos**: Se obtiene y retorna el nombre de los dos puntos más cercanos

**Estrategia**: Se trata de un algoritmo de fuerza bruta que se puede resolver mediante la fórmula de **combinación** esto debido a que la idea es comparar la _diferencia_ entre un punto y otro, en esta comparación no importa el orden, debido a que si comparo la distancia entre el punto **A** y el punto **B** es lo mismo que si comparo la distancia entre el punto **B** y el punto **A**. Mi idea es comparar el **primer punto** con los otros tres puntos, el **segundo punto** con los otros dos puntos y el **tercer punto** con el último punto, no se deben repetir las comparaciones.

### Pseudocódigo

```ts
// Función para encontrar los dos puntos más cercanos
string find_nearest_points(E string points_names[3], E int vals_x[3], E vals_y[3]){
    // Variable de retorno
    names_nearest_points <- ""
    // Distancia mínima entre puntos
    min_distance <- MaxInfinite

    // Recorrer vectores
    PARA i <- 1 HASTA 4 CON PASO 1 HACER
        PARA j <- (i + 1) HASTA 4 CON PASO 1 HACER
            // Potenciar valores a la 2
            pow_x <- pow(vals_x[j] - vals_x[i], 2)
            pow_y <- pow(vals_y[j] - vals_y[i], 2)
            // Calcular la distancia
            // calc_min_distance = √((x2 - x1)² + (y2 - y1)²)
            calc_min_distance <- sqrt(pow_x + pow_y)
            // Comparar distancia actual con las distancias mínima anterior
            SI calc_min_distance < min_distance THEN
                // Nueva distancia mínima
                min_distance <- calc_min_distance
                // Nuevos nombres de puntos (A,D o B,C....)
                names_nearest_points <- points_names[i] + "," + point_names[j]
    
    // Retornar nombres de los puntos concatenados
    RETURN names_nearest_points
}
---
// main()

// Inicialización de variables
nombre <- ['A', 'B', 'C', 'D']
x <- [3, 2, 4, -1]
y <- [1, 5, 2, 4]

names_points <- find_nearest_points(nombre, x, y)
ESCRIBIR "Los 2 puntos más cercanos son: ", names_points
```

## Ejercicio 9

El problema de las n reinas es un pasatiempo que consiste en poner n reinas en el tablero 
de ajedrez sin que se amenacen. En el juego del ajedrez la reina amenaza a aquellas 
piezas que se encuentren en su misma fila, columna o diagonal. 

Implemente un algoritmo 
por fuerza bruta el cual determine todas las combinaciones posibles que sean solución a 
este juego para un tablero n*n.

**Estrategia**: Este algoritmo puede resolverse por medio de una **permutación**, ya que el orden sí importa, además de que en cada combinación resultante las siguientes combinaciones dependerán de la combinación anterior. Se plantea tratar de ir desde 0 hasta n, n veces y cada combinación siguiente tendrá n-1 posibilidades.

**Pre**: {
- `E int n`: Tamaño del tablero

}

**Pos**: Se retorna **vector** con las posibles combinaciones, cada posición del **vector** representa la **fila** y el valor dentro de cada **columna** es la **columna** correspondiente a la **fila**.

```ts
// Función para generar la siguiente permutación en orden lexicográfico
boolean next_permutation(E int arr[], E int n){
    k <- -1
    // Buscar el índice k más grande tal que arr[i] < arr[i+1]
    PARA i <- 0 HASTA n-2 CON PASO 1 HACER
        SI arr[i] < arr[i+1] ENTONCES
            k <- i

    // Si no existe un k válido, es que el arreglo está en orden decreciente
    SI k = -1 ENTONCES
        RETURN false

    l <- -1
    // Buscar el índice l más grande tal que arr[k] < arr[i]
    PARA i <- (k + 1) HASTA n-1 CON PASO 1 HACER
        SI arr[k] < arr[i] ENTONCES
            l <- i

    // Intercambiar arr[k] con arr[l]
    temp <- arr[k]
    arr[k] <- arr[l]
    arr[l] <- temp

    // Invertir el subarreglo desde arr[k+1] hasta arr[n-1]
    inicio <- k + 1
    fin <- n - 1
    MIENTRAS inicio < fin HACER
        temp <- arr[inicio]
        arr[inicio] <- arr[fin]
        arr[fin] <- temp
        inicio <- inicio + 1
        fin <- fin - 1

    RETURN true
}

// Función para imprimir el vector (un número por posición)
void imprimir_vector(E int arr[], E int n){
    PARA i <- 0 HASTA n-1 CON PASO 1 HACER
        ESCRIBIR arr[i] + " "
    ESCRIBIR "\n"
}

// Función para generar todas las permutaciones
// Sin validaciones, sobrescribiendo el mismo vector en cada iteración
void generar_permutaciones(E int n){
    // Declarar el vector permutation de tamaño n
    vector permutation <- nuevoVectorDeTamaño(n)
    // Inicializar el vector con la secuencia 0, 1, 2, ..., n-1
    PARA i <- 0 HASTA n-1 CON PASO 1 HACER
        permutation[i] <- i
    // Imprimir la permutación inicial
    imprimir_vector(permutation, n)
    MIENTRAS next_permutation(permutation, n) HACER
        imprimir_vector(permutation, n)
}

// main()
E int n <- 4  // Tamaño del tablero
generar_permutaciones(n)
```

## Ejercicio 3

Desarrollar un método que retorne **verdadero** si una palabra está en una sopa de letras (la 
cual se debe cargar desde un archivo de texto, los cuales están anexos), de lo contrario 
retornar **falso**.

**Ejemplo**: Palabra buscada **“PERU”**, las palabras solo pueden estar horizontal o vertical.

**Estrategia**: Sea cual sea la estructura de los archivos, pienso obtener formar una matriz de filas y columnas, luego una vez formada la matriz recorreré y formaré una palabra del mismo tamaño que la palabra buscada por medio de **fuerza bruta** (Formando todas las posibles combinaciones), una vez formada la combinación se compara con la palabra buscada, si son iguales se retorna **True** sino, se retorna **False**.