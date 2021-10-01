# Ejecutaremos este ejercicio sin control de errores
# y veremos que nuestro programa no podrá seguir funcionando con el error

fichero = open("numeros.txt", "r")
lines = fichero.readlines()
print(lines)

print("He terminado de leer y a partir de aqui puedo ejecutar más cosas")
resultado = 10-5
print(resultado)
