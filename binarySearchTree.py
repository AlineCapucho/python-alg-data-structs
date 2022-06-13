class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value, current=None):
        if (self.root == None):
            self.root = Node(value)
            return
        if (current == None):
            current = self.root
        
        if (value < current.value):
            if(current.leftChild == None):
                current.leftChild = Node(value)
                return
            else:
                self.insert(value, current.leftChild)
        elif (value > current.value):
            if(current.rightChild == None):
                current.rightChild = Node(value)
                return
            else:
                self.insert(value, current.rightChild)
        elif (value == current.value):
            raise Exception('Key already in BST.')
    
    def contains(self, value, current=None):
        if (current == None):
            current = self.root
        if(value == current.value):
            return True
        elif(value < current.value and current.leftChild != None):
            return self.contains(value, current.leftChild)
        elif(value > current.value and current.rightChild != None):
            return self.contains(value, current.rightChild)
        
        return False

    def printInOrder(self, current=None):
        if (current == None):
            current = self.root
        
        if(current):
            if(current.leftChild):
                self.printInOrder(current.leftChild)
            print(current.value)
            if(current.rightChild):
                self.printInOrder(current.rightChild)
    
    def printPreOrder(self, current=None):
        if (current == None):
            current = self.root
        
        if(current):
            print(current.value)
            if(current.leftChild):
                self.printPreOrder(current.leftChild)
            if(current.rightChild):
                self.printPreOrder(current.rightChild)
    
    def printPostOrder(self, current=None):
        if (current == None):
            current = self.root
        
        if(current):
            if(current.leftChild):
                self.printPostOrder(current.leftChild)
            if(current.rightChild):
                self.printPostOrder(current.rightChild)
            print(current.value)
        

bst = BinarySearchTree()

a = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]

for elem in a:
    bst.insert(elem)

# bst.printInOrder()
# print()
bst.printPreOrder()
# print()
# bst.printPostOrder()