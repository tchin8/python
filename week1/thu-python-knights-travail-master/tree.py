class Node:
  def __init__(self, value):
    self._value = value
    self._parent = None
    self._children = []
  
  def add_child(self, node):
    if node not in self._children:
      self._children.append(node)
      if node.parent != self:
        node.parent = self
  
  def remove_child(self, node):
    if node and node in self._children:
      self._children.remove(node)
      node.parent = None

  def depth_search(self, value):
    stack = [self]
    while len(stack):
      node = stack[-1]
      stack.remove(node)
      if node.value == value:
        return node
      stack = stack + node._children
    return None
  
  def breadth_search(self, value):
    queue = [self]
    while len(queue):
      node = queue.pop(0)
      if node.value == value:
        return node
      queue = queue + node._children
    return None

  @property
  def value(self):
    return self._value

  @property
  def children(self):
    return self._children

  @property
  def parent(self):
    return self._parent
  
  @parent.setter
  def parent(self, node):
    if self._parent != None and self in self._parent.children:
      self._parent.remove_child(self)
    self._parent = node
    if node != None:
      node.add_child(self)


# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)

# still failing one test???