
# using list

class StackList:

    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0


    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not  self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


    def size(self):
        return len(self.items)


stack_list = StackList()
stack_list.push(1)
stack_list.push(2)
stack_list.push(3)

print('Stack using list: ', stack_list.items)
print(f'IS empty? {stack_list.is_empty()}')
print(f'Size : {stack_list.size()}')
print(f'Peek : {stack_list.peek()}')

popped_item = stack_list.pop()
print(f'Popped item : {popped_item}')
print(f'Stack after pop : {stack_list.items}')



# -----  Using collections.deque -------

from collections import deque

class StackDeque:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

# Example usage
stack_deque = StackDeque()

stack_deque.push(1)
stack_deque.push(2)
stack_deque.push(3)

print("Stack using deque:", stack_deque.items)
print("Is empty?", stack_deque.is_empty())
print("Size:", stack_deque.size())
print("Peek:", stack_deque.peek())

popped_item = stack_deque.pop()
print("Popped item:", popped_item)
print("Stack after pop:", stack_deque.items)


"""
Stacks are linear data structures in Python. Storing items in Stacks is based on 
the principles of First-In/Last-Out (FILO) or Last-In/First-Out (LIFO). In Stacks, 
the addition of a new element at one end is accompanied by the removal of an element from the same end. 
The operations ‘push’ and ‘pop’ are used for insertions and deletions, respectively. 
Other functions related to Stack are empty(), size() and top(). 
Stacks can be implemented using modules and data structures from 
the Python library – list, collections.deque, and queue.LifoQueue. 

"""