import sys
sys.path.append('../')

import unittest
from  stack import init

class TestRevertStack(unittest.TestCase):
  def test_revert_list_empty(self):
    stack = init(0)
    self.assertEqual(stack.revert(), None)

  def test_revert_list_empty(self):
    stack = init(10)
    res = stack.revert()
    self.assertEqual(res.get_len(), 10)
    self.assertEqual(res.peek(), 1)

if __name__ == '__main__':
    unittest.main()
