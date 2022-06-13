class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def enqueue(self, val):
        node = Node(val)

        if self.head and self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = self.head

        self.size += 1
    
    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value
        raise Exception('Empty queue.')

    def peek(self):
        if self.head:
            return self.head.value
        raise Exception('Empty queue.')
    
    def size(self):
        pass

myQueue = Queue()
array = [1,2,3,4,5]

for elem in array:
    myQueue.enqueue(elem)

print(myQueue.peek())
myQueue.dequeue()