
class TreeNode():
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

def insert(node, key):
    '''Node is root initially
       Go left or right depending of key value. 
       Insert New node when a leaf is found'''
    if node is None:
       return TreeNode(key)
    if  key < node.key:
        node.leftChild = insert(node.leftChild, key)
    else:
        node.rightChild = insert(node.rightChild, key)
    return node

def searchTree(root, key):
    '''Search for a key. Go left sub tree is key is < node.key
    else go right sub tree'''
    if (root is None or root.key == key):
        return root
    elif key < root.key:
        return searchTree(root.leftChild, key)
    else:
        return searchTree(root.rightChild, key)
    #return None

def findMinNode(root):
    minNode = root
    while minNode.leftChild is not None:
         minNode = minNode.leftChild
    return minNode.key

def deleteNode(root, key):
    if root is None:
        return None
    if key < root.key:
        root.leftChild = deleteNode(root.leftChild, key)
    elif key > root.key:
        root.rightChild = deleteNode(root.rightChild, key)
    #key is found at this step. Delete now
    #no child
    if root.key == key:
        if not root.leftChild and not root.rightChild:
            return None
        #one child
        if not root.leftChild and root.rightChild: #no left child
            return root.rightChild
        if not root.rightChild and root.leftChild:
            return root.leftChild
        #if both child 
        minNode = findMinNode(root.rightChild)
        root.key = minNode
        root.rightChild = deleteNode(root.rightChild, root.key)
    
    return root
    
    
def preOrder(root):
    '''Root->Left->Right'''
    if root:
        print(root.key, end=" ")
        preOrder(root.leftChild)
        preOrder(root.rightChild)   

def inOrder(root):
    '''Left->Root->Right'''
    if root:
        inOrder(root.leftChild)
        print(root.key, end=" ")
        inOrder(root.rightChild)

def postOrder(root):
    '''Left->Right->Root'''
    if root:
        postOrder(root.leftChild)
        postOrder(root.rightChild)
        print(root.key, end=" ")

myRoot = TreeNode(10)
myRoot = insert(myRoot, 5)
myRoot = insert(myRoot, 15)
myRoot = insert(myRoot, 13)
myRoot = insert(myRoot, 20)
myRoot = insert(myRoot, 25)
myRoot = insert(myRoot, 3)
deleteNode(myRoot, 15)
preOrder(myRoot)
#postOrder(myRoot) 