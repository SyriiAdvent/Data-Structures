"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is less we move it to the left branch
        # if left node is taken we call insert() on that node again
        if self.value == value and self.right is None:
            self.right = BSTNode(value)
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # if value is larger we move it to the Right branch
        # if Right node is taken we call insert() on that node again
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
                

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        counter = self.value if self.value is not None else None

        # while checking:
        if target >= counter:
            if counter == target:
                return True
            else:
                if self.right is not None:
                    return self.right.contains(target)

        elif target <= counter:
            if counter == target:
                return True
            else:
                if self.left is not None:
                    return self.left.contains(target)
        return False
            

    # Return the maximum value found in the tree
    def get_max(self):
        max = 0
        counter = self.value if self.value is not None else None

        # while checking:
        if counter > max:
            max = counter
            if self.right is not None:
                max = self.right.get_max()
        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # def fn(self, node):
    #     print(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if self.left:
            self.left.in_order_print(self.left)
        elif self.right:
            self.right.in_order_print(self.right)
        print(self.value)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        print(self.value)
        if self.left:
            print(self.left.value)
            if self.right:
                print(self.right.value)
            self.left.bft_print(self.left)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


my_tree = BSTNode(10) # Main
my_tree.insert(2) # left
my_tree.insert(20) # right
my_tree.insert(1) # left
my_tree.insert(1) # ???

my_tree.insert(5) # Left -> right
my_tree.insert(21) # right
my_tree.insert(22) # right
my_tree.insert(9) # ??

# my_tree.contains(22)
# my_tree.contains(5)
# my_tree.contains(9)

# my_tree.get_max()
# my_tree.in_order_print()
my_tree.bft_print()