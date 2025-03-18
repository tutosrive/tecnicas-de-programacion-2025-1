import files.generators as gener
import files.file_manager as file_man
import files.calculation as calc

# Ruta de acceso del directorio "data"
data_path:str = "./taller/data"
student_file:str = f'{data_path}/students.csv'
notes_file:str = f'{data_path}/notes.csv'
ranking_file:str = f'{data_path}/ranking.csv'

# Encabezados de archivos
file_man.write_csv(student_file, True, ["identification", "name", "lastname", "age", "code_id", "email"])
file_man.write_csv(notes_file, True, ["period1", "period2", "period3", "final_note"])
file_man.write_csv(ranking_file, True, ['final_note', 'students_list'], 'w')

for i in range(25):
    # Entrada de datos de usuario (nombre, edad, e.t.c.)
    name:str = input("Ingrese su nombre: ")
    lastname:str = input("Ingrese su apellido: ")
    age:int = int(input("Ingrese su edad (solo el número): "))
    identification:str = input("Ingrese su número de identificación: ")
    code_id:str = input("Ingrese su código estudiantil: ")
    # Generar email para el estudiante actual
    email:str = gener.generate_email(name, lastname, code_id)
    # Escribir los datos del estudiante en su archivo correspondiente
    file_man.write_csv(student_file, True, [identification, name, lastname, age, code_id, email], 'a')

    # Notas
    data:list = []
    # Obtener las notas de los 3 peridos/cortes
    for i in range(3):
        note:float = float(input(f"Ingrese la nota del periodo/corte {i + 1}: "))
        data.append(note)
    # Calcular notas finales de cada periodo/recorte
    calc.calc_all_percent_note(data)
    # Calcular nota final del estudiante
    final_note_student:float = calc.calc_final_note(data)[1]
    # Agregar nota final del estudiante
    data.append(final_note_student)
    # Escribir notas finales de cada periodo/recorte y la nota final del estudiante
    file_man.write_csv(notes_file, True, data, 'a')

# Lectura de todas las notas
notes:list = file_man.read_csv(notes_file)[1]
students:list = file_man.read_csv(student_file)[1]

# Recorer la matriz de estudiantes obtenidos
for period, students_row in enumerate(calc.calc_better_by_period(notes, students)):
    # Organizar mensaje según cantidad de estudiantes
    msg:str = f"Mejores estudiantes periodo {period + 1} son" if len(students_row) > 1 else f"Mejor estudiante periodo {period + 1} es"
    # Imprimir estudiante/s separados por coma
    print(f'{msg}: {', '.join(students_row)}')

# Promedio general del grupo
general_prom:float = calc.calc_general_prom(notes)
print(f'Promedio general del grupo de estudiantes: {general_prom}')

# Escribir lista ordenada descendentemente de las notas finales y sus estudiantes
notes_sorted_and_students:list = gener.list_descendent(notes, students)
file_man.write_csv(ranking_file, False, notes_sorted_and_students, 'a')