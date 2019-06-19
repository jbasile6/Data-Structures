class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    # add item to back of list
    return self.storage.append(item)
  
  def dequeue(self):
    # check to see if length is greater than zero
    if len(self.storage) > 0:
      # removed item from 0 index
      return self.storage.pop(0)

  def len(self):
    return len(self.storage)
