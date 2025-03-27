# Taller Fuera Bruta (Parte 2)

## Ejercicio N°6

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

# Ejercicio 9

El problema de las n reinas es un pasatiempo que consiste en poner n reinas en el tablero 
de ajedrez sin que se amenacen. En el juego del ajedrez la reina amenaza a aquellas 
piezas que se encuentren en su misma fila, columna o diagonal. 

Implemente un algoritmo 
por fuerza bruta el cual determine todas las combinaciones posibles que sean solución a 
este juego para un tablero n*n.

**Estrategia**: Inicialmente tendré **n** posibles combinaciones para acomodar la **Reina**,
pero a medida que el algoritmo se ejecuta, las posibilidades se reducen cada vez más, pasando de ser
**n** posibilidades a **n - 1** posibilidades de acomodar a la reina.

**Pre**:

**Pos**: