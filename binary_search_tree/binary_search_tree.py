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

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

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
tree.insert(2)
tree.insert(11)
tree.insert(3)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(25)
tree.insert(13)
tree.insert(20)
tree.for_each(times_two)
print(tree.value)
