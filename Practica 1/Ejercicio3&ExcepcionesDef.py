class Error(Exception):
        pass # estamos diciendo con el pass que la clase anterior es vacia.

class valorDemasiadoPequeno(Error):
        pass

class valorDemasiadoGrande(Error):
        pass

numero = 10
while(True):
    try:
        numero_entrada =int(input("Introduce un numero: "))
        if(numero_entrada < numero):
            raise valorDemasiadoPequeno
        elif(numero_entrada > numero):
            raise valorDemasiadoGrande
        break
    except valorDemasiadoPequeno:
        print("El numero es demasiado pequeño, intentalo de nuevo")
    except valorDemasiadoGrande:
        print("El numero es demasiado grande, intentalo de nuevo")

print("Enhorabuena, has encontrado el numero correcto")
