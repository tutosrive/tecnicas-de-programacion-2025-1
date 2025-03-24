# **Clase sobre Manipulación de Datos en Python**

## **1. Lectura y escritura por consola**

Concepto:  
La lectura y escritura en consola permite interactuar con el usuario mediante la entrada de datos y la visualización de resultados.

### **Ejemplo en pseudocódigo:**

```pseudocode
Escribir "Ingrese su nombre: "  
Leer nombre  
Escribir "Hola, " + nombre
```

### **Ejemplo en Python:**

```py
nombre = input("Ingrese su nombre: ")  
print("Hola, " + nombre)
```

## **2. Operaciones con cadenas**

Concepto:  
Las cadenas son secuencias de caracteres y se pueden manipular con diversas funciones, como concatenación, búsqueda y reemplazo.

### **Ejemplo en pseudocódigo:**

```pseudocode
cadena <- "Hola Mundo"  
cadena <- Reemplazar(cadena, "Mundo", "Python")  
Escribir "Nueva cadena: " + cadena
```

### **Ejemplo en Python:**

```py
cadena = "Hola Mundo"  
cadena = cadena.replace("Mundo", "Python")  
print("Nueva cadena:", cadena)
```

### **Otras operaciones con cadenas:**

- `split()`: Divide una cadena en una lista de subcadenas basadas en un delimitador.  
- `substring(slice)`: Extrae una parte de la cadena.
- `strip()`: Elimina espacios en blanco al inicio y al final.

```py
texto = "  Python es genial  "  
print(texto.strip())  # "Python es genial"

palabras = "uno,dos,tres".split(",")  
print(palabras)  # ['uno', 'dos', 'tres']

subcadena = texto[2:8]  
print(subcadena)  # "Python"
```

## **3. Documentación de código fuente**

Concepto:  
Documentar el código es importante para su mantenimiento. En Python, se usan comentarios `#` y docstrings `""" """`.

### **Ejemplo en pseudocódigo:**

```pseudocode
// Función que suma dos números  
Funcion Sumar(a, b)  
    Retornar a + b  
Fin Funcion
```

### **Ejemplo en Python:**

```py
def sumar(a, b):  
    """Esta función suma dos números y devuelve el resultado.
    
    Args:
        a (int): Número 1
        b (int): Número 2

    Returns:
        int: Suma de los dos números
    """  
    return a + b

print(sumar(3, 5))
```

## **4. Listas**

Concepto:  
Las listas permiten almacenar y manipular colecciones de datos de forma dinámica.

### **Ejemplo en pseudocódigo:**

```pseudocode
lista <- [10, 20, 30, 40]  
Agregar(lista, 50)  
Eliminar(lista, 20)  
Para cada elemento en lista Hacer  
    Escribir elemento  
Fin Para
```

### **Ejemplo en Python:**

```py
lista = [10, 20, 30, 40]  
lista.append(50)  
lista.remove(20)

for elemento in lista:  
    print(elemento)
```

### **Otras aplicaciones de listas:**

- **Ordenar listas:**  
```py
numeros = [5, 2, 9, 1, 3]  
numeros.sort()  
print(numeros)  # [1, 2, 3, 5, 9]  
```

- **Listas de listas (Matrices):**  
```py
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
print(matriz[1][2])  # 6  
```

- **Filtrar elementos de una lista:**  
```py
numeros = [1, 2, 3, 4, 5, 6]  
pares = list(filter(lambda x: x % 2 == 0, numeros))  
print(pares)  # [2, 4, 6]  
```

- **Comprensión de listas:**  
```py
cuadrados = [x**2 for x in range(10)]  
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
```

## **5. Diversas formas de lectura y escritura a través de archivos**

Concepto:  
En programación, los archivos permiten almacenar datos de forma persistente. Existen operaciones de lectura y escritura en archivos de texto y binarios.

### **Ejemplo en pseudocódigo:**

```pseudocode
Abrir archivo "datos.txt" en modo escritura  
Escribir en archivo "Hola, este es un archivo de texto."  
Cerrar archivo

Abrir archivo "datos.txt" en modo lectura  
Leer contenido del archivo y mostrar en pantalla  
Cerrar archivo
```

### **Ejemplo en Python:**

```py
# Escritura en un archivo  
with open("datos.txt", "w") as archivo:  
    archivo.write("Hola, este es un archivo de texto.n")

# Lectura de un archivo  
with open("datos.txt", "r") as archivo:  
    contenido = archivo.read()  
    print(contenido)
```

Este tema se amplia en la seccion de  ARCHIVOS