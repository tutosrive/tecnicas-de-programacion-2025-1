# enqueue(cola, valor head, end)

> [!NOTE]
> ### pre:
> 
> `{E/S int queue[n]; E int value; E int head; E/S int end}`
>
> ### pos:
> Si hay espacio disponible en la COLA, se agregará el nuevo elemento, se "encolará", y el fin (**end**) aumentará en 1 (es decir, se moverá un elemento adelante) 

```py
enqueue(E/S int queue[n]; E int value; E int head; E/S int end){
    if (isFull(queue[n], end)){
        print("La cola está llena")
    } else {
        end := end + 1
        queue[end] := value
    }
}
```