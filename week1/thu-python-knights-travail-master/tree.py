class Node:
  def __init__(self, value):
    self._value = value
    self._parent = None
    self._children = []

  def value(self):
    return self._value

  def children(self):
    return self._children

  @property
  def parent(self):
    return self._parent
  
  @parent.setter
  def parent(self, value):
    self._parent = value
    # calls the 'add_child' method of the parent node passing itself as the node 
    # to add to the list of children
  
  def add_child(self, node):
    self._children.append(node)
    # and update the node's '_parent' if the node is not already in '_children'
  
  def remove_child(self, node):
    self._children.remove(node)
    self._parent = None
    
  

  