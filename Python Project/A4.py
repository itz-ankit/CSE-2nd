class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top else None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data


# Stack example
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:")
while not stack.is_empty():
    print(stack.pop())

# Queue example
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:")
while not queue.is_empty():
    print(queue.dequeue())
