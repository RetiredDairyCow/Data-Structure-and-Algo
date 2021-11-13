#Linked List Pyton

class myNode(object):
    def __init__(self, data = None):
        self.data = data
        self.nextNode = None

class myLinkedList(object):

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.nextNode
    
    def search(self, elem):
        temp = self.head
        if (temp.data == elem):
                    print("FOUND")
                    return
        while (temp):
            if (temp.data == elem):
                print(f"FOUND => {elem}")
                return
            temp = temp.nextNode
        
        print("Not Found OOOPsss")
        return
    
    def delete(self, elem):
        current = self.head
        prev = None
        if(self.head.data == elem):
            self.head = current.nextNode
            return
        
        while (current):
            try:
                if (current.data == elem):
                    prev.nextNode = current.nextNode
                    current = None
                    break
                else:
                    prev = current
                    current = current.nextNode
            except: 
                f"Element: {elem} could not be deleted"
                return

    def addElem(self, Node):
        """add at the end"""
        temp = self.head
        while temp.nextNode:
            temp = temp.nextNode
        temp.nextNode = Node

    def myadd(self, elem):
        """add at the beginnning O(1)"""
        newElem = myNode(elem)
        newElem.nextNode = self.head
        self.head = newElem

#driver
llist = myLinkedList()
llist.head = myNode("one")
# how to make a new node secondElem = myNode("Second")

#llist.addElem(secondElem)
llist.myadd("second")
llist.myadd("third")
llist.myadd("fourth")
llist.delete("one")
llist.printList()       

#llist.search("second")


 