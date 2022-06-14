class minHeap():
    def __init__(self):
        self.heap = []
        self.size = len(self.heap)
    
    def getLeftChildIndex(self, index):
        return index*2 + 1
    
    def getRightChildIndex(self, index):
        return index*2 + 2
    
    def getParentIndex(self, index):
        return (index-1)//2
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < len(self.heap)
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < len(self.heap)
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def getLeftChild(self, index):
        if self.hasLeftChild(index):
            return self.heap[self.getLeftChildIndex(index)]

    def getRightChild(self, index):
        if self.hasRightChild(index):
            return self.heap[self.getRightChildIndex(index)]
    
    def getParent(self, index):
        if self.hasParent(index):
            return self.heap[self.getParentIndex(index)]

    def peek(self):
        if(self.size == 0):
            raise Exception("Heap is empty.")
        return self.heap[0]
    
    def poll(self):
        if(self.size == 0):
            raise Exception("Heap is empty.")
        min = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop(self.size - 1)
        self.size = len(self.heap)
        self.heapifyDown()
        return min
    
    def add(self, val):
        self.heap.append(val)
        self.size = len(self.heap)
        self.heapifyUp()

    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            rightChild = self.getRightChild(index)
            leftChild = self.getLeftChild(index)

            if (self.hasRightChild(index) and rightChild < leftChild):
                smallerChildIndex = self.getRightChildIndex(index)
            
            if(self.heap[index] < self.heap[smallerChildIndex]):
                break
            else:
                self.heap[index], self.heap[smallerChildIndex] = self.heap[smallerChildIndex], self.heap[index]
                index = smallerChildIndex
    
    def heapifyUp(self):
        index = len(self.heap) - 1
        while(self.hasParent(index) and self.getParent(index) > self.heap[index]):
            self.heap[self.getParentIndex(index)], self.heap[index] = self.heap[index], self.heap[self.getParentIndex(index)]
            index = self.getParentIndex(index)


heap = minHeap()
a = [10, 4, 82, 126, 1, 8, 57]

for elem in a:
    heap.add(elem)

print(heap.peek())
heap.poll()
print(heap.peek())
heap.poll()
print(heap.peek())
heap.add(0)
print(heap.peek())
