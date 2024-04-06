import sys
sys.path.append('../')

import unittest
from  stack import init

class TestPushStack(unittest.TestCase):
  def test_push_list_empty(self):
    stack = init(0)
    stack.push(11)
    self.assertEqual(stack.get_len(), 1)

  def test_push(self):
    stack = init(10)
    stack.push(11)
    self.assertEqual(stack.get_len(), 11)

if __name__ == '__main__':
    unittest.main()
