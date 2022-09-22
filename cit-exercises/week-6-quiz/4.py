# create a class called Stack. The class should have the following methods: push, pop, and size. The push method should add an item to the stack. The pop method should remove an item from the stack. The size method should return the size of the stack.

class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, elem):
        self.stack.append(elem)
    
    def pop(self):
        self.stack.pop()

    def size(self):
        return len(self.stack)