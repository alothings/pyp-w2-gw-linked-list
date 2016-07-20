from .interface import AbstractLinkedList
from linked_list import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """
    def __init__(self, elements=None):
        if not elements:
            self.start = None
            self.end = None
        else:
            new_node = Node(elements[0])
            self.start = new_node
            self.end = new_node
            for element in elements[1:]:
                self.append(element)
            
    def __str__(self):
        pass

    def __len__(self):
        current_node = self.start
        count = 0
        while not current_node.next == None:
            current_node = current_node.next
            count += 1
        return count

    def __iter__(self):
        # return self
        pass
    
    

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        pass

    def append(self, elem):
        new_node = Node(elem)
        if not self.start and not self.end:
            self.start = new_node
        else:
            self.end.next = new_node
        self.end = new_node

    def count(self):
        pass

    def pop(self, index=None):
        pass