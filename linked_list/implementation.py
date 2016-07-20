from .interface import AbstractLinkedList
from linked_list.node import Node

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
        l = []
        iterNode = self.start
        while iterNode is not None:
            l.append(iterNode.elem)
            iterNode = iterNode.next
        return str(l)
        

    def __len__(self):
        iterNode = self.start
        count = 0
        while iterNode is not None:
            count += 1
            iterNode = iterNode.next
        return count

# http://stackoverflow.com/questions/2180578/python-why-cant-i-iterate-over-a-list-is-my-exception-class-borked
    def __iter__(self):
        self.iterNode = self.start
        # return iter(self)
        return self

    def __next__(self):
        if self.iterNode == None:
            raise StopIteration()
        value = self.iterNode.elem
        self.iterNode = self.iterNode.next
        return value
        
    def next(self):
        if self.iterNode == None:
            raise StopIteration()
        value = self.iterNode.elem
        self.iterNode = self.iterNode.next
        return value

    def __getitem__(self, index):
        iterNode = self.start
        count = 0
        while count < index:
            count += 1
            iterNode = iterNode.next
        return iterNode.elem

    def __add__(self, other):
        for item in other:
            self.append(item)
        return self

    def __iadd__(self, other):
        for item in other:
            self.append(item)
        return self
        
    def __eq__(self, other):
        return list(self) == other
        
    def __ne__(self, other):
        return list(self) == other

    def append(self, elem):
        new_node = Node(elem)
        if not self.start and not self.end:
            self.start = new_node
        else:
            self.end.next = new_node
        self.end = new_node

    def count(self):
        return len(self)

    def pop(self, index=None):
        if index > len(self)-1:     # if index larger than size
            raise IndexError
        
        if self.start is None:      # if empty list
            raise IndexError
        
        if self.start.next is None: # if one element, set start and end to None
            temp = self.start
            self.start = None
            self.end = None
            return temp
            
        iterNode = self.start.next
        temp = self.start
        counter = 0
        
        if index is None:
            index = self.count() 
            print(index)
        
        if index == 0:
            temp = self.start
            self.start = self.start.next
            return temp
        
        while iterNode.next is not None and counter < index - 1:
            counter += 1
            temp = temp.next
            iterNode = iterNode.next

        if temp.next is not None:
            temp.next = iterNode.next
        
        else:
            iterNode = temp
            temp = None
            
        print("HELLO")
        print(self.__str__())
        self.__len__()
        self.count()
        print(self.__str__())
        return iterNode.elem
