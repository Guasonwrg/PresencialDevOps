import math

def estadistica(numeros):
    # Calcular la media
    n = len(numeros)
    media = sum(numeros) / n
    
    # Calcular la desviación estándar
    suma_diferencias_cuadradas = sum((x - media) ** 2 for x in numeros)
    desviacion_estandar = math.sqrt(suma_diferencias_cuadradas / n)
    
    return media, desviacion_estandar


numeros = [10, 12, 23, 23, 16, 23, 21, 16]
media, desviacion_estandar = estadistica(numeros)
print(f"Media: {media}")
print(f"Desviación estándar: {desviacion_estandar}")
