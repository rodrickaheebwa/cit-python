# create a class called Queue. The class should have the following methods: enqueue, dequeue, and size. The enqueue method should add an item to the queue. The dequeue method should remove an item from the queue. The size method should return the size of the queue.

class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, elem):
        self.queue.insert(0, elem)

    def dequeue(self):
        self.queue.pop()

    def size(self):
        return len(self.queue)