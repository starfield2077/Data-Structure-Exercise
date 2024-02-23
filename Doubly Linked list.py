class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev

        print(llstr)


    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        self.tail = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        if self.tail is None:
            self.tail = Node(data, None, None)

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

        itr = self.tail
        while itr.prev:
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



if __name__ == "__main__":
    ll = doublyLinkedList()
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(35)
    ll.insert_at_end(42)
    ll.print_forward()
    ll.print_backward()
