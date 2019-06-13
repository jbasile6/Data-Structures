class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.insert(len(self.storage), value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    store = self.storage
    store[0], store[len(store) - 1] = store[len(store) - 1], store[0]
    m = store.pop(len(store) - 1)
    self._sift_down(0)
    return m

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    store = self.storage
    x = ((index- 1) // 2)
    #stays in the index scope
    if x >= 0:
      if store[index] > store[x]:
        store[index], store[x] = store[x], store[index]
        self._bubble_up(x)
      else:
        return

    else:
      return


  def _sift_down(self, index):
    pass
