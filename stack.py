class Node():
    def __init__(self, val):
        self.value = val
        self.next = None

class Stack():
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            self.size -= 1
            return value
        raise Exception("Empty stack.")
    
    def peek(self):
        if self.top:
            return self.top.value
        raise Exception("Empty stack.")
    
    def size(self):
        return self.size

stack = Stack()
array = [1,2,3,4,3]
for elem in array:
    stack.push(elem)
print(stack.peek())