# push(pila, valor, tope)

> [!NOTE]
> ### pre: 
> `{E/S int pila[n]; E int valor; E int tope}`
> ### pos:
>	Se agregará el nuevo elemento en caso de que la **PILA** tenga espacio disponble, en caso contrario se mostrará un mensaje por consola que dice "**La pila está llena**"

```py
int push(E/S int pila[n]; E int valor; E int tope){
    if (llena(pila[n], tope)){
        print("La pila está llena")
    } else {
        tope := tope + 1
        pila[tope] := valor
    }
}
```