import pdb

def factorial(n):
    resultado = 1
    for i in range(1,n+1):
        resultado +=i
    return resultado

def primo(n):
# decimos desde donde queremos que se ejecute.
    pdb.set_trace() 
    es_primo = True
    for i in range(2, n - 1):
        if(n % i == 0):
            es_primo = False
    return es_primo


def listar_n_primos(n):
    for i in range(2,n):
        es_primo = primo(i)
        if(es_primo):
            print(i, "es un numero primo.")
       


def funcion_inventada(n,m):
    resultado = 0
    for i in range(n):
        if(i % 2 == 0):
            resultado += n*17
        else:
            n -=2
    resultado /=n
    return resultado


# LLamamos a las funciones:
print(factorial(5))
print(primo(17))
print(listar_n_primos(20))
print(funcion_inventada(4,8))