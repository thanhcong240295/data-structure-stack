import sys
sys.path.append('../')

import unittest
from  stack import init

class TestPeekStack(unittest.TestCase):
  def test_peek_list_empty(self):
    stack = init(0)
    self.assertEqual(stack.peek(), None)

  def test_peek(self):
    stack = init(10)
    stack.push(11)
    self.assertEqual(stack.peek(), 11)

if __name__ == '__main__':
    unittest.main()
