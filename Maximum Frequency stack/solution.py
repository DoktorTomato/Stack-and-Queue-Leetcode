'''
This script implements stack using linked list and Queue using stack
'''
from collections import deque

class Node:
    '''
    This is a node that can be a part of a linked list
    '''
    def __init__(self, data=None, next_data=None) -> None:
        self.data = data
        self.next = next_data

    def copy(self):
        return Node(self.data, self.next)

class FreqStack:

    def __init__(self):
        self.head = deque()

    def push(self, val: int) -> None:
        self.head.append(val)

    def pop(self) -> int:
        most_freq = Node(None, 0)
        self.head.reverse()
        for el in self.head:
            count = self.head.count(el)
            if count > most_freq.next:
                most_freq = Node(el, count)
        new_head = deque()
        flag = True
        for el in self.head:
            if el != most_freq.data:
                new_head.append(el)
            elif el == most_freq.data and not flag:
                new_head.append(el)
            else:
                flag = False
        new_head.reverse()
        self.head = new_head
        return most_freq.data

freq_stack = FreqStack()
freq_stack.push(5)
freq_stack.push(7)
freq_stack.push(5)
freq_stack.push(7)
freq_stack.push(4)
freq_stack.push(5)
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
