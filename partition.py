from LinkedList import LinkedList
from LinkedList import Node

def partition(ll, x):
    newLL = LinkedList()
    newLL.add(ll.head.value)
    node = ll.head.next
    while node:
        if node.value < x:
            newNode = Node(node.value)
            newNode.next = newLL.head
            newLL.head = newNode
        else:
            newLL.add(node.value)
        node = node.next
    return newLL

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(partition(customLL, 30))
