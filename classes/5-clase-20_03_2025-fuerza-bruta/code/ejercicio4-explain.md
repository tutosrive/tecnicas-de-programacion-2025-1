# Explicación del Código

## Enunciado
Para el ejercicio de la **contraseña**, permitir que el usuario defina los caracteres a usar y determine el tamaño de la contraseña. Decir cuántas posibilidades hay y mostrarlas.

## Código

```python
# filepath: ejercicio4.py

"""
Enunciado:
    Para el ejercicio de la **contraseña**, permitir que el usuario defina los caracteres a usar y
    que determine el tamaño de la contraseña. Decir cuantas posibilidades hay y mostrarlas.
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
```

## Explicación

### Comentarios Iniciales
```python
"""
Enunciado:
    Para el ejercicio de la **contraseña**, permitir que el usuario defina los caracteres a usar y
    que determine el tamaño de la contraseña. Decir cuantas posibilidades hay y mostrarlas.
"""
```
- Este bloque de comentarios describe el enunciado del ejercicio.

### Lectura de Entrada
```python
# Leer los caracteres a usar
caracteres: list[str] = list(input("Ingrese los caracteres a usar: "))
```
- `caracteres`: Es una lista de cadenas (`list[str]`) que almacena los caracteres ingresados por el usuario.
- `input("Ingrese los caracteres a usar: ")`: Solicita al usuario que ingrese los caracteres.
- `list(...)`: Convierte la cadena de entrada en una lista de caracteres.

```python
# Leer el tamaño de la contraseña
tamaño: int = int(input("Ingrese el tamaño de la contraseña: "))
```
- `tamaño`: Es un entero (`int`) que almacena el tamaño de la contraseña ingresado por el usuario.
- `input("Ingrese el tamaño de la contraseña: ")`: Solicita al usuario que ingrese el tamaño de la contraseña.
- `int(...)`: Convierte la entrada en un entero.

### Cálculo del Total de Posibilidades
```python
# Calcular el total de posibilidades
total_posibilidades: int = len(caracteres) ** tamaño
```
- `total_posibilidades`: Es un entero (`int`) que almacena el total de posibilidades.
- `len(caracteres)`: Obtiene la longitud de la lista de caracteres.
- `** tamaño`: Eleva la longitud de la lista de caracteres a la potencia del tamaño de la contraseña.

### Función Recursiva para Generar Combinaciones
```python
# Función recursiva para generar combinaciones
def generar_combinaciones(caracteres: list[str], combinacion_actual: str, tamaño: int, combinaciones: list[str]) -> None:
```
- `generar_combinaciones`: Es una función que genera todas las combinaciones posibles de los caracteres.
- `caracteres`: Lista de caracteres a usar.
- `combinacion_actual`: Cadena que almacena la combinación actual.
- `tamaño`: Tamaño de la contraseña.
- `combinaciones`: Lista que almacena todas las combinaciones generadas.
- `-> None`: Indica que la función no retorna ningún valor.

```python
    if len(combinacion_actual) == tamaño:
        combinaciones.append(combinacion_actual)
        return
```
- `if len(combinacion_actual) == tamaño`: Verifica si la longitud de la combinación actual es igual al tamaño de la contraseña.
- `combinaciones.append(combinacion_actual)`: Agrega la combinación actual a la lista de combinaciones.
- `return`: Termina la ejecución de la función.

```python
    for i in range(len(caracteres)):
        nueva_combinacion: str = combinacion_actual + caracteres[i]
        generar_combinaciones(caracteres, nueva_combinacion, tamaño, combinaciones)
```
- `for i in range(len(caracteres))`: Itera sobre cada carácter en la lista de caracteres.
- `nueva_combinacion: str = combinacion_actual + caracteres[i]`: Crea una nueva combinación agregando el carácter actual a la combinación actual.
- `generar_combinaciones(caracteres, nueva_combinacion, tamaño, combinaciones)`: Llama recursivamente a la función con la nueva combinación.

### Inicialización y Llamada a la Función
```python
# Inicializar combinaciones
combinaciones: list[str] = []
```
- `combinaciones`: Es una lista de cadenas (`list[str]`) que almacena todas las combinaciones generadas.

```python
# Llamar a la función para generar combinaciones
generar_combinaciones(caracteres, "", tamaño, combinaciones)
```
- Llama a la función `generar_combinaciones` con la lista de caracteres, una cadena vacía como combinación actual, el tamaño de la contraseña y la lista de combinaciones.

### Mostrar Resultados
```python
# Mostrar el total de posibilidades
print("Total de posibilidades:", total_posibilidades)
```
- Muestra el total de posibilidades calculadas.

```python
# Mostrar combinaciones
for combinacion in combinaciones:
    print(combinacion)
```
- Itera sobre cada combinación en la lista de combinaciones y la imprime.

Este código permite al usuario definir los caracteres a usar y el tamaño de la contraseña, calcula el total de posibilidades y muestra todas las combinaciones posibles mediante la variación combinatoria con repetición.

--- 

# Seguimiento

Claro, aquí tienes el seguimiento detallado de la función recursiva `generar_combinaciones` con los parámetros especificados:

### Ejemplo de Entrada
- `caracteres`: `['a', '1', 'b']`
- `tamaño`: `2`

### Primer Llamado
```python
generar_combinaciones(['a', '1', 'b'], "", 2, [])
```
- `combinacion_actual`: `""`
- `combinaciones`: `[]`

### Iteración 1
- `i = 0`
- `nueva_combinacion = "" + 'a' = "a"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "a", 2, [])
  ```

### Segundo Llamado
```python
generar_combinaciones(['a', '1', 'b'], "a", 2, [])
```
- `combinacion_actual`: `"a"`
- `combinaciones`: `[]`

### Iteración 1
- `i = 0`
- `nueva_combinacion = "a" + 'a' = "aa"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "aa", 2, [])
  ```

### Tercer Llamado
```python
generar_combinaciones(['a', '1', 'b'], "aa", 2, [])
```
- `combinacion_actual`: `"aa"`
- `combinaciones`: `[]`

### Condición de Terminación
- `len("aa") == 2` es `True`
- Agrega `"aa"` a `combinaciones`
- `combinaciones`: `["aa"]`
- Retorna al segundo llamado

### Iteración 2
- `i = 1`
- `nueva_combinacion = "a" + '1' = "a1"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "a1", 2, ["aa"])
  ```

### Cuarto Llamado
```python
generar_combinaciones(['a', '1', 'b'], "a1", 2, ["aa"])
```
- `combinacion_actual`: `"a1"`
- `combinaciones`: `["aa"]`

### Condición de Terminación
- `len("a1") == 2` es `True`
- Agrega `"a1"` a `combinaciones`
- `combinaciones`: `["aa", "a1"]`
- Retorna al segundo llamado

### Iteración 3
- `i = 2`
- `nueva_combinacion = "a" + 'b' = "ab"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "ab", 2, ["aa", "a1"])
  ```

### Quinto Llamado
```python
generar_combinaciones(['a', '1', 'b'], "ab", 2, ["aa", "a1"])
```
- `combinacion_actual`: `"ab"`
- `combinaciones`: `["aa", "a1"]`

### Condición de Terminación
- `len("ab") == 2` es `True`
- Agrega `"ab"` a `combinaciones`
- `combinaciones`: `["aa", "a1", "ab"]`
- Retorna al primer llamado

### Iteración 2
- `i = 1`
- `nueva_combinacion = "" + '1' = "1"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "1", 2, ["aa", "a1", "ab"])
  ```

### Sexto Llamado
```python
generar_combinaciones(['a', '1', 'b'], "1", 2, ["aa", "a1", "ab"])
```
- `combinacion_actual`: `"1"`
- `combinaciones`: `["aa", "a1", "ab"]`

### Iteración 1
- `i = 0`
- `nueva_combinacion = "1" + 'a' = "1a"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "1a", 2, ["aa", "a1", "ab"])
  ```

### Séptimo Llamado
```python
generar_combinaciones(['a', '1', 'b'], "1a", 2, ["aa", "a1", "ab"])
```
- `combinacion_actual`: `"1a"`
- `combinaciones`: `["aa", "a1", "ab"]`

### Condición de Terminación
- `len("1a") == 2` es `True`
- Agrega `"1a"` a `combinaciones`
- `combinaciones`: `["aa", "a1", "ab", "1a"]`
- Retorna al sexto llamado

### Iteración 2
- `i = 1`
- `nueva_combinacion = "1" + '1' = "11"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "11", 2, ["aa", "a1", "ab", "1a"])
  ```

### Octavo Llamado
```python
generar_combinaciones(['a', '1', 'b'], "11", 2, ["aa", "a1", "ab", "1a"])
```
- `combinacion_actual`: `"11"`
- `combinaciones`: `["aa", "a1", "ab", "1a"]`

### Condición de Terminación
- `len("11") == 2` es `True`
- Agrega `"11"` a `combinaciones`
- `combinaciones`: `["aa", "a1", "ab", "1a", "11"]`
- Retorna al sexto llamado

### Iteración 3
- `i = 2`
- `nueva_combinacion = "1" + 'b' = "1b"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "1b", 2, ["aa", "a1", "ab", "1a", "11"])
  ```

### Noveno Llamado
```python
generar_combinaciones(['a', '1', 'b'], "1b", 2, ["aa", "a1", "ab", "1a", "11"])
```
- `combinacion_actual`: `"1b"`
- `combinaciones`: `["aa", "a1", "ab", "1a", "11"]`

### Condición de Terminación
- `len("1b") == 2` es `True`
- Agrega `"1b"` a `combinaciones`
- `combinaciones`: `["aa", "a1", "ab", "1a", "11", "1b"]`
- Retorna al primer llamado

### Iteración 3
- `i = 2`
- `nueva_combinacion = "" + 'b' = "b"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "b", 2, ["aa", "a1", "ab", "1a", "11", "1b"])
  ```

### Décimo Llamado
```python
generar_combinaciones(['a', '1', 'b'], "b", 2, ["aa", "a1", "ab", "1a", "11", "1b"])
```
- `combinacion_actual`: `"b"`
- `combinaciones`: `["aa", "a1", "ab", "1a", "11", "1b"]`

### Iteración 1
- `i = 0`
- `nueva_combinacion = "b" + 'a' = "ba"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "ba", 2, ["aa", "a1", "ab", "1a", "11", "1b"])
  ```

### Undécimo Llamado
```python
generar_combinaciones(['a', '1', 'b'], "ba", 2, ["aa", "a1", "ab", "1a", "11", "1b"])
```
- `combinacion_actual`: `"ba"`
- `combinaciones`: `["aa", "a1", "ab", "1a", "11", "1b"]`

### Condición de Terminación
- `len("ba") == 2` es `True`
- Agrega `"ba"` a `combinaciones`
- `combinaciones`: `["aa", "a1", "ab", "1a", "11", "1b", "ba"]`
- Retorna al décimo llamado

### Iteración 2
- `i = 1`
- `nueva_combinacion = "b" + '1' = "b1"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "b1", 2, ["aa", "a1", "ab", "1a", "11", "1b", "ba"])
  ```

### Duodécimo Llamado
```python
generar_combinaciones(['a', '1', 'b'], "b1", 2, ["aa", "a1", "ab", "1a", "11", "1b", "ba"])
```
- `combinacion_actual`: `"b1"`
- `combinaciones`: `["aa", "a1", "ab", "1a", "11", "1b", "ba"]`

### Condición de Terminación
- `len("b1") == 2` es `True`
- Agrega `"b1"` a `combinaciones`
- `combinaciones`: `["aa", "a1", "ab", "1a", "11", "1b", "ba", "b1"]`
- Retorna al décimo llamado

### Iteración 3
- `i = 2`
- `nueva_combinacion = "b" + 'b' = "bb"`
- Llama recursivamente:
  ```python
  generar_combinaciones(['a', '1', 'b'], "bb", 2, ["aa", "a1", "ab", "1a", "11", "1b", "ba", "b1"])
  ```

### Decimotercer Llamado
```python
generar_combinaciones(['a', '1', 'b'], "bb", 2, ["aa", "a1", "ab", "1a", "11", "1b", "ba", "b1"])
```
- `combinacion_actual`: `"bb"`
- `combinaciones`: `["aa", "a1", "ab", "1a", "11", "1b", "ba", "b1"]`

### Condición de Terminación
- `len("bb") == 2` es `True`
- Agrega `"bb"` a `combinaciones`
- `combinaciones`: `["aa", "a1", "ab", "1a", "11", "1b", "ba", "b1", "bb"]`
- Retorna al primer llamado

### Resultado Final
- `combinaciones`: `["aa", "a1", "ab", "1a", "11", "1b", "ba", "b1", "bb"]`
