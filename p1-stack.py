
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def peek(self):
        return self.top.data

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data

    def print(self):
        while self.top is not None:
            print(self.pop())


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(2)
    print(stack.peek())
    # stack.print()
