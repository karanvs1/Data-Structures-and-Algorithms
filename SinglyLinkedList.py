import tensorflow as tf
class Node:
    def __init__(self, Value = None):
        self.Value = Value
        self.Next = None

class SList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.Next
    
    def insert(self, value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            if location == 0:
                newNode.Next = self.head
                self.head = newNode
            elif location == -1:
                newNode.Next = None
                self.tail.Next = newNode
                self.tail = newNode
            else:
                index = 0
                tempNode = self.head
                while index < location - 1:
                    tempNode = tempNode.Next
                    index += 1
                nextNode = tempNode.Next
                tempNode.Next = newNode
                newNode.Next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traverse(self):
        if self.head == None:
            print('The SLL does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.Value)
                node = node.Next

    def search(self, nodeValue):
        if self.head == None:
            return 'The SLL does not exist'
        else:
            node = self.head
            while node is not None:
                if node.Value == nodeValue:
                    return node.Value
                node = node.Next
            return "The value does not exist in the SLL"
    
    def deleteNode(self, location):
        if self.head == None:
            print('The SLL does not exist')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head , self.tail = None , None
                else:
                    self.head = self.head.Next
            elif location == -1:
                if self.head == self.tail:
                    self.head , self.tail = None , None
                else:
                    node = self.head
                    while node is not None:
                        if node.Next == self.tail:
                            break
                        node = node.Next
                    node.Next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.Next
                    index += 1
                tempNode.Next = tempNode.Next.Next

    def deleteentireSLL(self):
        if self.head == None:
            print('The SLL does not exist')
        else:
            self.head = None
            self.tail = None


Node1 = Node(1)
Node2 = Node(2)

SLL = SList()
SLL.head = Node1
SLL.head.Next = Node2
SLL.tail = Node2
SLL.insert(3,2)
SLL.insert(4,3)

print([node.Value for node in SLL])

SLL.deleteNode(-1)

print([node.Value for node in SLL])

SLL.deleteentireSLL()

SLL.traverse()

print(SLL.search(4))
