def sumar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("División por cero no permitida")
    return a / b

def es_par(n):
    return n % 2 == 0

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para negativos")
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
