class Node:
    def __init__(self, Value = None):
        self.Value = Value
        self.Next = None
        self.Prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.Next

    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.Next = None
        node.Prev = None
        self.head = node
        self.tail = node
        return 'The Doubly Linked List is created'
    
    def insterDLL(self, value, location):
        if self.head is None:
            return 'The doubly linked list does not exist'
        else:
            newNode = Node(value)
            if location == 0:
                newNode.Prev = None
                newNode.Next = self.head
                self.head.Prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.Next = None
                newNode.Prev = self.tail
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
    
    def traverseDLL(self):
        if self.head is None:
            return 'The DLL does not exist'
        else:
            node = self.head
            while node:
                print(node.Value)
                node = node.Next
    
    def reversetraverseDLL(self):
        if self.head is None:
            return 'The DLL does not exist'
        else:
            node = self.tail
            while node:
                print(node.Value)
                node = node.Prev
    
    def searchDLL(self, value):
        if self.head is None:
            return 'The DLL does not exist'
        else:
            node = self.head
            while node:
                if node.Value == value:
                    return node.Value
                node = node.Next
            return 'The value does not exist in the DLL'
    
    def deleteDLL(self, location):
        if self.head is None:
            return 'The DLL does not exist'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.Next
                    self.head.Prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.Prev
                    self.tail.Next = None
            else:
                currnode = self.head
                index = 0
                while index < location - 1:
                    currnode = currnode.Next
                    index += 1
                currnode.Next = currnode.Next.Next
                currnode.Next.Prev = currnode
            print('The node has been successfully deleted')
                
    def deleteentireDLL(self):
        node = self.head
        while node:
            node.Prev = None
            node = node.Next
        self.head = None
        self.tail = None
        print('The DLL has been deleted')

doublyLL = DLL()
doublyLL.createDLL(3)

doublyLL.insterDLL(0,0)
doublyLL.insterDLL(4,-1)
doublyLL.insterDLL(1,1)
doublyLL.insterDLL(2,2)


print([node.Value for node in doublyLL])

doublyLL.traverseDLL()

doublyLL.reversetraverseDLL()

print(doublyLL.searchDLL(4))

doublyLL.deleteDLL(2)
print([node.Value for node in doublyLL])

print(doublyLL.deleteentireDLL())

print([node.Value for node in doublyLL])