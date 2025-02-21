import unittest
from list_methods_1 import insert, filled

class Tester(unittest.TestCase):
    def test_filled(self):
        self.assertTrue(filled([0, 1, 2, 3], 4)) # True
        self.assertFalse(filled([0, None, 1, 2, 3], 4)) # True (Resultado esperado)
    
    def test_insert(self):
        list1 = [0, 1, None, 3, 9, None]
        insert(list1, 9999, 2, 4) # Insertar valor nuevo
        # Resultado esperado después de ejecutar "insert": [0, 1, 9999, None, 3, 9]
        self.assertTrue(list1, [0, 1, 9999, None, 3, 9])

if __name__ == '__main__':
    unittest.main(verbosity=2)