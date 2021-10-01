import numpy as np

def checklist(list):
    elem = list[0]
    resultado = True
    for i in range(1,len(list)):
        if(list[i]!= elem):
            resultado = False
    return resultado

# Conclusión: Podemos hacer el Unittest de la fº "defchecklist(list)"
# pero no tendria sentido hacerla para la función "def tragaperras()" ya que es 1 función aleatoria

def tragaperras():
    opciones =['cereza', 'manzana' , 'naranja', 'kiwi', 'melon']
    tirada = np.random.randint(0,len(opciones),size = len(opciones))
    print("El resultado de su tirada es el siguiente:")
    for i in tirada:
        print(opciones[i])
    resultado = checklist(tirada)
    if(resultado):
        print("Ha ganado el premio")
    else:
        print("Mala suerte, intentelo de nuevo")

# Llamamos a nuestra función
tragaperras()
