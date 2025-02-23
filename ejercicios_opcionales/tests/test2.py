import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../code')))
from app2 import add_to_words

class Tester(unittest.TestCase):
    def test_add_to_words(self):
        phrase = add_to_words("Hola Mundo")
        self.assertEqual(phrase, ['ola-Hente', 'Mundo'])

if __name__ == "__main__":
    unittest.main(verbosity=2)