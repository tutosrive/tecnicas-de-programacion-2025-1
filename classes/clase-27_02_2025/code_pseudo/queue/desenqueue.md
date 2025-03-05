# desenqueue(cola, head)

> [!NOTE]
> ### pre:
> 
> `{E/S int queue[n]; E int head; S int value}`
>
> ### pos:
>
> `int = 0`: Si la **COLA** está **vacía**, no habrá elementos para "**desencolar**".
> 
> `int = 1`: Indica que las operaciones se llevaron a cabo con éxito, además, el **parámetro de SALIDA** `value` contendrá el valor del elemento desencolado.

```py
int desenqueue(E/S int queue[n]; E int head; S int value){
    if (isEmpty(head)){
        print("La cola está vacía")
        ↑0
    } else {
        value := queue[head]
        head := head + 1
        ↑1
    }
}
```