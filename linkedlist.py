
class Node:

  def __init__(self, value):
    self.data = value
    self.next = None
    self.prev = None
  
  def __str__(self):
    return self.data

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.current = None
    self.length = 0
  
  def push(self, value):
    """
    Add new node to the tail
    """
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
      self.current = self.head
    else:
      newNode = Node(value)
      newNode.prev = self.tail
      self.tail.next = newNode
      self.tail = self.tail.next
    self.length = self.length + 1

  def pop(self, index):
    """
    Pop node by index
    """
    if index < 0 or index >= self.length:
      raise "Index out of range"
    node = self.head
    i=0
    while i<=index:
      if i==index:
        if self.current == node:
          self.current = node.next if node.next else node.prev
        if node.prev:
          node.prev.next = node.next
          node.next.prev = node.prev
        else:
          self.head = node.next
        break
      node = node.next
      i = i+1
    self.length = self.length - 1
  
  def next(self):
    """
    Go to the next node
    """
    if self.current and self.current.next:
      self.current = self.current.next
      return True
    return False

  def previous(self):
    """
    Go to the previous node
    """
    if self.current and self.current.prev:
      self.current = self.current.prev
      return True
    return False
  
  def reset(self):
    self.current = self.head

  def at(self, index):
    """
    Get node by index
    """
    if index < 0 or index >= self.length:
      raise "Index out of range"
    node = self.head
    i=0
    while i<=index:
      if i==index:
        return node
      node = node.next
      i = i+1
  
  def __str__(self):
    """
    Get lists dara as string value
    """
    values = ""
    node = self.head
    while node:
      values = values + "{} ".format(node.__str__())
      node = node.next
    return values

if __name__ == "__main__":
  
  l = LinkedList()
  l.push("python")
  l.push("go")
  l.push("c++")
  l.push("docker")
  l.push("kubernetes")

  print("===========Print ALL=============")
  print(l.__str__())

  print("========Print at index 2=========")
  print(l.at(2).__str__())

  print("=========Pop at index 3==========")
  l.pop(3)
  print(l.__str__())

  print("=========Print length============")
  print(l.length)

  print("=======Print next node===========")
  is_current = True
  while(is_current):
    print(l.current.__str__())
    is_current = l.next()

  print("=======Print previous node=======")
  is_current = True
  while(is_current):
    print(l.current.__str__())
    is_current = l.previous()
