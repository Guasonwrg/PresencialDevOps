def posearch(arreglo, valor):
    # Inicializar la posición y la diferencia mínima
    posicion_cercana = 0
    diferencia_minima = abs(arreglo[0] - valor)
    
    # Recorrer el arreglo para encontrar el número más cercano
    for i in range(1, len(arreglo)):
        diferencia_actual = abs(arreglo[i] - valor)
        if diferencia_actual < diferencia_minima:
            diferencia_minima = diferencia_actual
            posicion_cercana = i
    
    return posicion_cercana


arreglo = [1, 3, 5, 8]
valor = 6
posicion = posearch(arreglo, valor)
print(f"El número más cercano a {valor} es {arreglo[posicion]} en la posición {posicion}")
