# type: ignore
try:
    import sys 
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)
    
    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)
    
    def teste_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3),
            (-5, 5, 0),
            (100, 100, 200),
        )
        for n in x_y_saidas:
            with self.subTest(n=n):
                x, y, saida = n
                self.assertEqual(soma(x, y), saida)

if __name__ == '__main__':
    unittest.main(verbosity=2)