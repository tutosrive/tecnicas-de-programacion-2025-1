import unittest
from list_methods_1 import insert, filled, remove, search

class Tester(unittest.TestCase):
    def test_filled(self):
        self.assertTrue(filled([0, 1, 2, 3], 4)) # True
        self.assertFalse(filled([0, None, 1, 2, 3], 4)) # True (Resultado esperado)
    
    def test_insert(self):
        list1: list[int] = [0, 1, None, 3, 9, None]
        insert(list1, 9999, 2, 4) # Insertar valor nuevo
        # Resultado esperado después de ejecutar "insert": [0, 1, 9999, None, 3, 9]
        self.assertEqual(list1, [0, 1, 9999, None, 3, 9])

    def test_remove(self):
        list1: list[int] = [0, 1, 2, 3, 5, 4]
        remove(list1, 3, 6) # Eliminar el entero 3
        self.assertEqual(list1, [0, 1, 2, None, 5, 4]) # Se espera OK para => [0, 1, 2, None, 5, 4]

    def test_search(self):
        list1: list[int] = [0, 1, 2, 3, 5, 4]
        pos: int = search(list1, 5, 6) # Buscar entero "5" en la lista
        pos2: int = search(list1, 12, 6) # Buscar el entero "12" en la lista
        self.assertEqual(pos, 4) # OK, debería encontrar el entero "5" en posición 4
        self.assertEqual(pos2, -1) # OK, no se encontró el entero "12" en la lista

if __name__ == '__main__':
    unittest.main(verbosity=2)