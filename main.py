class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value

    def peek(self):
        if self.top:
            return self.top.value

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_stack()
