class Node():
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.first = None
        self.len = 0
    
    def append(self, val):
        node = Node(val)
        if self.first:
            current = self.first
            while(current.next != None):
                current = current.next
            current.next = node
            current = node
        else:
            self.first = node
        self.len += 1
    
    def prepend(self, val):
        node = Node(val)
        node.next = self.first
        self.first = node
        self.len += 1
    
    def removeFromValue(self, val):
        current = self.first
        if (self.first.value == val):
            self.first = self.first.next

        previous = None
        current = self.first
        while(current != None):
            if(current.value) == val:
                previous.next = current.next
            previous = current
            current = current.next
        return
    
    def __str__(self):
        current = self.first
        list = ''
        while(current.next != None):
            list += f'{current.value}, '
            current = current.next
        list += f'{current.value}'
        return list


linkedList = LinkedList()
array = [8, 0, 1, 439, 584, 58, 10, 20, 30, 55]

for elem in array:
    linkedList.append(elem)

print(linkedList)

linkedList.prepend(16)

print(linkedList)

linkedList.removeFromValue(16)

linkedList.removeFromValue(58)

print(linkedList)
