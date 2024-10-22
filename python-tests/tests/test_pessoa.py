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
from pessoa import Pessoa
from unittest.mock import patch, Mock

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Davi', 'Tanaka')
        self.p2 = Pessoa('Mauro', 'Tanaka')

    def test_pessoa_nome_attr_nome_tem_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Davi')
        self.assertEqual(self.p2.nome, 'Mauro') 

    def test_attr_nome_e_instancia_de_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_sobrenome_attr_nome_tem_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Tanaka')
        self.assertEqual(self.p2.sobrenome, 'Tanaka')
        
    def test_attr_sobrenome_e_instancia_de_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertEqual(self.p1.dados_obtidos, False)
        self.assertEqual(self.p2.dados_obtidos, False)

    def test_obter_todos_os_dados_com_sucesso(self):
        with patch('pessoa.requests.get') as request_falso:
            request_falso.return_value = Mock(ok=True)
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)


            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('pessoa.requests.get') as request_falso:
            request_falso.return_value = Mock(ok=False)
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)


            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)

    def test_obter_os_dados_sequencia_e_falha_sequencial(self):
        with patch('pessoa.requests.get') as request_falso:
            request_falso.return_value = Mock(ok=True)

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

            request_falso.return_value = Mock(ok=False)

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)


if __name__ == '__main__':
    unittest.main(verbosity=2)
