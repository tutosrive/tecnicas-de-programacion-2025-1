# isFull(pila;tope)

> [!NOTE]
> ### pre: 
> `{E int pila[n]; E int tope;}`
>
> ### pos:
>	`bool = False`: **Lista NO llena** (Tiene espacio disponible)
>
>	`bool = True`: **Lista llena** (Sin espacio disponible)

```py
bool isFull(E int pila[n]; E int tope;){
    bool isFilled := False
    # TOPE = n (Tamaño de la PILA)
	if (tope = n){
        isFilled := True
    }
    ↑isFilled
}
```