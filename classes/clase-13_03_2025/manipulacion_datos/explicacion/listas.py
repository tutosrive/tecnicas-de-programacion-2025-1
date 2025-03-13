"""
Concepto:
Las listas permiten almacenar y manipular colecciones de datos de forma dinámica.

Ejemplo en pseudocódigo:
    lista <- [10, 20, 30, 40]
    Agregar(lista, 50)
    Eliminar(lista, 20)
    Para cada elemento en lista Hacer
        Escribir elemento
    Fin Para

Ejemplo en Python:
    lista = [10, 20, 30, 40]
    lista.append(50)
    lista.remove(20)

    for elemento in lista:
        print(elemento)

Otras aplicaciones de listas:
- **Ordenar listas:**
```python
numeros = [5, 2, 9, 1, 3]
numeros.sort()
print(numeros)  # [1, 2, 3, 5, 9]
```

- **Listas de listas (Matrices):**
```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][2])  # 6
```

- **Filtrar elementos de una lista:**
```python
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]
```

- **Comprensión de listas:**
```python
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
"""

# Crear listas
lista = [10, 20, 30, 40]
lista.append(50)
lista.remove(20)
print(lista)

# Ordenar listas ascendente
numeros = [5, 2, 9, 1, 3]
numeros.sort()
print(numeros)  # [1, 2, 3, 5, 9]

# Listas de listas (matrices)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][2])  # 6

# Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

# Crear listas en una sola línea (comprensión de listas)
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]