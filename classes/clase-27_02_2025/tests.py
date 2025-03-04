import unittest as ut
from stack import *
from queue import *

class Tester(ut.TestCase):
    def test_stack_isEmpty(self):
        self.assertTrue(isEmpty(0)) # True
        self.assertFalse(isEmpty(1)) # True
    
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
    
    def test_stack_pop_reference(self):
        stack:list[int] = [10, 11, 12]
        top_reference:list[int] = [2]
        value_reference:list[int] = [None]
        wasRemoved:int = pop_reference(stack, top_reference, value_reference)
        self.assertEqual(wasRemoved, 1) # Debe ser cierto
        self.assertEqual(value_reference[0], 12) # Debe ser cierto
        # Simulando lista vacía (top = 0)
        stack:list[int] = [0, 0, 0]
        top_reference:list[int] = [0]
        value_reference:list[int] = [None]
        wasRemoved:int = pop_reference(stack, top_reference, value_reference)
        self.assertEqual(wasRemoved, 0) # Debe ser cierto
        self.assertEqual(value_reference[0], None) # Debe ser cierto

    def test_stack_pop_multireturn(self):
        stack:list[int] = [10, 11, 12]
        top = 2
        wasRemoved, top, value = pop_multi_return(stack, top)
        # Se espera que las preposiciones sean verdaderas
        self.assertEqual(wasRemoved, 1)
        self.assertEqual(top, 1)
        self.assertEqual(value, 12)
        self.assertEqual(stack[top], 11)
        # Cuando lista vacía
        stack:list[int] = [0, 0, 0]
        top = 0
        wasRemoved, top, value = pop_multi_return(stack, top)
        # Se espera que las preposiciones sean verdaderas
        self.assertEqual(wasRemoved, 0)
        self.assertEqual(top, 0)
        self.assertEqual(value, None)
        self.assertEqual(stack[top], 0)

if __name__ == '__main__':
    ut.main(verbosity=2)