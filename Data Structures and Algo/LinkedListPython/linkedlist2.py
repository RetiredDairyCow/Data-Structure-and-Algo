class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class myLL:
    def __init__(self):
        self.head = None

    def addNode(self, elem):
        newNode = Node(elem)
        newNode.nextNode = self.head
        self.head = newNode

    def printLL(self):
        temp = self.head
        while temp:
            print(f"Node data = {temp.data}")
            temp = temp.nextNode

    def searchInList(self, elem):
        temp = self.head
        if temp.data == elem:
            print("Element found")
            return
        temp = temp.nextNode
        while(temp):
            if temp.data == elem:
                print(f"Element -> {temp.data} found!")
                return
            temp = temp.nextNode 
        print("Element not found")

    def delete(self, elem):
        


 #driver 
myList = myLL() 
myList.addNode("ash")
myList.addNode("Olivia")
myList.printLL()
myList.searchInList("sjdhsak")

