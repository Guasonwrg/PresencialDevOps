def sumarBorde(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    suma = 0
    
    # Sumar la primera y la última fila completa
    suma += sum(matriz[0])  # Primera fila
    suma += sum(matriz[filas - 1])  # Última fila
    
    # Sumar los elementos de la primera y última columna (sin contar las esquinas ya sumadas)
    for i in range(1, filas - 1):
        suma += matriz[i][0]  # Primera columna (excepto esquinas)
        suma += matriz[i][columnas - 1]  # Última columna (excepto esquinas)
    
    return suma


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = sumarBorde(matriz)
print(f"La suma del borde de la matriz es: {resultado}")

