import unittest as ut
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../code')))
from app1 import add_to_word

class Tester(ut.TestCase):
    def test_add_to_word(self):
        word = add_to_word("Mañana")
        self.assertEqual(word, "añana-Mente")

if __name__ == "__main__":
    ut.main(verbosity=2)