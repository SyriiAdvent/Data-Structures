from linked_list_c import LinkedList, Node

"""
A stack is a data structure whose primary purpose is to store and
return elements in; Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        else:
            return None

# example uses
# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# my_popped_stack_item = my_stack.pop()
# print(my_popped_stack_item)

class LinkedStack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            x = self.storage.remove_tail()
            self.size -= 1
            return x
        else:
            return None
    
    def __len__(self):
        return self.size

my_stack_list = LinkedStack()