def calc_final_note(notes:list) -> tuple:
    """Calcular la nota final a partir de la lista de notas

    Args:
        notes (list): Lista de notas de los tres periodo/cortes (deben estar las 3 notas correspondientes)

    Returns:
        tuple: Se retorna una tupla con dos posiciones:
            - La primera posición (0) Indica si se realizó el cálculo (True) o si no (False).
            - La segunda posición indica la nota final (float) cuando primera posición es True, None en caso contrario
    """
    len_notes:int = len(notes)
    if len_notes == 3:
        # Calcular nota y formatear a solo un decimal
        final_note:float = float(f"{(sum(notes)):.1f}")
        return True, final_note
    else:
        print(f"Debe tener las notas de los tres periodos/cortes correspondientes, tiene {len_notes} de 3 notas")
        return False, None # Hacen falta notas

def calc_better_by_period(notes:list, students:list) -> list:
    """Obtener el nombre del estudiante con la mejor calificación de cada periodo/corte/corte

    Args:
        notes (list): 
        students (list): Lista de los nombres de estudiantes de un solo periodo/corte

    Returns:
        str: Nombre del estudiante con la mejor nota
    """
    periods:list = [__float_periods_list(notes, 0), __float_periods_list(notes, 1), __float_periods_list(notes, 2)]
    # Obtener los máximos de cada periodo
    betters:list = [max(periods[0]), max(periods[1]), max(periods[2])]
    student_list:list = []
    # Recorrer en el rango de los periodos
    for i in range(len(periods)):
        student_names:list = []
        # El mismo valor puede estar repetido
        for index in __get_index(notes, betters[i], i):
            # Obtener únicamente el nombre ([0]) de cada estudiante en las filas ([index]) especificadas
            student_names.append(f'{students[index][1]} {students[index][2]}')
        # Agregar cada lista de estudiantes mejores (Lista porque pueden haber repetidos)
        student_list.append(student_names)
    return student_list

def __get_index(list_search: list[list], value_search: any, index: int) -> list:
    """Obtener el índice de una valor dentro de una lista (soporta valores duplicados)

    Args:
        list_search (matrix): Matriz en la cual se buscará el valor 
        value_search (any): Valor el cual ayudará a encontrar el/los índice/índices dentro de la Matriz
        index (int): Fila de la matriz en la cual se buscará el valor

    Returns:
        list: Matriz de índices encontrados
    """
    return [i for i, x in enumerate(list_search) if x[index] == value_search]

def __float_periods_list(notes: list, index: int) -> list:
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

def calc_all_percent_note(notes:list) -> None:
    """Calcular todos los porcentajes de la lista de notas y sobreescribir con el valor calculado (Paso por referencia)

    Args:
        notes (list): Lista de notas de los tres periodo/cortes
    """
    # Calculra porcentajes de cada nota
    try:
        notes[0] *= 0.3
        notes[1] *= 0.35
        notes[2] *= 0.35
    except IndexError as e: # Faltan notas
        print("Asegúrese de ingresar la nota de cada uno de los tres periodo/cortes")

def calc_general_prom(notes:list) -> float:
    """Calcular el promedio general de las notas FINALES del grupo de estudiantes 

    Args:
        notes (list): Lista de notas FINALES de cada periodo/recorte

    Returns:
        float: Promedio general del grupo
    """
    final_note_all_periods:list = []
    # Recorrer periodos/recortes
    for row in notes:
        # final_note_all_periods.append(note_final)
        final_note_all_periods.append(float(row[3]))

    # Calcular el promedio de las notas finales
    general_prom:float = float(f'{(sum(final_note_all_periods) / len(final_note_all_periods)):.1f}')
    return general_prom