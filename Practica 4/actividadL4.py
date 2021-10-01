import pdb
from math import sqrt
""" 1. Haciendo uso de comprensión de listas realice un programa que, dado una lista de listas de números enteros,
devuelva el máximo de cada lista.
"""
a = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

pdb.set_trace()
b = [max(i) for i in a]

print(b)


""" 2. Haga uso de la función filter para construir un programa que, dado una lista de n números devuelva aquellos
que son primos. Por ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente debe devolver como
resultado [3, 5, 5, 13]
"""
def primo(n):
    for i in range(2, int(2*sqrt(n))):
        return n % i !=0
elementos =[3, 4, 8, 5, 5, 22, 13]
es_primo = list(filter(primo, elementos) )
print(es_primo)
