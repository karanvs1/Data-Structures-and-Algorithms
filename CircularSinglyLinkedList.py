class Node:
    def __init__(self, Value = None):
        self.Value = Value
        self.Next = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.Next == self.head:
                break
            node = node.Next

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.Next = node
        self.head = node
        self.tail = node
        return 'The CSLL is Created'
    
    def insertCSLL(self, value, location):
        if self.head is None:
            return 'The CSLL does not exist'
        else:
            newNode = Node(value)
            if location == 0:
                newNode.Next = self.head
                self.head = newNode 
                self.tail.Next = newNode
            elif location == -1:
                self.tail.Next = newNode
                newNode.Next = self.head
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.Next
                    index += 1
                newNode.Next = tempNode.Next
                tempNode.Next = newNode
            return 'The node has been successfully created'
        
    def traverseCSLL(self):
        if self.head is None:
            return 'The CSLL does not exist'
        else:
            node = self.head
            while node:
                print(node.Value) 
                node = node.Next
                if node == self.head:
                    break
    
    def searchCSLL(self, value):
        if self.head is None:
            return 'The CSLL does not exist'
        else:
            node = self.head
            while node:
                if node.Value == value:
                    return node.Value
                node = node.Next
                if node == self.tail.Next:
                    return 'The node doest not exist in this CSLL'
    
    def deleteCSLL(self, location):
        if self.head is None:
            print('The CSLL does not exist')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.Next = None
                else:
                    self.head = self.head.Next
                    self.tail.Next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.Next = None
                else:
                    node = self.head
                    while node:
                        if node.Next == self.tail:
                            break
                        node = node.Next
                    node.Next = self.head
                    self.tail = node
            else:
                node = self.head
                index = 0
                while index < location -1:
                    node = node.Next
                    index += 1
                node.Next = node.Next.Next
    
    def deleteentireCSLL(self):
        if self.head is None:
            print('The CSLL does not exist')
        else:
            self.head = None
            self.tail = None

CSLL = CircularSLL()
CSLL.createCSLL(1)

CSLL.insertCSLL(0,0)
CSLL.insertCSLL(2,1)
CSLL.insertCSLL(3,1)
CSLL.insertCSLL(2,2)

print([node.Value for node in CSLL])

CSLL.deleteCSLL(4)

CSLL.deleteentireCSLL()

CSLL.traverseCSLL()

print(CSLL.searchCSLL(6))