class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
        else:
            print("Stack is full!")

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Stack is empty!")

    def traverse(self):
        print(self.stack)

stack = Stack(5)
for i in range(6):
    stack.push(i)

stack.traverse()
for i in range(6):
    stack.pop()
stack.traverse()