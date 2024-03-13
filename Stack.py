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


def is_balanced(string):
    s = Stack()
    for c in string:
        if c == '(':
            s.push(c)
        elif c == '[':
            s.push(c)
        elif c == '{':
            s.push(c)
        elif c == ')':
            if not s.is_empty() and s.peek() == '(':
                s.pop()
            else:
                s.push(c)
        elif c == '}':
            if not s.is_empty() and s.peek() == '{':
                s.pop()
            else:
                s.push(c)
        elif c == ']':
            if not s.is_empty() and s.peek() == '[':
                s.pop()
            else:
                s.push(c)
        else:
            continue
    return s.is_empty()


res = is_balanced("({a+b})")
print(res)
res1 = is_balanced("))((a+b}{")
print(res1)
res2 = is_balanced("((a+b))")
print(res2)
res3 = is_balanced("))")
print(res3)
res4 = is_balanced("[a+b]*(x+2y)*{gg+kk}")
print(res4)