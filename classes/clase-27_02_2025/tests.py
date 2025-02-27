import unittest as ut
from stack import *
from queue import *

class Tester(ut.TestCase):
    def test_stack_isEmpty(self):
        self.assertFalse(isEmpty(0)) # True
        self.assertTrue(isEmpty(1)) # True
    
    def test_stack_isFull(self):
        stack: list[int] = [0, 6, 23, 1]
        top: int = 3
        self.assertTrue(isFull(stack, top)) # True
        self.assertFalse(isFull(stack, top - 1)) # True
    
    def test_stack_push(self):
        stack: list[int] = [0, 1, 2, None]
        push(stack, 12, 2)
        self.assertEqual(stack, [0, 1, 2, 12]) # Debe ser verdadero
        stack: list[int] = [0, 1, 2, None]
        push(stack, 12, 2)
        self.assertNotEqual(stack, [0, 1, 2, None]) # Debe ser verdadero

if __name__ == '__main__':
    ut.main(verbosity=2)