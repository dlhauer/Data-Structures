from doubly_linked_list import DoublyLinkedList, ListNode


class LRUCache:

    def __init__(self, limit=10):
        self.max = limit
        self.cache = DoublyLinkedList()
        self.size = 0
        self.storage = dict()

    def get(self, key):
        node = self.storage.get(key)
        if not node or (not node.next and not node.prev):
            return None
        self.cache.move_to_end(node)
        return node.value

    def set(self, key, value):
        node = self.storage.get(key)
        if node:
            self.cache.move_to_front(node)
            node.value = value
        else:
            self.cache.add_to_tail(value)
            self.storage.update({key: self.cache.tail})
        self.size = len(self.cache)
        if self.size > self.max:
            self.cache.remove_from_head()
            self.size = len(self.cache)
