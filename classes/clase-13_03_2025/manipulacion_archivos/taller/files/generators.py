def generate_email(name:str, lastname:str, code_student: str) -> str:
    """Generar Correo Electrónico para un estudiante

    Args:
        name (str): Nombre del estudiante
        lastname (str): Apellido del estudiante
        code_student (str): Código del estudiante

    Returns:
        str: Dirección de 'Correo Electrónico' generada
    """
    # Dar formato al Correo Electrónico
    email:str = f'{name}_{lastname}.{code_student}@ucaldas.edu.co'
    # Retornar correo en minúsculas
    return email.lower().replace(' ', '')

def list_descendent() -> None:
    pass