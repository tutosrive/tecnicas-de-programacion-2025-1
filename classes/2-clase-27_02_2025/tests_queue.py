import unittest as ut
import queue1 as q

class Tester(ut.TestCase):
    def test_queue_isEmpty(self):
        self.assertTrue(q.isEmpty(-1)) # True
        self.assertFalse(q.isEmpty(1)) # True
    
    def test_queue_isFull(self):
        queue: list[int] = [0, 6, 23, 1]
        end:list[int] = [3]
        self.assertTrue(q.isFull(queue, end[0])) # True
        self.assertFalse(q.isFull(queue, end[0] - 1)) # True
    
    def test_queue_enqueue(self):
        queue: list[int] = [0, 1, 2, None]
        end:list[int] = [2]
        q.enqueue(queue, 12, end)
        self.assertEqual(queue, [0, 1, 2, 12]) # Debe ser verdadero
        queue: list[int] = [0, 1, 2, None]
        end:list[int] = [2]
        q.enqueue(queue, 12, end)
        self.assertNotEqual(queue, [0, 1, 2, None]) # Debe ser verdadero
    
    def test_queue_desenqueue(self):
        queue:list[int] = [10, 11, 12]
        head:int = 1
        wasDesenqueue, head, value = q.desenqueue(queue, head)
        self.assertEqual(wasDesenqueue, 1) # Debe ser cierto
        self.assertEqual(value, 11) # Debe ser cierto
        self.assertEqual(head, 2) # Debe ser cierto
        # Simulando COLA vacía (head = -1)
        queue:list[int] = [0, 0, 0]
        head:int = -1
        wasDesenqueue, head, value = q.desenqueue(queue, head)
        self.assertEqual(wasDesenqueue, 0) # Debe ser cierto
        self.assertEqual(value, None) # Debe ser cierto
        self.assertEqual(head, -1) # Debe ser cierto
        # Simulando COLA llena (head = len(queue) - 1)
        queue:list[int] = [9, 10, 12]
        head:int = 2
        wasDesenqueue, head, value = q.desenqueue(queue, head)
        self.assertEqual(wasDesenqueue, 1) # Debe ser cierto
        self.assertEqual(value, 12) # Debe ser cierto
        # al estar la cabecera en la última posición, una vez "desencolado" el elemento, quedará VACÍA (head = -1)
        self.assertEqual(head, -1) # Debe ser cierto

if __name__ == '__main__':
    ut.main(verbosity=2)