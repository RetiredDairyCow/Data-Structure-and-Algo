'''Min heap properties (indexed at 1)
Let P = Parent and parent is always smaller than its children
Left Child = 2P
Right Child = 2P + 1
Min heap is implemented as an array of Nodes (N)'''

class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def insert(self, key):
        '''insert at end and "swim up"'''
        self.heapList.append(key)
        self.currentSize = self.currentSize + 1
        self.swimUp(self.currentSize)
    
    def swimUp(self, size):
        '''size also acts like an index. 0 being root node'''
        while size // 2 > 0:
            if self.heapList[size] < self.heapList[size//2]:
                temp = self.heapList[size//2]
                self.heapList[size//2] = self.heapList[size]
                self.heapList[size] = temp
            size = size // 2 #keep swimming up
    
    def delMin(self):
        '''O(n) since root is the smallest child'''
        min = self.heapList[1]
        #now set last node as root
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop() #remove last node
        self.swimDown(1)
        return min
    
    def swimDown(self, index):
        while(index*2) <= self.currentSize:
            mc = minChild(index)
            if self.heapList[index] > self.heapList[mc]:
                temp = self.heapList[index]
                self.heapList[index] = self.heapList[mc]
                self.heapList[mc] = temp
            index = mc 

    
    def minChild(self, index):
        '''returns index on minimum child'''
        if index*2+1 > self.currentSize: #if no right child and only left child
            return index*2
        elif (heapList[index*2] < heapList[index*2 + 1]):
            return index*2
        else:
            return index*2+1
    
    
list = [5, 11,3, 14, 18, 19, 21, 33, 17, 27]
myMinHeap = MinHeap()
for x in list:
    print("Inserting: " + str(x))
    myMinHeap.insert(x)

print(myMinHeap.heapList)