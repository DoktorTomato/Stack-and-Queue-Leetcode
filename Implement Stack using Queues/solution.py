'''
This script has classes to implement Linked list Queue and Stack(using queue)
'''

class Node:
    '''
    This is a node that can be a part of a linked list
    '''
    def __init__(self, data=None, next_data=None) -> None:
        self.data = data
        self.next = next_data
    def __repr__(self) -> str:
        return f'Node({self.data}, {self.next})'

class Queue:
    '''
    This is the Queue class
    '''
    def __init__(self) -> None:
        self.head = Node()

    def push(self, push_data):
        cur = self.head
        if cur.data is None:
            cur.data = push_data
        else:
            while cur.next:
                cur = cur.next
            cur.next = Node(push_data)

    def pop(self):
        if self.head is None or self.head.data is None:
            return
        pop_data = self.head.data
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = Node()
        return pop_data

    def __repr__(self) -> str:
        res = "Queue("
        cur = self.head
        while cur:
            res += repr(cur)
            cur = cur.next
        res += ')'
        return res

class MyStack:
    '''
    This is the stack implemented using a queue
    '''
    def __init__(self) -> None:
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, push_data):
        self.q1.push(push_data)

    def pop(self):
        temp_data = False
        while self.q1.head.data:
            if temp_data:
                self.q2.push(temp_data)
            temp_data = self.q1.pop()
        pop_data = temp_data
        while self.q2.head.data:
            temp_data = self.q2.pop()
            self.q1.push(temp_data)
        return pop_data

    def top(self):
        temp_data = False
        while self.q1.head.data:
            temp_data = self.q1.pop()
            self.q2.push(temp_data)
        top_data = temp_data
        while self.q2.head.data:
            temp_data = self.q2.pop()
            self.q1.push(temp_data)
        return top_data

    def empty(self):
        return self.q1.head.data is None
