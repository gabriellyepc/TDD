import unittest
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import modulo_aprovacao

# teste_todos_passam
# teste_ninguem_passa
# teste_nota_7
# teste_um_aluno

lista = [{"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},
		{"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"},
		{"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}]
		

class TestAprovacao(unittest.TestCase):
    def teste(self):
        self.assertEqual(modulo_aprovacao.aprovacao(lista), lista)

unittest.main(verbosity=2)