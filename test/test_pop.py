import sys
sys.path.append('../')

import unittest
from  stack import init

class TestPopStack(unittest.TestCase):
  def test_pop_list_empty(self):
    stack = init(0)
    self.assertEqual(stack.pop(), None)

  def test_pop(self):
    stack = init(10)
    pop = stack.pop()
    self.assertEqual(pop, 10)
    self.assertEqual(stack.get_len(), 9)

if __name__ == '__main__':
    unittest.main()
