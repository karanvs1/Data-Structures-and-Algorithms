from LinkedList import LinkedList, Node

def intersection(ll1, ll2):
    if ll1.tail is not ll2.tail:
        return False
    else:
        len1 = len(ll1)
        len2 = len(ll2)

        shorter = ll1 if len1 < len2 else len2
        longer = ll2 if len1 < len2 else len1

        diff = len(longer) - len(shorter)
        longerNode = longer.head
        shorterNode = shorter.head
        
        for i in range(diff):
            longerNode = longerNode.next

        while longerNode is not shorterNode:
            longerNode = longerNode.next
            shorterNode = shorterNode.next

        return longerNode

def addSameNode(ll1, ll2, value):
    node = Node(value)
    ll1.tail.next = node
    ll1.tail = node
    ll2.tail.next = node
    ll2.tail = node

ll1 = LinkedList()
ll1.generate(3, 0, 10)

ll2 = LinkedList()
ll2.generate(4, 0 ,10)

addSameNode(ll1, ll2, 11)
addSameNode(ll1, ll2, 16)

print(ll1)
print(ll2)

print(intersection(ll1, ll2))