from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size = len(self.storage)

    def dequeue(self):
        node = self.storage.remove_from_tail()
        self.size = len(self.storage)
        return node

    def len(self):
        return self.size
