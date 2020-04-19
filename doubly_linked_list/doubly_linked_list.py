
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
        node = ListNode(value, None, prev_head)
        self.head = node
        if prev_head:
            prev_head.prev = self.head
        if not self.tail:
            self.tail = node
        self.length += 1

    def remove_from_head(self):
        if not self.head:
            return
        prev_head = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
            if not self.head.next:
                self.tail = self.head
        else:
            self.tail = None
        prev_head.next = None
        self.length -= 1
        return prev_head.value

    def add_to_tail(self, value):
        prev_tail = self.tail
        node = ListNode(value, prev_tail, None)
        self.tail = node
        if prev_tail:
            prev_tail.next = self.tail
        if not self.head:
            self.head = node
        self.length += 1

    def remove_from_tail(self):
        if not self.tail:
            return
        self.length -= 1
        prev_tail = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
            if not self.tail.prev:
                self.head = self.tail
        else:
            self.head = None
        prev_tail.prev = None
        return prev_tail.value

    def move_to_front(self, node):
        if not node or not isinstance(node, ListNode) or node.prev == None:
            return
        prev_head = self.head
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.head = node
        self.head.prev = None
        self.head.next = prev_head
        prev_head.prev = self.head

    def move_to_end(self, node):
        if not node or not isinstance(node, ListNode) or node.next == None:
            return
        prev_tail = self.tail
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        node.next.prev = node.prev
        self.tail = node
        self.tail.next = None
        self.tail.prev = prev_tail
        prev_tail.next = self.tail

    def delete(self, node):
        if not node or not isinstance(node, ListNode):
            return
        if node.prev == None and node.next == None:
            self.head = None
            self.tail = None
        elif node.prev == None:
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
        self.length -= 1

    def get_max(self):
        node = self.head
        max_val = self.head.value
        while(node):
            if type(max_val) != type(node.value):
                print("Brah, I can't compare values of different types.\n")
                return
            max_val = max(max_val, node.value)
            node = node.next
        return max_val
