def isFull(queue: list[int], end:int) -> bool:
    """Verificar si la COLA está llena

    ### PRECONDICIONES: {`E int queue[n]`, `E int end`}
    ### POSCONDICIONES: 
        Se retornará un valor booleano el cual indicará si está llena (True) o NO (False) la COLA

    Args:
        queue (list[int]): COLA la cual se verificará si está o NO llena
        end (int): Índice del fin (último elemento) de la COLA

    Returns:
        bool: `True` => COLA llena || `False` => COLA con espacio
    """
    isFilled:bool = False
    # Se suma 1 al final porque los índices comienzan desde cero
    if (end + 1) >= len(queue):
        isFilled = not isFilled # Negación lógica
    return isFilled

def isEmpty(head: int) -> bool:
    """Verificar si la COLA está vacía

    ### PRECONDICIÓN: {`E int head`}
    ### POSCONDICIÓN: 
        Se indicará si la COLA está vacía o tiene espacio "PARA ENCOLAR" por medio de un valor Booleano

    Args:
        head (int): Índice de la cabecera (índice del primer elemento "encolado")

    Returns:
        bool: Booleano que indicará si la COLA está vacía o NO
    """
    isNull: bool = False
    # Si la cabecera está en el índice -1, estará vacía
    if head == -1:
        isNull = not isNull # Negación lógica
    return isNull

def enqueue(queue: list[int], value: int, end: list[int]):
    """"Encolar" un elemento nuevo a la COLA en cuestión

    ### PRECONDICIÓN: {`E/S int cola[n]`, `E int value`, `E/S int end`}
    ### POSCONDICIÓN:
        La COLA deberá contener el nuevo elemento si hay espacio en esta, de lo contrario se debe mostrar por consola "La COLA está llena", indicando que no se realizaron más operaciones

    Args:
        queue (list[int]): COLA con la cual se trabajará
        value (int): Valor que se quiere agregar
        head (list[int]): Índice de la "cabecera" ("primer" elemento "encolado") de la COLA
        end (list[int]): Índice del fin de la COLA
    """
    if isFull(queue, end[0]):
        print("La COLA está llena")
    else:
        # Correr el fin un elemento adelante
        end[0] += 1
        # "Encolar" el nuevo elemento al final
        queue[end[0]] = value

def desenqueue(queue: list[int], head: int) -> tuple:
    """"Desencolar" un elemento de la COLA de elementos

    ### PRECONDICIÓN: {`E/S int queue[n]`, `E/S int head`}
    ### POSCONDICIÓN:
        La COLA deberá contener un elemento menos, el elemento "desencolado" de la cabecera y la cabecera ahora debe estar un elemento adelante

    Args:
        queue (list[int]): COLA de la cual se desea "desencolar" el elemento
        head (int): Índice de la cabecera de la COLA (primer elemento encolado)

    Returns:
        tuple: `(0, head: int, None)` Cuando la COLA está vacía || `(1, head: int, value: int)` Cuando la COLA NO está vacía
    """
    # Si NO está vacía
    if not isEmpty(head):
        # Obtener el valor que se "desencola" (procesa/quita/elimina)
        value:int = queue[head]
        """Si la cabecera está en el último elemento, significa que una vez "desencolado"
        este último elemento, la COLA quedará VACÍA (head = -1)
        """
        if isFull(queue, head):
            head = -1
        else:
            # Mover la cabecera un elemento adelante
            head += 1
        # Retornar lista NO vacía (1), índice de la cabecera y valor "desencolado"
        return 1, head, value
    # Retornar lista vacía (0), índice de la cabecera y None (NO se desencoló nada)
    return 0, head, None