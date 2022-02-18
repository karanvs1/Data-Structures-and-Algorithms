class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode
    
    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
    
    def deQueue(self):
        if self.isEmpty():
            return 'The Queue is Empty'
        else:
            tempnode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
        return tempnode

    def peek(self):
        if self.isEmpty():
            return 'The Queue is empty'
        else:
            return self.linkedlist.head
    
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None

customQ = Queue()
customQ.enqueue(1)
customQ.enqueue(2)
customQ.enqueue(3)
print(customQ)
print(customQ.deQueue())
print(customQ)
        

