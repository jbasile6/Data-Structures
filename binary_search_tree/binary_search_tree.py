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
    curNode = self
    yesContains = False
    while True:
      # if cur node val is the target return true
      if curNode.value == target:
        yesContains = True
        break
      # if not, check if target val would be found to the left or right

      # target would be found to the left
      elif curNode.value > target:
        # check if cur node left exists(similar method used in insert)
        if curNode.left is not None:
          curNode = curNode.left
        else:
          #does not exist, break, returns false
          break
      elif curNode.value < target:
        if curNode.right is not None:
          curNode = curNode.right
        else:
          break
    return yesContains



  def get_max(self):
    # keep going right until cur node right does not exist
    curNode = self
    if curNode.right is not None:
      return curNode.right.get_max()
    else: 
      return curNode.value

  def for_each(self, cb):
    curNode = self
    if curNode.left is not None:
      self.left.for_each(cb)
    if curNode.right is not None:
      self.right.for_each(cb)
    return cb(curNode.value)

