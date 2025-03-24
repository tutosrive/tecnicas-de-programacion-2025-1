"""
Enunciado:
    Cree un programa que lea desde un archivo una lista de nombres que se encuentran separados por coma y punto y coma
    (Nombres1, Apellidos1;Nombres2,Apellidos2), luego debe detectar cuál es el nombre que más se repite, y también detectar
    cuántas veces se repite cada apellido.
"""
import csv

def read_csv(file: str) -> list[list[str]]:
    """Leer archivo CSV

    Args:
        file (str): Ruta del archivo CSV

    Returns:
        list[list[str]]: Información registrada en el archivo CSV
    """
    data: list[list[str]] = []
    with open(file, 'r', encoding='utf-8') as csv_file:
        data = list(csv.reader(csv_file))
    return data

def splitter(string_to_split: str, separator: str) -> list[str]:
    """Función que simula ser "split"

    Args:
        string_to_split (str): String que se quiere "recortar/separar"
        separator (str): String que representa el separador mediante el cual se cortará el String

    Returns:
        list[str]: Lista de palabras extraídas/separadas del String
    """
    # Inicalizar lista de palabras
    words:list[str] = []
    word:str = "" 
    for char in string_to_split:
        # Verificar si el caracter actual es diferente que el "separador" indicado
        if char != separator:
            # Agregar cada caracter hasta formar una palabra
            word += char
        else:
            # Se encontró un "espacio"
            #se procede a agregar la palabra a la lista de palabras
            words.append(word)
            # Se inicializa la variable nuevamente (nueva palabra)
            word:str = ""
    # Se agrega la última palabra formada
    words.append(word)
    # Retornar la lista de palabras extraídas
    return words

def get_val_matrix(matrix: list[list[str]], index: int) -> list[str]:
    """Obtener los valores de cada fila de una matriz

    Args:
        matrix (list[list[str]]): Matriz de la cual se obtendrán los datos
        index (int): Índice de la fila del cual se extraerán los datos por cada fila de la matriz

    Returns:
        list[str]: Lista con los valores de la columna especificada de cada fila de la matriz
    """
    return [row[index] for row in matrix if row[index] != '']

def create_list_count(data: list[str]) -> list[list[str | int]]:
    """Crear matriz que contiene los elementos de una lista y las veces en las que se repite este elemento

    Args:
        data (list[str]): Lista de la cual se tomarán y contarán los elementos

    Returns:
        list[list[str | int]]: Matriz con constituida por una lista por cada elemento y sus repectivas repeticiones/ocurrencias
    """
    # Lista de valores obtenidos (count es para las repetciones)
    vals, count = [], []
    # Obtener cada valor de "data"
    for val in data:
        # Recorrer lista de valores para compararlos
        for i in range(len(vals)):
            if val == vals[i]:
                # Si el valor de data ya existe en "vals"
                # Indica que ya se agregaron valores, por tanto será una repetición
                count[i] += 1
        # Si el valor de "data" no está en "vals"
        # Indica que es un nuevo valor
        if val not in vals:
            # Se agrega como un nuevo valor
            vals.append(val)
            # Se agrega la primer ocurrencia
            count.append(1)
    # Se crea una matriz con cada valor y sus respectivas repeticiones
    counts_vals = [[vals[i], count[i]] for i, _ in enumerate(vals)]
    # Se retorna matriz de [[valores, repeticiones]]
    return counts_vals

def get_moda_repetition(matrix: list[list[str | int]]) -> tuple[int, list[str | int]]:
    """Obtener la "moda" de una matriz de elementos con sus repectivas repeticiones

    Args:
        matrix (list[list[str | int]]): Matriz de la cual se extraerá los datos

    Returns:
        
    
        **tuple[int, list[str | int]]**: SÍ\n
            **(0, ['', 0])**: Indica que hay más de un elemento "modal", y por tanto no hay "moda"\n
            **(1, [str, int])**: Indica que hay solo un elemento "modal", y por tanto sí hay "moda"
    """
    # Valor "nulo" o inicial
    moda: list[str | int] = ['', 0]
    for row in matrix:
        # Comparación de repeticiones (cantidad de courrencias)
        if row[1] > moda[1]: # type: ignore
            # Se agrega la "nueva" moda
            moda[0], moda[1] = row[0], row[1]
        # Ya sea un valor menor o sea el mismo valor
        elif row[1] == moda[1]:
            # Se determina a "nulo" nuevamente la moda
            moda[0], moda[1] = '', 0
    # Validación de la forma actual de "moda"
    if moda == ['', 0]:
        # No hay "moda"
        return 0, moda
    else:
        # Si hay "moda"
        return 1, moda

# file_names: str = './listas/data/nombres_colombianos.csv'
file_names: str = './listas/data/nombres_colombianos.csv'
data: list[list[str]] = read_csv(file_names)
# Separar nombres y apellidos por los punto y coma (;)
data = [splitter(data[0][int(index)], ';') for index, _ in enumerate(data[0])]
# Obtener lista de apellidos [0] y lista de nombres [1]
lastnames_names: list[list[str]] = [get_val_matrix(data, 0), get_val_matrix(data, 1)]

# Obtener las veces que se repite cada nombre
names_repetitions_count: list[list[str | int]] = create_list_count(lastnames_names[1])
# Obtener la "moda" de los nombres
moda_names = get_moda_repetition(names_repetitions_count)
print(f'Nombres (Repeticiones)==>\n {names_repetitions_count}', end='\n\n')
print(f'Moda Nombre ==> {moda_names}', end='\n\n')

# Obtener las repeticiones de los apellidos
lastnames_repetitions_count: list[list[str | int]] = create_list_count(lastnames_names[0])
print(f'Apellidos (Repeticiones)==>\n {lastnames_repetitions_count}')