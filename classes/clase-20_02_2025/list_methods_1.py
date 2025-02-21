def insert(L: list[int], value: int, pos: int, size: int) -> None:
    """Insertar un nuevo valor a la lista pasada por parámetro

    ### Precondición:
        `value ∈ Z`; `pos ∈ N`; `size ∈ N` 

    ### Postcondición:
        Al finalizar la ejecución, se agregará el nuevo valor a lista en la posición indicada.


    Args:
        L (list[int]): Lista a la cual se agregará el nuevo valor
        pos (int): Posición en la cual se insertará el nuevo "valor"
        size (int): Tamaño actual de la lista (cantidad de espacios ocupados)
    """
    # Validar "espacio" en la lista y la posición parametrizada
    if filled(L, size) or pos == len(L):
        print("No se puede agregar el nuevo valor.")
    else:
        # Ir desde el 
        for i in range(size, pos - 1, -1):
            # "Mover" el valor de la izquierda, una cacilla a la derecha
            L[i+1] = L[i]
        # Agregar el nuevo valor a la posición "despejada"
        L[pos] = value

def filled(L: list[int], size: int) -> bool:
    """Insertar un nuevo valor a la lista pasada por parámetro

    ### Precondición:
        `value ∈ Z`; `pos ∈ N`; `size ∈ N` 

    ### Poscondición:
        Una vez ejecutada esta subrutina, se indicará/retornará si la lista tiene todos 
        sus espacios ocupados (`True`) o si aún tiene espacios disponibles (`False`)

    Args:
        L (list[int]): Lista que se desea verificar
    """
    # El tamaño ocupado es igual al tamaño disponible
    list_filled = size == len(L)
    return list_filled