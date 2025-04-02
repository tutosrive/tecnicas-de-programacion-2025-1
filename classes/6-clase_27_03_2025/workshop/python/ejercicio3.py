import math

# Función for encontrar los dos puntos más cercanos
def find_nearest_points(points_names: list[str], vals_x: list[int], vals_y: list[int]) -> str:
    # Variable de retorno
    names_nearest_points = ""
    # Distancia mínima entre puntos
    min_distance = math.inf

    # Recorrer vectores
    for i in range(4):
        for j in range(i+1, 4, 1):
            # Potenciar valores a la 2
            pow_x = pow(vals_x[j] - vals_x[i], 2)
            pow_y = pow(vals_y[j] - vals_y[i], 2)
            # Calcular la distancia
            # calc_min_distance = √((x2 - x1)² + (y2 - y1)²)
            calc_min_distance = math.sqrt(pow_x + pow_y)
            # Comforr distancia actual con las distancias mínima anterior
            if calc_min_distance < min_distance:
                # Nueva distancia mínima
                min_distance = calc_min_distance
                # Nuevos nombres de puntos (A,D o B,C....)
                names_nearest_points = points_names[i] + "," + points_names[j]
    
    # Retornar nombres de los puntos concatenados
    return names_nearest_points

# main()

# Inicialización de variables
nombre = ['A', 'B', 'C', 'D']
x = [3, 2, 4, -1]
y = [1, 5, 2, 4]

names_points = find_nearest_points(nombre, x, y)
print(f"Los 2 puntos más cercanos son: {names_points}")