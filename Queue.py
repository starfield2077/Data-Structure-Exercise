import threading
import time
from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.appendleft(val)

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
 
    def front(self):
        return self.queue[-1]

q = Queue()
orders = ['pizza','samosa','pasta','biryani','burger']
def add_order(orders):
    for order in orders:
        print("placing order for: ", order)
        q.enqueue(order)
        time.sleep(0.5)

def serve_order():
    time.sleep(1.5)
    while not q.is_empty():
        print("Now serving: ", q.dequeue())
        time.sleep(2)

if __name__ == '__main__':

    t1 = threading.Thread(target=add_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()


def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    produce_binary_numbers(10)