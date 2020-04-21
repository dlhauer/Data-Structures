class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        if len(self.storage) > 1:
            self._bubble_up(len(self.storage)-1)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        if index % 2 == 0:
            parent_index = (index-2)//2
        else:
            parent_index = (index-1)//2
        if self.storage[index] <= self.storage[parent_index]:
            return
        self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
        if parent_index > 0:
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        pass


heap = Heap()
heap.insert(3)
heap.insert(25)
heap.insert(19)
heap.insert(17)
heap.insert(16)
heap.insert(40)
heap.insert(24)
heap.insert(30)
print(heap.storage)
