def histograma(arreglo):
    for numero in arreglo:
        # Imprimir el número seguido de esa cantidad de asteriscos
        print(f"{numero}{'*' * numero}")


arreglo = [5, 2, 1]
histograma(arreglo)
