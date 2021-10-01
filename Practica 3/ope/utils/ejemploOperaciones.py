class operacionesMatematicas:
    """
    Operaciones matematicas. Esta clase resuelve una serie de operaciones sobre datos de tipo entero.
    Atributos:
    op1:
        Este es el primier operando(del tipo entero) que se va utilizar en los metodos de operaciones matematicas.
        En el caso de que el operador que se aplique sea unario, se tendra en cuenta op1 y no op2.
    op2:
        este es el primier operando(del tipo entero) que se va utilizar en los metodos de operaciones matematicas.

    Metodos:

    suma:
        Suma los operando op1 y op2
    resta:
        Resta los operandos op1 y op2
    division:
        Divide el operando op1 entre el operando op2. Si op2=0, devuelve 0.
    multiplicacion:
        Realiza el producto entre los operandos op1 y op2.
    es_primo:
        Determina si el operando op1 es o no primo.
    factorial:
        Calcula el factorial de op1.

    Ejemplos:
    >>> import operacionesMatematicas
    >>> OM = operacionesMatematicas(5,8)
    >>> resultado_suma =OM,suma()
    >>> resultado_factorial = OM.factorial()
    """

    # Creamos el contructor
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def suma(self):
        """
        Metodo suma. Aplica el algoritmo de la suma sobre los operados op1 y op2
        Inputs:
            self.op1
            self.op2
        Outputs:
            res: resultado de sumar op1 y op2.
        """
        res = self.op1+ self.op2
        return res

    def resta(self):
        """
        Metodo resta. Aplica el algoritmo de la resta sobre los operados op1 y op2
        Inputs:
            self.op1
            self.op2
        Outputs:
            res: resultado de restar op1 y op2.
        """
        res = self.op1 - self.op2
        return res


    def producto(self):
        """
        Metodo producto. Aplica el algoritmo del producto sobre los operados op1 y op2
        Inputs
        ------
            self.op1
            self.op2
        Outputs
        ----------
            res: resultado de multiplicar op1 y op2.
        """
        res = self.op1*self.op2
        return res


    def division(self):
        """
        Metodo resta. Aplica el algoritmo de la division sobre los operados op1 y op2.
        Si el denominador (op2) es igual a 0, este metodo devolvera 0.
        Inputs
        ------
            self.op1
            self.op2
        Outputs
        -------
            res: resultado de dividir  op1 entre op2.
        """
        res = self.op1/self.op2 if(self.op2 !=0) else 0

        return res

    def primo(self):
        """
        Metodo primo. Determina si el operando op1 es un numero primo
        Inputs
        ------
            self.op1
        Outputs
        -------
            True si selp.op1 es primo, False en caso contrario.
        """
        es_primo = True
        for i in range (2,self.op1-1):
            if(self.op1%i == 0):
                es_primo=False
        return es_primo

    def factorial(self):
        """
        Metodo para calcular el factorial de un numero.
        """
        assert(n>= 0)
        fct= 1
        for i in range(1,op1+1):
            fct *=i
        return fct
