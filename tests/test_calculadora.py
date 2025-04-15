import pytest
from src.calculadora import sumar, dividir, es_par, factorial

def test_suma_basica():
    assert sumar(2, 3) == 5

def test_division_normal():
    assert dividir(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ValueError, match="División por cero no permitida"):
        dividir(5, 0)

def test_es_par():
    assert es_par(4) is True
    assert es_par(5) is False

def test_factorial_limite():
    assert factorial(0) == 1
    assert factorial(3) == 6

def test_factorial_negativo():
    with pytest.raises(ValueError, match="El factorial no está definido para negativos"):
        factorial(-1)
