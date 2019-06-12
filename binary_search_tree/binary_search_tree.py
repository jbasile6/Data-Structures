class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    curNode = self
    while True:
      # if cur node goes left
      if curNode.value > new_node.value:
        # if cur node exists
        if curNode.left is not None:
          #cur node becomes that value
          curNode = curNode.left
        else:
          curNode.left = new_node
          break
      # if cur node goes right
      if curNode.value < new_node.value:
        if curNode.right is not None:
          curNode = curNode.right
        else:
          curNode.right = new_node
          break


  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass

