def leer_enteros():
    num_intentos = 0
    while(num_intentos < 3):
        n = input("Introduzca un numero entero:")
        try:
            n=int(n)
            print("Todo ok")
            return # NOTE:
        except:
            num_intentos +=1
    print("Has ingresado un valor incorrecto en 3 ocasiones. Se acabaron tus oportunidades")


# LLamo a la función
leer_enteros()
