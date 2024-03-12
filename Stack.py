from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0



def reverse_string(string):
    s = Stack()
    new_string = ""
    for c in string:
        s.push(c);
    while (not s.is_empty()):
        new_string += s.pop();
    return new_string

print(reverse_string("We will conquere COVID-19"))

def is_balenced(string):
    stack = Stack()
