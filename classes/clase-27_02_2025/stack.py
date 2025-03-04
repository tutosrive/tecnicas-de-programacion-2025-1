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
	# Validar si el TOPE (cima de la PILA) es igual a 0
	# de ser así, la lista está vacía
	if top == 0:
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

def pop_reference(stack: list[int], top_reference: list[int], value_reference: list[int]) -> int:
	"""Eliminar último elemento de la PILA (con valores por referencia, solo retorna 1 ó 0)

	### PRECONDICIONES: {`E/S int stack[n]`, `E/S int top[1]`, `E/S int value_reference[None]`}
	### POSCONDICIONES: 
			Se retorna:
				int: 0 => Lista vacía || 1 => Operaciones ejecutadas con éxito
			NOTA: Es claro que `stack`, `top_reference` y `value_reference` son "paso por referencia" y no se retornan
	Args:
		stack (list[int]): PILA con la cual se trabajará
		top_reference (list[int]): Tope (cima) de la PILA (se debe especificar como un `int` en posición 0)
		value_reference (list[None]): Almacenará el valor que se eliminará ó None

	Returns:
		int: `0` => Lista vacía || `1` => Operaciones ejecutadas con éxito
	"""
	if not isEmpty(top_reference[0]):
		# Agregar el valor que se "eliminará"
		# Usando lis.pop() eliminará el último valor y lo retornará
		value_reference[0] = stack[top_reference[0]]
		# Reducir tope en 1
		top_reference[0] -= 1
		# Operaciones ejecutadas con éxito
		return 1
	# PILA vacía
	return 0

def pop_multi_return(stack: list[int], top: int) -> tuple:
	"""Eliminar último elemento de la PILA (con múltiples retornos (tupla))

	### PRECONDICIONES: {`E/S int stack[n]`, `E/S int top`}
	### POSCONDICIONES: 
			Se retorna:
				tuple: (0, top: int, value = None): Lista vacía || (1, top: int, value: int): Operaciones ejecutadas con éxito

	Args:
		stack (list[int]): PILA con la cual se trabajará
		top (int): Índice del tope (cima, último elemento) de la PILA

	Returns:
		tuple: (0, top: int, None) Cuando la lista está vacía || (1, top: int, value: int)
	"""
	if not isEmpty(top):
		# Agregar el valor que se "eliminará"
		# Guardar el valor del TOPE ACTUAL
		value:int = stack[top]
		# Reducir tope en 1
		top -= 1
		# Operaciones ejecutadas con éxito
		return 1, top, value
	# PILA vacía
	return 0, top, None

def push(stack: list[int], value: int, top: int) -> None:
	"""Agregar un elemento a la PILA

	### PRECONDICIONES: {`E/S int stack[n]`, `E int value`, `E/S int top`}
	### POSCONDICIONES: 
		La PILA deberá contener el nuevo "valor" pasado por parámetro y el TOPE (Cima) estará un elemento adelante (`top + 1`)

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

# PILA que simula ser un arreglo estático
#stack:list[int] = [10, 11, 12]
# TOPE de la PILA
#top:int = 2
# "Eliminar" el elemento del tope de la PILA
#wasRemoved, top, value = pop_multi_return(stack, top)
#print(f'{wasRemoved=}\n{top=}\n{value=}\n{stack[top]=}')