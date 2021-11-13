class Hashtable:
    def __init__(self):
        self.elementArray = [0] * 10000
    

    def getHashIndex(self, element):
        return hash(element)

    def addToTable(self, element):
        hashIndex = self.getHashIndex(element) % 1000
        print("Hash index = {}".format(hashIndex))
        print("Added: " + element) 
        self.elementArray[hashIndex] = element

    def deleteFromTable(self, element):
        hashIndex = hash(element) % 1000
       
        self.elementArray.pop(hashIndex)
        print("Deleted: " + element)


e1 = str(10) #cannot add mutable datatypes to hashtable
e2 = str(20)
str1 = "Olivia"
str2 = "Rishi"

myHashTable = Hashtable()
#myHashTable.addToTable(str1)
myHashTable.addToTable(str1)
myHashTable.addToTable(str2)

myHashTable.deleteFromTable(str1)
#print(myHashTable[148])



#myHashTable.elementArray.pop(148)
#print("Deleted should be 0 ->" + str(myHashTable.elementArray[148]))