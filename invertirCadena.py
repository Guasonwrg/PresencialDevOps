def invertir(cadena):
    # Crear una cadena vacía para almacenar el resultado
    cadena_invertida = ""
    
    # Recorrer la cadena desde el último carácter hasta el primero
    for i in range(len(cadena) - 1, -1, -1):
        cadena_invertida += cadena[i]
    
    return cadena_invertida


print(invertir("aloh")) 
print(invertir("Python"))
