# isFull(cola, end)

> [!NOTE]
> ### pre:
> 
> `{E int queue[n]; E int end}`
>
> ### pos:
>
> `bool = False`: La **COLA** tiene espacio disponible
> 
> `bool = True`: La **COLA** está llena (No tiene espacio disponible)

```py
bool isFull(E/S int queue[n]; E/S int end){
    bool isFilled := False
    if(end = n){
        isFilled := True
    }
    ↑isFilled
}
```