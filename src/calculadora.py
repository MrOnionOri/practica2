def sumar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("División por cero no permitida")
    return a / b

def es_par(n):
    return n % 2 == 0

def factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    if n < 0:
        raise ValueError("El factorial no está definido para negativos")
    return 1 if n == 0 else n * factorial(n - 1)
