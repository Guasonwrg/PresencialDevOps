def traspuesta(matriz):
    # Usar comprensión de listas para intercambiar filas por columnas
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]


matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

resultado = traspuesta(matriz)
for fila in resultado:
    print(fila)
