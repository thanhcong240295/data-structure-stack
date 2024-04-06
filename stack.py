class Node:
  def __init__(self, data: int) -> None:
    self.data = data
    self.next = None

class Stack:
  def __init__(self) -> None:
    self.head = None

  def is_empty(self):
    if self.head == None:
        return True
    else:
        return False
    
  def push(self,data):
    new_node = Node(data)

    if self.head == None:
      self.head = new_node
      return

    new_node.next = self.head
    self.head = new_node

  def pop(self):
    if self.is_empty():
      return None

    popped_node = self.head
    self.head = self.head.next
    popped_node.next = None

    return popped_node.data
  
  def peek(self):
    if self.is_empty():
      return None

    return self.head.data
  
  def revert(self):
    if self.is_empty():
      return None
    
    result = Stack()
    current = self.head

    while current:
      result.push(current.data)
      current = current.next

    return result

  def display(self):
    current = self.head
    while current:
      print(current.data, end=' ')
      current = current.next

  def get_len(self) -> int:
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count

def init(len: int):
  s = Stack()

  for i in range(0, len):
    s.push(i + 1)

  return s
