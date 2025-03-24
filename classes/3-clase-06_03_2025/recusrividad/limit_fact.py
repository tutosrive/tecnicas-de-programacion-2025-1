from files.factorial import fact

file = open("./classes/clase-06_03_2025/recusrividad/data/stack_overflow.md", "a")
file.write("# Stack Overflow with FACTORIAL\n")
n = 0
# Ejecutar factorial hasta el desborde
try:
    while True:
        factorial = fact(n)
        file.write(f"- **X** = {n}\n")
        n += 1
except RecursionError as e:
    file.write(f'\n-------------\n## Error\n {e.__class__.__name__} - {e}')
file.close()