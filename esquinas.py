def sumaEsquinas(matriz):
    if len(matriz) == 0 or len(matriz[0]) == 0:
        return 0  # Si la matriz está vacía, retorna 0

    filas = len(matriz)
    columnas = len(matriz[0])
def sumaEsquinas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Sumar los elementos de las cuatro esquinas
    suma = matriz[0][0]  # Esquina superior izquierda
    suma += matriz[0][columnas - 1]  # Esquina superior derecha
    suma += matriz[filas - 1][0]  # Esquina inferior izquierda
    suma += matriz[filas - 1][columnas - 1]  # Esquina inferior derecha
    
    return suma

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = sumaEsquinas(matriz)
print(f"La suma de las esquinas de la matriz es: {resultado}")
