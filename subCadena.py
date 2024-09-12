def contarSubcadena(cadena, subcadena):
    contador = 0
    longitud_subcadena = len(subcadena)
    
    # Recorrer la cadena principal y buscar coincidencias de la subcadena
    for i in range(len(cadena) - longitud_subcadena + 1):
        if cadena[i:i + longitud_subcadena] == subcadena:
            contador += 1
    
    return contador


cadena = "banana"
subcadena = "ana"
resultado = contarSubcadena(cadena, subcadena)
print(f"La subcadena '{subcadena}' aparece {resultado} vez(veces) en la cadena '{cadena}'.")
