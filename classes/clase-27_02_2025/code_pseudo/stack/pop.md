# pop(pila, tope, value)

> [!NOTE]
> ### pre: 
> `{E/S int pila[n]; E/S int tope; S int value}`
>
> ### pos:
>	`int = 1`: **Lista no vacía** y elemento del tope fue eliminado (S int value, será el valor eliminado)
>
>	`int = 0`: **Lista vacía** (No se realizaron más operaciones, salida de la subrutina)

```py
int pop(E/S int pila[n]; E/S int tope; S int value){
	# Verificar si la **lista está vacía** (No habrán elementos a eliminar)
	if (vacia(tope)){
		print("Pila vacía")
		# Informa que la **lista está vacía**
		↑ 0 
	} else {
		# Se alamacena el valor actual del "tope"
		value := pila[tope]
		# El tope, se "devuelve" (-1) una posición
		tope := tope - 1
		# Se informa que se llevó a cabo las operaciones
		↑ 1
	}
}
```