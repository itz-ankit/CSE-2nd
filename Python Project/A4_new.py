class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next: Node = next


class Stack:
    def __init__(self):
        self.top: Node = None

    def isEmpty(self):
        return self.top == None

    def peek(self):
        return self.top.data if self.top else None

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if (self.isEmpty()):
            return None
        data = self.top.data
        self.top = self.top.next
        return data


class Queue:
    def __init__(self):
        self.front: Node = None
        self.rear: Node = None

    def isEmpty(self):
        return self.front == None

    def enQueue(self, data):
        if self.isEmpty():
            self.front = self.rear = Node(data)

        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next

    def deQueue(self):
        if self.isEmpty():
            return None
        data = self.front.data
        self.front = self.front.next

        if self.isEmpty():
            self.rear = None
        return data


def test_stack():
    st = Stack()

    while (True):
        c = int(input("\nEnter 1 to check if stack is empty,2 to peek,3 to push,4 to pop,anything else to exit :"))

        match c:
            case 1:
                print("Stack is", "empty." if st.isEmpty() else "not empty.")

            case 2:
                if st.isEmpty():
                    print("Stack is empty.")
                else:
                    print(st.peek())

            case 3:
                st.push(int(input("Enter value to input :")))

            case 4:
                if st.isEmpty():
                    print("Stack underflow")
                else:
                    print(st.pop())

            case 0:  # for debugging
                temp: Node = st.top
                while (temp):
                    print(temp.data, end=" ")
                    temp = temp.next
                print()

            case _:  # default case
                print("Terminating execution")
                exit()


def test_queue():
    queue = Queue()

    while (True):
        c = int(input("\nEnter 1 to check if queue is empty,2 to view front element,3 to enQueue,4 to deQueue,anything else to exit :"))

        match c:
            case 1:
                print("Queue is", "empty." if queue.isEmpty() else "not empty.")

            case 2:
                if queue.isEmpty():
                    print("Queue is empty.")
                else:
                    print(queue.front.data)

            case 3:
                queue.enQueue(int(input("Enter value to input :")))

            case 4:
                if queue.isEmpty():
                    print("Queue underflow")
                else:
                    print(queue.deQueue())

            case 0:  # for debugging
                temp = queue.front
                while (temp):
                    print(temp.data, end=" ")
                    temp = temp.next
                print()

            case _:  # default case
                print("Terminating execution")
                exit()


choice = str(input("Enter stack or queue to test them :"))
if choice == "stack":
    test_stack()
elif choice == "queue":
    test_queue()
else:
    print("Invalid choice!")
