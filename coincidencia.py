def coincidencia(palabra, frase):
    # Convertir tanto la palabra como la frase a minúsculas para que la búsqueda no sea sensible a mayúsculas/minúsculas
    palabra = palabra.lower()
    frase = frase.lower()
    
    # Dividir la frase en palabras
    palabras_en_frase = frase.split()
    
    # Contar cuántas veces aparece la palabra en la lista de palabras de la frase
    contador = 0
    for p in palabras_en_frase:
        if p == palabra:
            contador += 1
    
    return contador


print(coincidencia("sol", "El sol brilla más que el sol"))  # 2
print(coincidencia("luna", "La luna está llena y la luna brilla mas que el sol aunque la luna es iluminada por el sol"))
