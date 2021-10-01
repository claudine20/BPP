# Ejecutaremos este el mismo ejercicio con control de errores o excepciones
# y veremos que nuestro programa puede seguir funcionando con el error del fichero:

try:
    fichero = open("numeros.txt", "r")
    lines = fichero.readlines()
    print(lines)
except:
    print("No he encontrado el fichero. O no existe o esta en otro directorio")
else:# Este else es optativo, es simplemente para cerrar el fichero y el buffer.
    fichero.close()
print("He terminado de leer y a partir de aqui puedo ejecutar más cosas")
resultado = 10-5
print(resultado)
