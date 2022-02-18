# from QueLinkedList import Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.LeftChild = None
        self.RightChild = None

newBT = TreeNode('Drinks')
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')

newBT.LeftChild = leftChild
newBT.RightChild = rightChild

leftChild.LeftChild = TreeNode('Tea') 
leftChild.RightChild = TreeNode('Coffee')
rightChild.LeftChild = TreeNode('Cola')
rightChild.RightChild = TreeNode('Pepsi')

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.LeftChild)
    preOrder(rootNode.RightChild)
    
def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.LeftChild)
    print(rootNode.data)
    inOrder(rootNode.RightChild)  

def postorder(rootNode):
    if not rootNode:
        return
    postorder(rootNode.LeftChild)
    postorder(rootNode.RightChild)
    print(rootNode.data)

# def levelTraversal(rootNode):
#     customQueue = Queue()
#     customQueue.enqueue(rootNode)
#     while not (customQueue.isEmpty()):
#         root = customQueue.deQueue()
#         print(root.value.data)

#         if (root.value.LeftChild is not None):
#             customQueue.enqueue(root.value.LeftChild)

#         if (root.value.RightChild is not None):
#             customQueue.enqueue(root.value.RightChild)

def levelTraversal(rootNode):
    customQueue = []
    customQueue.append(rootNode)
    while customQueue:
        root = customQueue.pop(0)
        print(root.data)

        if (root.LeftChild is not None):
            customQueue.append(root.LeftChild)

        if (root.RightChild is not None):
            customQueue.append(root.RightChild)

def searchTree(rootNode, nodeValue):
    if rootNode is None:
        return 'The tree does not exist'
    else:
        customQueue = []
        customQueue.append(rootNode)
        while customQueue:
            root = customQueue.pop(0)
            if root.data == nodeValue:
                return root.data
            else:
                if (root.LeftChild is not None):
                    customQueue.append(root.LeftChild)

                if (root.RightChild is not None):
                    customQueue.append(root.RightChild)
        return 'The node does not exist'

def insertNode(rootNode, newNode):
    if rootNode is None:
        rootNode = newNode
    else:
        customQueue = []
        customQueue.append(rootNode)
        while True:
            root = customQueue.pop(0)
            if root.LeftChild is None:
                root.LeftChild = newNode
                break

            elif root.LeftChild is None:
                root.LeftChild = newNode
                break

            if (root.LeftChild is not None):
                customQueue.append(root.LeftChild)

            if (root.RightChild is not None):
                customQueue.append(root.RightChild)

def getLastNode(rootNode):
    if rootNode is None:
        return 'The tree does not exist'
    else:
        customQueue = []
        customQueue.append(rootNode)
        while customQueue:
            root = customQueue.pop(0)

            if root.LeftChild:
                customQueue.append(root.LeftChild)

            if root.RightChild:
                customQueue.append(root.RightChild)

        return root

def deleteLastNode(rootNode, dNode):
    if rootNode is None:
        return 'The Tree Does not exist'
    else:
        if rootNode == dNode:
            rootNode = None
            return
        customQueue = []
        customQueue.append(rootNode)
        while customQueue:
            root = customQueue.pop(0)

            if root.RightChild:
                if root.RightChild is dNode:
                    root.RightChild = None
                    return
                else:
                    customQueue.append(root.RightChild)

            if root.LeftChild:
                if root.LeftChild is dNode:
                    root.LeftChild = None
                    return
                else:
                    customQueue.append(root.LeftChild)

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return 'The tree does not exist'
    else:
        customQueue = []
        customQueue.append(rootNode)
        while customQueue:
            root = customQueue.pop(0)
            
            if root.data == nodeValue:
                node = root

            if root.LeftChild:
                customQueue.append(root.LeftChild)

            if root.RightChild:
                customQueue.append(root.RightChild)

        node.data = root.data
        deleteLastNode(rootNode, getLastNode(rootNode))
        
print('Pre Order')
preOrder(newBT)
print('------------')

print('In Order')
inOrder(newBT)
print('------------')

print('Post Order')
postorder(newBT)
print('-------------')

insertNode(newBT, TreeNode('Apple'))

deleteNode(newBT, 'Tea')

deleteLastNode(newBT, getLastNode(newBT))

print('Level Traversal')
levelTraversal(newBT)
print('--------------')

print(searchTree(newBT, 'Hot'))

print(getLastNode(newBT).data)

