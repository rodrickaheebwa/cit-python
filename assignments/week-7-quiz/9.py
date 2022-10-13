#9. Using only functions and lists, Implement a queue data structure. The queue should have the following methods: enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO)


queue = []

def enqueue(elem):
    queue.insert(0, elem)

def dequeue():
    queue.pop()

def size():
    return len(queue)