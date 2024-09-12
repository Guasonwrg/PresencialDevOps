def factorial(n):
    # El factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    
    # Calcular el factorial usando un bucle
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    
    return resultado


print(factorial(10))  
print(factorial(2))  
