def generate_email(name:str, lastname:str, code_student: str) -> str:
    """Generar Correo Electrónico para un estudiante

    Args:
        name (str): Nombre del estudiante
        lastname (str): Apellido del estudiante
        code_student (str): Código del estudiante

    Returns:
        str: Dirección de 'Correo Electrónico' generada
    """
    # Dar formato al Correo Electrónico
    email:str = f'{name}_{lastname}.{code_student}@ucaldas.edu.co'
    # Retornar correo en minúsculas
    return email.lower().replace(' ', '')

def list_descendent(notes: list[list], students: list[list]) -> list:
    """Ordenar la lista del ranking descendentemente

    Args:
        notes (list[list]): Lista de rankings
        students (list[list]): _description_

    Returns:
        list: _description_
    """
    # Castear las notas de String a Float
    parsing_to_float_matrix(notes)
    # Ordenar las filas de la matriz según la nota final de cada fila (row[3]) (en orden Descendente reverse=True)
    notes_sorted: list[list] = sorted(notes, key=lambda row: row[3], reverse=True)
    # Notas en una lista (vector, 1 dimensión)
    notes_vector: list = []
    # Obtener un vector de las notas finales (por ello índice = 3)
    __create_vector_not_duplicate_values_from_matrix(notes_sorted, notes_vector, 3)
    # Crear una matriz ([row[3]]) de solo la nota final, esto para
    # escribir varias filas directamente, por eso hice una matriz
    notes_sorted: list[list] = __create_matrix_from_vector(notes_vector)
    # Agregar los estudiantes al ranking de notas
    __add_students_for_each_final_note(notes_sorted, students, notes)
    # Retornar matriz de notas finales ordenada descendentemente con sus estudiantes 
    return notes_sorted

def __create_vector_not_duplicate_values_from_matrix(matrix:list[list], vector:list, index: int) -> None:
    # Recorrer matriz
    for row in matrix:
        if row[index] not in vector:
            # Agregar valor de (row[index]) al vector de referencia
            vector.append(row[index])

def __create_matrix_from_vector(vector: list) -> list:
    """Crear una matrix a partir de un vector

    Args:
        vector (int): Vector/Lista del cual se extraerán los datos para la matriz

    Returns:
        list[list]: Matriz con los datos del vector
    """
    # Crear una matriz ([row[3]]) de solo la nota final, esto para
    # escribir varias filas directamente, por eso hice una matriz
    matrix: list[list] = [[col] for col in vector]
    return matrix

def __add_students_for_each_final_note(notes_sorted: list[list], students: list[list], notes: list[list]) -> None:
    # Recorrer notas finales
    for index, nota in enumerate(notes_sorted):
        # Obetener la lista de estudiantes (Habrán notes_sorted iguales...)
        # Se entiende que j = fila, y por ende students[1][j][1] obtiene el "nombre" y students[1][j][2] el/los apellido/S
        students_list: list = [f'{students[j][1]} {students[j][2]}' for j in get_index(notes, notes_sorted[index][0], 3)]
        # Agregar el listado de estudiantes a la fila de la nota actual (notes_sorted[index])
        notes_sorted[index].append(students_list)
        # Antes de pasar a la siguiente nota, se debe limpiar los estudiantes de la nota anterior
        students_list: list = []

def get_index(list_search: list[list], value_search: any, index: int) -> list:
    """Obtener el índice de una valor dentro de una lista (soporta valores duplicados)

    Args:
        list_search (matrix): Matriz en la cual se buscará el valor 
        value_search (any): Valor el cual ayudará a encontrar el/los índice/índices dentro de la Matriz
        index (int): Columna de la matriz en la cual se buscará el valor

    Returns:
        list[list]: Matriz de índices encontrados
    """
    return [i for i, x in enumerate(list_search) if x[index] == value_search]

def float_periods_list(notes: list, index: int) -> list:
    """Extraer los valores de cada periodo y agregarlos a una lista la cual será retornada

    Args:
        notes (list): Lista/Vector de notas
        index (int): Índice del vector (indicando el periodo a extraer)

    Returns:
        list: Lista de los periodos extraídos de cada fila de la Matriz
    """
    periods: list = []
    for i in range(len(notes)):
        notes[i][index] = float(notes[i][index])
        periods.append(notes[i][index])
    return periods

def parsing_to_float_matrix(matrix: list[list]) -> None:
    """Castear/Convertir datos de una matriz (Strings) a números decimales (float)

    Args:
        matrix (list[list]): Matriz de la cual se extraerán los datos
    """
    # Recorrer la matriz, en lugar de usar range(len(matrix)), decidí usar enumerate y capturar índice (i) y valor (row = fila)
    for i, row in enumerate(matrix):
        # Map, permite en este caso, castear de STRING a FLOAT, cada valor(map(float, matrix[i])) de cada fila (matrix[i])
        matrix[i] = list(map(float, matrix[i])) 