# isEmpty(head)

> [!NOTE]
> ### pre:
> 
> `{E int head}`
>
> ### pos:
>
> `bool = False`: La **COLA** **NO** está vacía (Tiene elementos)
> 
> `bool = True`: La **COLA** está vacía (No tiene elementos)

```py
bool isEmpty(E int head){
    bool isNull := False
    # HEAD = 0 (Los índices comienzan desde 0, en un lenguaje real sería -1)
    if(head = 0){
        isNull := True
    }
    ↑isNull
}
```