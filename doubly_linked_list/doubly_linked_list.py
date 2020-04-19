
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print_list(self, direction):
        node = self.head if direction == 'forward' else self.tail
        while(node):
            print(node.value)
            node = node.next if direction == 'forward' else node.prev

    def add_to_head(self, value):
        prev_head = self.head
        self.head = ListNode(value, None, prev_head)
        prev_head.prev = self.head
        self.length += 1

    def remove_from_head(self):
        prev_head = self.head
        self.head = self.head.next
        self.head.prev = None
        prev_head.next = None
        self.length -= 1
        return prev_head.value

    def add_to_tail(self, value):
        prev_tail = self.tail
        self.tail = ListNode(value, prev_tail, None)
        prev_tail.next = self.tail
        self.length += 1

    def remove_from_tail(self):
        prev_tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        prev_tail.prev = None
        self.length -= 1
        return prev_tail.value

    def move_to_front(self, node):
        if not node or not isinstance(node, ListNode):
            return
        prev_head = self.head
        node.prev.next = node.next
        node.next.prev = node.prev
        self.head = node
        self.head.prev = None
        self.head.next = prev_head
        prev_head.prev = self.head

    def move_to_end(self, node):
        if not node or not isinstance(node, ListNode):
            return
        prev_tail = self.tail
        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail = node
        self.tail.next = None
        self.tail.prev = prev_tail
        prev_tail.next = self.tail

    def delete(self, node):
        if not node or not isinstance(node, ListNode):
            return
        if node.prev == None:
            self.head = node.next
            self.head.prev = None
            node.next = None
        elif node.next == None:
            self.tail = node.prev
            self.tail.next = None
            node.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None

    """Returns the highest value currently in the list"""

    def get_max(self):
        pass


node = ListNode('dan')
lizt = DoublyLinkedList(node)
lizt.add_to_head('hau')
lizt.add_to_head('sam')
# print(lizt.length)
# lizt.print_list('forward')
val = lizt.remove_from_head()
lizt.add_to_tail('lil')
val = lizt.remove_from_tail()
node = lizt.tail
lizt.delete(node)
lizt.print_list('forward')
lizt.print_list('rev')
# print(lizt.length)
