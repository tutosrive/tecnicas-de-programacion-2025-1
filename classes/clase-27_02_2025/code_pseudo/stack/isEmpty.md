# isEmpty(tope)

> [!NOTE]
> ### pre: 
> `{E int tope;}`
>
> ### pos:
>	`bool = False`: **Lista NO vacía** (Tiene elementos)
>
>	`bool = True`: **Lista vacía** (Sin elementos)

```py
bool isEmpty(E int tope;){
    bool isNull := False
    # TOPE = 0 (En pseudocódigo los índices correctos inician en 1)
	if (tope = 0){
        isNull := True
    }
    ↑isNull
}
```