# Paso 1: Creamos la clase calculadora con sus 2 atributos
class calculadora:
    num1 = 0
    num2 = 0
    ##
    # operacionesCalculadora. Esta clase resuelve una serie de operaciones sobre datos de tipo entero.
    # Atributos:
    # num1:
    #   Este es el primer operando(del tipo entero) que se va utilizar en los metodos de operaciones matematicas.
    # num2:
    #   Este es el segundo operando(del tipo entero) que se va utilizar en los metodos de operaciones matematicas.

    # Metodos:

    # sumar:
    #   Suma los operandos num1 y num2

    # multiplicar:
    #   Realiza el producto entre los operandos num1 y num2

    # restar:
    #   Resta los operandos num1 y num2


    # dividir:
    #   Divide el operando num1 entre el operando num2.


##
    # Paso 2: Creamos el constructor para usar las variables de la  clase calculadora.
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

##
    # Paso 3: Creamos los 4 metodos(funciones) para hacer las operaciones con la calculadora.
    def sumar(self):
        ##
        #Metodo sumar. Aplica el algoritmo de la suma sobre los operandos num1 y num2.
        #Inputs:
        #    self.num1
        #    self.num2
        #Outputs:
        #    resultadoSuma : resultado de sumar num1 y num2.
        resultadoSuma = self.num1 + self.num2
        return print(f"La suma es:{resultadoSuma}")

    def multiplicar(self):
        ##
        #Metodo multiplicar. Aplica el algoritmo del producto sobre los operandos num1 y num2
        #Inputs
        #------
        #    self.num1
        #    self.num2
        #Outputs
        #----------
        #    resultadoMultiplicar: resultado de multiplicar num1 y num2.
        resultadoMultiplicar = self.num1 * self.num2
        return print(f"La multiplicación es:{resultadoMultiplicar}")


    def restar(self):
        ##
        #Metodo restar. Aplica el algoritmo de la resta sobre los operandos num1 y num2.
        #Inputs:
        #    self.num1
        #    self.num2
        #Outputs:
        #    resultadoRestar: resultado de restar num1 y num2.
        resultadoRestar = self.num1 -  self.num2
        return print(f"La resta es:{resultadoRestar}")


    def dividir(self):
        ##
        #Metodo dividir. Aplica el algoritmo de la division sobre los operandos num1 y num2.
        #Inputs
        #------
        #    self.num1
        #    self.num2
        #Outputs
        #-------
        #    res: resultado de dividir num1 entre num2.
        resultadoDividir = self.num1 / self.num2
        return print(f"La division es:{resultadoDividir}")


##
# Paso 5:Creamos el objeto "calculadora" y llamamos a los métodos que hemos creado anteriormente.

calculadora = calculadora(10,5)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir()
