#implementing stack in python
#implementing stack using list in python
class Stack():
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)
        return data

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]
    
    def is_empty(self):
        return len(self.elements) == 0

    def printStack(self):
        print(self.elements)


def checkBracketBalance(input):

    if (len(input) % 2 != 0):
        return False
    
    opening_brackets = set('([{')
    pairs = set([ ('(',')'), ('[',']'), ('{','}') ])
    
    stack = Stack()
    
    for bracket in input:
        if bracket in opening_brackets:
            stack.push(bracket)
        else:
            poppedBracked = stack.pop()
            if (poppedBracked, bracket) not in pairs:
                return False
    return stack.is_empty()
    

if checkBracketBalance('[{}]([])'):
    print("Balanced")
else:
    print("Not Balanced")

if checkBracketBalance('{[}]([])'):
    print("Balanced")
else:
    print("Not Balanced")



