def isEmpty(top:int) -> bool:
	"""Verficar si una PILA  está vacía

	### PRECONDICIONES: {`E int top`}
	### POSCONDICIONES: 
			Se retorna:
				bool: True: Lista vacía || False: Lista NO vacía
	
	Args:
		top (int): Posición del tope de la PILA (posición del último elemento)

	Returns:
		bool: Booleano que indicará si la lista ESTÁ o NO vacía 
	"""
	isNull: bool = False # Por defecto es vacía
	# Validar si el TOPE (cima de la PILA) es mayor a 0
	# de ser así, la lista está vacía
	if top > 0:
		isNull = not isNull # Negación lógica
	return isNull

def isFull(stack: list[int], top: int) -> bool:
	"""Verficar si una PILA  está llena

	### PRECONDICIONES: {`E int stack[n]`, `E int top`}
	### POSCONDICIONES: 
			Se retorna:
				bool: True: Lista llena || False: Lista NO llena
	
	Args:
		top (int): Posición del tope de la PILA (posición del último elemento)

	Returns:
		bool: Booleano que indicará si la lista ESTÁ o NO llena 
	"""
	isFilled: bool = False # Por defecto es NO llena
	# Validar si TOPE (cima de la PILA) + 1 es mayor o igual al tamaño de la PILA
	# de ser así, la PILA está llena
	if (top + 1) >= len(stack):
		isFilled = not isFilled # Negación lógica
	return isFilled

def push(stack: list[int], value: int, top: int) -> None:
	"""Agregar un elemento a la PILA 

	### PRECONDICIONES: {`E/S int stack[n]`, `E int value`, `E/S int top`}

	Args:
		stack (list[int]): PILA  a la cual se intentará agregar el elemento
		value (int): Valor que se intentará agregar a la PILA 
		top (int): Tope de la PILA (cima de la PILA, último elemento, última posición ocupada)
	"""
	# Verificar si hay espacio en la pila
	if isFull(stack, top):
		print("La PILA está llena ó verifique el TOPE")
	else:
		# "Subir" tope una posición
		top += 1
		# Almacenar el nuevo valor en el tope (la cima de la PILA)
		stack[top] = value