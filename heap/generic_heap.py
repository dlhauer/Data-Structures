class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        if not comparator:
            self.comparator = lambda x, y: x > y
        else:
            self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        val = self.get_priority()
        self._sift_down(0)
        self._bubble_up(self.get_size() - 1)
        return val

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if self.get_size() <= 1:
            return
        if index % 2 == 0:
            parent_index = (index-2)//2
        else:
            parent_index = (index-1)//2
        if not self.comparator(self.storage[index], self.storage[parent_index]):
            return
        self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
        if parent_index > 0:
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        last_index = len(self.storage)-1
        left_child_index = (2*index)+1
        right_child_index = (2*index)+2
        if left_child_index > last_index:
            del self.storage[index]
            return
        elif right_child_index > last_index:
            right_child_index = None
        if not right_child_index or self.comparator(self.storage[left_child_index], self.storage[right_child_index]):
            swap_index = left_child_index
        else:
            swap_index = right_child_index
        self.storage[index], self.storage[swap_index] = self.storage[swap_index], self.storage[index]
        self._sift_down(swap_index)
