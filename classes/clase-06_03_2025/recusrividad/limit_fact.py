from files.factorial import fact

file = open("./classes/clase-06_03_2025/recusrividad/data/stack_overflow.md", "a")
file.write("# Stack Overflow with FACTORIAL\n")
n = 0
# Ejecutar factorial hasta el desborde
while True:
    factorial = fact(n)
    file.write(f"- X = {n}\n")
    n += 1
# Código muerto
file.close()