import pytest
import operaciones

# Test Operación de factorial de un numero.
def test_factorial():
    assert operaciones.factorial(5)==120

# Test Operación de resta entre 2 numeros
def test_resta():
    x=5
    y=2
    resultado = 3
    assert  operaciones.resta(x,y)==resultado

# Test Operación minimo de 1 función
def test_minimo():
    lista_numeros=[2,17,18,23,0,-9]
    assert operaciones.minimo(lista_numeros)==-9

# Test Operación comprobar que 1 numero es primo o no
def test_es_primo():
    n1=3
    n2=4
    assert operaciones.es_primo(n1)==True
    assert operaciones.es_primo(n2)==False
