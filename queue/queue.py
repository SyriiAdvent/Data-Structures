from linked_list_c import LinkedList, Node

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your queue class to implement the Queue?
         What would that look like? How many queues would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(0)
        else:
            return None

#example uses
# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# my_enqueue_item = my_queue.dequeue()
# print(my_enqueue_item)

class LinkedQueue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()


    def __len__(self):
        return self.size