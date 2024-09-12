def silla(matriz):
    puntos_silla = []
    
    # Recorrer cada fila de la matriz
    for i in range(len(matriz)):
        # Encontrar el mínimo valor en la fila actual y su índice
        min_valor = min(matriz[i])
        min_columna = matriz[i].index(min_valor)
        
        # Comprobar si el valor mínimo en la fila es el máximo en la columna
        es_punto_silla = True
        for j in range(len(matriz)):
            if matriz[j][min_columna] > min_valor:
                es_punto_silla = False
                break
        
        # Si es un punto de silla, lo añadimos a la lista
        if es_punto_silla:
            puntos_silla.append((i, min_columna, min_valor))
    
    return puntos_silla


matriz = [
    [3, 8, 4],
    [2, 7, 9],
    [1, 6, 5]
]

resultado = silla(matriz)
print(f"Puntos de silla: {resultado}")

