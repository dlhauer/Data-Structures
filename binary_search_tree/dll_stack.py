from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = len(self.storage)

    def pop(self):
        node = self.storage.remove_from_tail()
        self.size = len(self.storage)
        return node

    def len(self):
        return self.size
