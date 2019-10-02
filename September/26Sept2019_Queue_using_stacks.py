"""
Implement a queue class using two stacks.
A queue is a data structure that supports the FIFO protocol (First in = first out).
Your class should support the enqueue and dequeue methods like a standard queue.
"""


class Queue:
    def __init__(self):
        self.stack_en = list()

    def enqueue(self, val):
        self.stack_en.append(val)

    def dequeue(self):
        return self.stack_en.pop(0)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
