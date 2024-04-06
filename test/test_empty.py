import sys
sys.path.append('../')

import unittest
from  stack import init

class TestEmptyStack(unittest.TestCase):
  def test_empty_list_empty(self):
    stack = init(0)
    self.assertEqual(stack.is_empty(), True)

  def test_pop(self):
    stack = init(10)
    self.assertEqual(stack.is_empty(), False)

if __name__ == '__main__':
    unittest.main()
