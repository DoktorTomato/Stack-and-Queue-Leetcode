'''
This script implements stack using linked list and Queue using stack
'''

class Node:
    '''
    This is a node that can be a part of a linked list
    '''
    def __init__(self, data=None, next_data=None) -> None:
        self.data = data
        self.next = next_data

class Stack:
    '''
    This is a stack class
    '''
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def push(self, push_data):
        if self.head is None:
            self.head = Node(push_data)
            self.size += 1
        else:
            self.head = Node(push_data, self.head)
            self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            data_popped = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data_popped

class MyQueue:
    '''
    This is a queue class
    '''
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        self.flag = True

    def push(self, x: int) -> None:
        self.stack_1.push(x)

    def pop(self) -> int:
        if self.stack_1.head is None and self.stack_2.head is None:
            return None
        elif self.stack_2.head is None:
            self.flag = True
        if self.flag:
            while self.stack_1.head:
                self.stack_2.push(self.stack_1.pop())
            self.flag = False
            return self.stack_2.pop()
        elif self.stack_2.head is not None:
            return self.stack_2.pop()

    def peek(self) -> int:
        if self.stack_1.head is None and self.stack_2.head is None:
            return None
        elif self.stack_2.head is None:
            self.flag = True
        if self.flag:
            while self.stack_1.head:
                self.stack_2.push(self.stack_1.pop())
            self.flag = False
            return self.stack_2.head.data
        elif self.stack_2.head is not None:
            return self.stack_2.head.data

    def empty(self) -> bool:
        if self.flag:
            return self.stack_1.head is None
        else:
            return self.stack_2.head is None

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
