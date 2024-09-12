def esCuadrada(matriz):
    # Verificar si la cantidad de filas es igual a la cantidad de columnas
    return all(len(fila) == len(matriz) for fila in matriz)

# Ejemplo de uso
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [1, 2, 3],
    [4, 5, 6]
]

print(esCuadrada(matriz1))  
print(esCuadrada(matriz2))  

