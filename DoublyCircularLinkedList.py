
class Node:
    def __init__(self, value= None):
        self.Value = value
        self.Next = None
        self.Prev = None

class DCLL:
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
            
    def createDCLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.Next = node
        node.Prev = node
        return 'The DCLL has been created'

    def insertDCLL(self, value, location):
        if self.head is None:
            return 'The DCLL does nit exist'
        else:
            newNode = Node(value)
            if location == 0:
                newNode.Next = self.head
                newNode.Prev = self.tail
                self.head.Prev = newNode
                self.head = newNode
                self.tail.Next = newNode
            elif location == -1:
                newNode.Next = self.head
                newNode.Prev = self.tail
                self.head.Prev = newNode
                self.tail.Next = newNode
                self.tail = newNode
            else:
                currNode = self.head
                index = 0
                while index < location -1:
                    currNode = currNode.Next
                    index += 1
                newNode.Next = currNode.Next
                newNode.Prev = currNode
                newNode.Next.Prev = newNode
                currNode.Next = newNode

    def traverseDCLL(self):
        node = self.head
        while True:
            print(node.Value)
            if node == self.tail:
                break 
            node = node.Next
    
    def reversetraverseDCLL(self):
        node = self.tail
        while True:
            print(node.Value)
            if node == self.head:
                break 
            node = node.Prev
    
    def searchDCLL(self, value):
        if self.head is None:
            return 'The DCLL does not exist'
        else:
            node = self.head
            while node:
                if node.Value == value:
                    return node.Value   
                node = node.Next
                if node == self.tail.Next:
                    return 'The node doest not exist in this CSLL'

    def deleteDCLL(self, location):
        if self.head is None:
            return 'The linked list does not exist'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.Prev = None
                    self.head.Next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.Next
                    self.head.Prev = self.tail
                    self.tail.Next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.Prev = None
                    self.head.Next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.Prev
                    self.tail.Next = self.head
                    self.head.prev = self.tail
            else:
                currnode = self.head
                index = 0
                while index < location - 1:
                    currnode = currnode.Next
                    index += 1
                currnode.Next = currnode.Next.Next
                currnode.Next.Prev = currnode

    def deleteentireDCLL(self):
        self.tail.Next = None
        node = self.head
        while node:
            node.Prev = None
            node = node.Next
        self.head = None
        self.tail = None
        print('The DCLL has been successfully deleted')


circulardoublylinkedlist = DCLL()
circulardoublylinkedlist.createDCLL(1)

circulardoublylinkedlist.insertDCLL(0,0)
circulardoublylinkedlist.insertDCLL(3,-1)
circulardoublylinkedlist.insertDCLL(2,2)

print([node.Value for node in circulardoublylinkedlist])

# circulardoublylinkedlist.traverseDCLL()
# circulardoublylinkedlist.reversetraverseDCLL()

# print(circulardoublylinkedlist.searchDCLL(1))

# circulardoublylinkedlist.deleteDCLL(3)

# circulardoublylinkedlist.deleteentireDCLL()