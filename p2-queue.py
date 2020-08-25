class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def peek(self):
        return self.head.data

    def add(self, data):
        node = Node(data)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def print(self):
        while self.head is not None:
            print(self.remove())

if __name__ == '__main__':
    q = Queue()
    q.add(0)
    q.add(1)
    q.add(2)
    q.add(0)
    q.print()
