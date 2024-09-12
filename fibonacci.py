def fibo(n):
    fibonacci = [0, 1]

    # Generar la serie de Fibonacci hasta el número n
    while len(fibonacci) < n + 1:
        siguiente_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(siguiente_numero)

    return fibonacci[:n+1]


n = 7
resultado = fibo(n)
print(resultado)