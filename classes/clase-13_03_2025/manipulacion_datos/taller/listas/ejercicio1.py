"""
Enunciado:
    Lea una lista de números desde un archivo y ordénelos en orden ascendente.
"""
import csv

def read_file_to_list_int(file_path: str) -> list:
    """Leer nombres de un archivo CSV

    ## Nota:  
        La función cuenta con el sistema de captura de errores (excepciones) referentes al archivo.

    Args:
        file_path (str): Ruta del archivo del cual se extraerán los nombres

    Returns:
        list: Lista con cada uno de los nombres del archivo especificado
    """
    names: list = []
    try:
        # Intenta abrir el archivo especificado en modo lectura
        with open(file_path, 'r', encoding='utf-8') as file:
            # Se crea un iterador "reader" del archivo CSV
            reader_file = csv.reader(file)
            # Se omite el encabezado del archivo
            next(reader_file)
            # Se accede a cada item del iterador y se agrega a la lista de nombres
            for row in reader_file:
                names.append(int(row[0]))
    except FileNotFoundError:
        print(f"No se encuentra el archivo {file_path}")
    
    return names

def sorting_ascendent(x: list) -> None:
    """Ordenar lista de forma ascendente mediante el algoritmo "**Bubble Sort**" (Ordenamiento Burbuja)

    Args:
        x (list): Lista que se desea ordenar, esta lista debe ser **estrictamente** de tipo numérico (**float** ó **int**)
    """
    # Ciclo en rango de longitud de lista
    for i in range(len(x)):
        # Ciclo usado para comparar uno a uno el par de número adyacentes
        for j in range(len(x) - i - 1):
            # Verificar si el valor de la "izquierda" [j] es mayor al de la "derecha"
            if x[j] > x[j + 1]:
                # Copiar valor que será sobreescrito
                centinel = x[j + 1]
                # Cambiar posiciones
                x[j + 1], x[j] = x[j], centinel

# Ruta del archivo CSV
numbers: str = './listas/data/numbers_desordered.csv'
# Obtener una lista de los nombres registrados en el archivo
numbers_list:list = read_file_to_list_int(numbers)
# Lista "desordenada"
print(f'Desordenada => {numbers_list}')
sorting_ascendent(numbers_list)
# Lista ordenada
print(f'Ordenada => {numbers_list}')