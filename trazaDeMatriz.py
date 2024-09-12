def traza(matriz, izquierda_a_derecha=True):
    n = len(matriz)  # Asumimos que la matriz es cuadrada
    suma = 0
    
    if izquierda_a_derecha:
        # Sumar la diagonal de izquierda a derecha (posición [i][i])
        for i in range(n):
            suma += matriz[i][i]
    else:
        # Sumar la diagonal de derecha a izquierda (posición [i][n-i-1])
        for i in range(n):
            suma += matriz[i][n-i-1]
    
    return suma


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcular traza de izquierda a derecha
print(traza(matriz, True))  

# Calcular traza de derecha a izquierda
print(traza(matriz, False)) 

