def maximin(arreglo):
    # Encontrar el valor máximo en el arreglo
    max_valor = max(arreglo)
    
    # Encontrar las posiciones donde aparece el valor máximo
    posiciones = [i for i, num in enumerate(arreglo) if num == max_valor]
    
    return max_valor, posiciones

arreglo = [1, 3, 7, 7, 2]
max_valor, posiciones = maximin(arreglo)
print(f"El valor máximo es {max_valor} y aparece en las posiciones {posiciones}")
