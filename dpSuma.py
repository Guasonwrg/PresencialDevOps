def dpSuma(matriz):
    n = len(matriz)  # Asumimos que la matriz es cuadrada
    suma = 0
    
    # Recorrer la matriz para sumar solo los elementos por encima de la diagonal principal
    for i in range(n):
        for j in range(i + 1, n):  # Solo elementos donde la columna es mayor que la fila (j > i)
            suma += matriz[i][j]
    
    return suma


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = dpSuma(matriz)
print(f"La suma de los elementos por encima de la diagonal principal es: {resultado}")
