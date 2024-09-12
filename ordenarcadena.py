def ordenarPorLongitud(cadenas):
    # Usar la función sorted() con la longitud de cada cadena como clave
    return sorted(cadenas, key=len)


cadenas = ['sol', 'estrella', 'luz']
resultado = ordenarPorLongitud(cadenas)
print(resultado) 
