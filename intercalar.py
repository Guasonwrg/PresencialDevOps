def intercala(arreglo1, arreglo2):
    # Inicializar el nuevo arreglo y los índices de ambos arreglos
    resultado = []
    i, j = 0, 0

    # Intercalar los dos arreglos comparando sus elementos
    while i < len(arreglo1) and j < len(arreglo2):
        if arreglo1[i] < arreglo2[j]:
            resultado.append(arreglo1[i])
            i += 1
        else:
            resultado.append(arreglo2[j])
            j += 1

    # Añadir los elementos restantes del arreglo1 (si los hay)
    while i < len(arreglo1):
        resultado.append(arreglo1[i])
        i += 1

    # Añadir los elementos restantes del arreglo2 (si los hay)
    while j < len(arreglo2):
        resultado.append(arreglo2[j])
        j += 1

    return resultado


arreglo1 = [10, 20, 50]
arreglo2 = [1, 2, 20, 24, 80]
resultado = intercala(arreglo1, arreglo2)
print(resultado)
