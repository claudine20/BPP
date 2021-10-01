# Importamos la herramienta reduce:
from functools import reduce

letras=[]
for i in "Python es el mejor lenguaje de programación del mundo":
    letras.append(i)
print(letras)

""" Compresion de listas"""
letras2 = [i for i in  "Python es el mejor lenguaje de programación del mundo"]
print(letras2)

pares = [i for i in range(21) if i % 2 ==0]
print(pares)

parImpar =[0 if i%2 == 0 else 1 for i in range(21)]
print(parImpar)

# Función para calcular el cuadrado de un numero:
def calcular_cuadrado(n):
    return n**2 # ** = elevar un numero, estamos elevando n a 2.
elementos =[2,3,5,9]
cuadrados = list(map(calcular_cuadrado, elementos))
print(cuadrados)

# Función para determinar si un numero es par:
def es_par(n):
    return n%2==0
elementos =[2,3,5,9]
pares = list(filter(es_par, elementos))
print(pares)

# Funcion sumatoria usando la herramienta reduce:
def sumatoria(a,b):
    return a+b
elementos =[2,3,5,9]
suma = reduce(sumatoria, elementos)
print(suma)

# Funcion factorial  usando la herramienta reduce. En este ejemplo calculamos el factorial del numero 5! = 120
def producto(a,b):
    return a*b
factorial = reduce(producto, range(1,6))
print(factorial)
