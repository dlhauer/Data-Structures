from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = BinarySearchTree(value)
        if value < self.value:
            if not self.left:
                self.left = node
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = node
            else:
                self.right.insert(value)

    def contains(self, target):
        if not self.value:
            return False
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    def get_max(self):
        max_val = self.value
        if self.right:
            max_val = self.right.get_max()
        return max_val

    def for_each(self, cb):
        self.value = cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------
    def in_order_print(self, node):
        if not self.left and not self.right:
            print(self.value)
            return
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    def bft_print(self, node):
        queue = Queue()
        temp_node = node
        while temp_node:
            print(temp_node.value)
            if temp_node.left:
                queue.enqueue(temp_node.left)
            if temp_node.right:
                queue.enqueue(temp_node.right)
            temp_node = queue.dequeue()

    def dft_print(self, node):
        stack = Stack()
        temp_node = node
        while temp_node:
            print(temp_node.value)
            if temp_node.right:
                stack.push(temp_node.right)
            if temp_node.left:
                stack.push(temp_node.left)
            temp_node = stack.pop()

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if not node:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


def times_two(n):
    return 2 * n


tree = BinarySearchTree(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(9)
tree.insert(4)
# tree.for_each(times_two)
# print(tree.value)
# print(tree.value)
tree.pre_order_dft(tree)
