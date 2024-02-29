# Using List

class QueueList:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):

        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)


queue_list = QueueList()

queue_list.enqueue(7)
queue_list.enqueue(8)
queue_list.enqueue(23)

print("Queue using list:", queue_list.items)
print("Is empty?", queue_list.is_empty())
print("Size:", queue_list.size())
print("Front:", queue_list.front())

dequeued_item = queue_list.dequeue()
print("Dequeued item:", dequeued_item)
print("Queue after dequeue:", queue_list.items)

# --- Using collections.deque ---

from collections import deque

class QueueDeque:

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()

    def front(self):

        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)


print('-' * 60)

queue_deque = QueueDeque()

queue_deque.enqueue(1)
queue_deque.enqueue(2)
queue_deque.enqueue(3)

print("Queue using deque:", queue_deque.items)
print("Is empty?", queue_deque.is_empty())
print("Size:", queue_deque.size())
print("Front:", queue_deque.front())

dequeued_item = queue_deque.dequeue()
print("Dequeued item:", dequeued_item)
print("Queue after dequeue:", queue_deque.items)
"""
 Similar to Stacks, Queues are linear data structures. However, items are stored based on the
 First- In/ First- Out (FIFO) principle. In a Queue, the item that is least recently added is removed first.
 Operations related to Queue include Enqueue (adding elements), Dequeue (deleting elements), Front and Rear.
 Like Stacks, Queues can be implemented using modules and data structures from
 the Python library – list, collections.deque, and queue.

"""
