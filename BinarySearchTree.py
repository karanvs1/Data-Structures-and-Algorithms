class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = TreeNode(nodeValue)
        else:
            insert(rootNode.left, nodeValue)
    else:
        if rootNode.right is None:
            rootNode.right = TreeNode(nodeValue)
        else:
            insert(rootNode.right, nodeValue)
    return 'The node has been successfully added'

def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.left)
        preOrderTraversal(rootNode.right)

def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        inOrderTraversal(rootNode.left)
        print(rootNode.data)
        inOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        postOrderTraversal(rootNode.left)
        postOrderTraversal(rootNode.right)
        print(rootNode.data)

def levelOrderTraversal(rootNode):
    customQueue = []
    customQueue.append(rootNode)
    while customQueue:
        root = customQueue.pop(0)
        print(root.data)
        if root.left:
            customQueue.append(root.left)
        if root.right:
            customQueue.append(root.right)

def search(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print('The Node is found')
    elif nodeValue < rootNode.data:
        if rootNode.left.data == nodeValue:
            print('The Node is found')
        else:
            search(rootNode.left)
    else:
        if rootNode.right.data == nodeValue:
            print('The Node is found')
        else:
            search(rootNode.right)
    
def minValueNode(bstNode):
    current = bstNode
    while current.left:
        current = current.left
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodeValue)
    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        if rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp

        temp = minValueNode(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)
    return rootNode

newBST = TreeNode(None) 
insert(newBST, 70)
insert(newBST, 50)
insert(newBST, 90)
insert(newBST, 30)
insert(newBST, 60)
insert(newBST, 80)
insert(newBST, 100)
insert(newBST, 20)
insert(newBST, 40)

print(newBST.data)
print(newBST.left.data)
print('---------------')

print('Pre Order Traversal')
preOrderTraversal(newBST)
print('---------------')

print('Inorder Traversal')
inOrderTraversal(newBST)
print('---------------')

print('Post Order Traversal')
postOrderTraversal(newBST)
print('---------------')

deleteNode(newBST, 20)
print('Lever order Traversal')
levelOrderTraversal(newBST)

search(newBST, 50)
