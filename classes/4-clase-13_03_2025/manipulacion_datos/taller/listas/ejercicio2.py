"""
Enunciado:
    Cree una lista de nombres y permita al usuario buscar uno en la lista.
"""
# Lista de nombres de usuarios
names: list[str] =  [
    "Juan", "Andrés", "Camilo", "Santiago", "Sebastián", "Mateo", "Nicolás", "Tomás", "Alejandro", "Samuel",
    "Daniel", "David", "José", "Manuel", "Miguel", "Felipe", "Cristian", "Jairo", "Esteban", "Leonardo",
    "Ricardo", "Carlos", "Eduardo", "Fernando", "Álvaro", "Jorge", "William", "Hugo", "Germán", "Oscar",
    "Luis", "Ramiro", "Rodrigo", "Orlando", "Jonathan", "Wilson", "Freddy", "Emerson", "Rafael", "Iván",
    "Kevin", "Edwin", "Brayan", "Jhon", "Darío", "Rubén", "Franklin", "Gustavo", "Omar", "Jesús",
    "Henry", "Fabio", "Reinaldo", "Jacobo", "Hernán", "Diego", "Rony", "Guillermo", "Alex", "Marcos",
    "Mateus", "Moises", "Julio", "Dilan", "Elkin", "Salvador", "Rodolfo", "Alexander", "Jaime", "Nilson",
    "Anderson", "Mauricio", "Raúl", "Byron", "Arley", "Cristóbal", "Martín", "Efraín", "Edison", "Javier",
    "Domingo", "Ariel", "Alonso", "Emanuel", "Sergio", "Fabián", "Pedro", "Ernesto", "Abel", "Jesús David",
    "Juan Pablo", "Johan", "Camilo Andrés", "Felix", "Andrés Felipe", "Bruno", "Julián", "Harold", "Jean Pierre", "Jhoan"
]

def search(name:str) -> bool:
    """Buscar un String (nombre) en la lista de nombres

    Args:
        name (str): Nombre a buscar en la lista

    Returns:
        bool: Indica si el nombre está o NO está en la lista
    """
    choose: bool = False
    if name in names:
        choose = True
    return choose

again: bool = True
# Ejecutar hasta que el usuario decida no buscar más
while(again):
    # Pedir nombre al usuario
    name: str = input("Ingrese un nombre para buscar: ")
    # Buscar nombre en la lista
    choose: bool = search(name)
    # Salida de información
    print(f'El nombre {"SÍ" if choose else "NO"} está en la lista de nombres')
    # Preguntar si desea buscar nuevamente
    again_str: str = input("¿Desea buscar otro nombre? (s | n): ")
    # Repetir mientras el usuario no ingrese un caracter correcto (s | n)
    while(again_str not in ['s', 'n']):
        again_str: str = input("Intente nuevamente: \n¿Desea buscar otro nombre? (s | n): ")
    again = False if again_str == "n" else True