tamMinimo = False

while not tamMinimo:
    password = input("Introduzca 1 contraseña que contenga al menos 8 caracteres:")
    if(len(password)>=8):
        tamMinimo = True
    else:
        print("La contraseña es demasiada corta. Debe tener al menos 8 caracteres.")

print("OK. Todo en orden")
