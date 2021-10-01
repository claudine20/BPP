import unittest
import operaciones

class pruebasunitarias(unittest.TestCase):

     # Test Operación de factorial de un numero.
    def test_factorial(self):
        self.assertEqual(operaciones.factorial(5),120)

    # Test Operación de resta entre 2 numeros
    def test_resta(self):
        x=5
        y=2
        resultado = 3
        self.assertEqual(operaciones.resta(x,y),resultado)

    # Test Operación comprobar que 1 numero es primo o no
    def test_es_primo(self):
        n1=3
        n2=4
        self.assertTrue(operaciones.es_primo(n1))
        self.assertFalse(operaciones.es_primo(n2))

     # Test Operación minimo de 1 función
    def test_minimo(self):
        lista_numeros=[2,17,18,23,0,-9]
        self.assertEqual(operaciones.minimo(lista_numeros),-9)




if __name__ == '__main__':
    unittest.main()
