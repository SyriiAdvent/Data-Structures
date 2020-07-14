"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        pass
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        
        # if DLL is not empty
        # if self.length != 0:
        else:
            # set new node's next to current head
            new_node.next = self.head
            # set head's prev to new node
            self.head.prev = new_node
            # set head to the new node
            self.head = new_node


    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
        # store the value of the head
        temp_node = self.head
        # decrement the length of the DLL
        self.length -= 1
        # delete the head
        # if head.next is not None
        if self.head.next is not None:
            # set head.next's prev to None
            self.head.next.prev = None
            # set head to head.next
            self.head = self.head.next
        # else (if head.next is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None

        # return the value
        return temp_node.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1

        # if DLL is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tail's next to new node
            self.tail.next = new_node
            # set tail to the new node
            self.tail = new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None
        # store the value of the tail
        temp_node = self.tail
        # decrement the length of the DLL
        self.length -= 1
        # delete the tail
        # if tail.prev is not None
        if self.tail.prev is not None:
            # set tail.prev's next to None
            self.tail.prev.next = None
            # set tail to tail.prev
            self.tail = self.tail.prev
        # else (if tail.prev is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None

        # return the value
        return temp_node.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        temp_node = self.delete(node)
        self.add_to_head(temp_node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        temp_node = self.delete(node)
        self.add_to_tail(temp_node)

    def remove_node_pointers(self, node):
        if node.prev is not None:
		# if node.prev isnt None
		# set the before nodes next node to the old nodes next node
		# (1) --> skip --> (3)
            node.prev.next = node.next

        if node.next is not None:
            # if node.next isnt None
		    # set the next nodes prev node to the old nodes prev node
		    # (1) <-- skip <-- (3)
            node.next.prev = node.prev
			
		# Then we can set the old node's prev and next to none
        node.next = None
        node.prev = None

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0: return None

        self.length -= 1
        if self.head == self.tail:
            self.head, self.tail = None, None

            return node.value
        
        elif node == self.head:
            self.head = self.head.next
            node.next, self.head.prev = None, None

            return node.value

        elif node == self.tail:
            self.tail = self.tail.prev
            node.prev, self.tail.next = None, None

            return node.value

        else:
            node_prev, node_next = node.prev, node.next
            node_prev.next, node_next.prev = node.next, node.prev

            return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    So if a Linked list of numers, return all of them added
    """
    def get_max(self):
        curr = self.head
        max = 0

        while curr is not None:
            if curr.value > max:
                max = curr.value
            curr = curr.next
        return max

# my_dbl_Linklist = DoublyLinkedList()

# # Add to Head
# my_dbl_Linklist.add_to_head(1)
# my_dbl_Linklist.add_to_head(2)
# # my_dbl_Linklist.remove_from_head()

# my_dbl_Linklist.add_to_tail(3)
# my_dbl_Linklist.add_to_tail(4)

# my_dbl_Linklist.remove_from_tail()


# print(f"HEAD: {my_dbl_Linklist.head.value}")
# print(f"TAIL: {my_dbl_Linklist.tail.value}")