# Operación de factorial de un numero.
def factorial(n):
     fct=1
     for i in range(1,n+1):
         fct*=i
     return fct

#  Operación de resta entre 2 numeros
def resta(a,b):
    return a-b

#  Operación de de 1 función
def minimo(lista_numeros):
    minimo =999999
    for i in lista_numeros:
        if(i < minimo):
            minimo =i
    return minimo

# Operación de 1 numero es primo o no
def es_primo(n):
    primo = True
    for i in range(2,n-1):
        if(n%i==0):
             primo = False
    return primo
