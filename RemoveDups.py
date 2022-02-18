from LinkedList import LinkedList

def removeDup(ll):
    if ll.head is None:
        return 
    else:
        currNode = ll.head
        visited = set([currNode.value])
        # visited = set()
        while currNode.next:
            if currNode.next.value in visited:
                currNode.next = currNode.next.next
            else:
                visited.add(currNode.next.value)
                currNode = currNode.next
        print(visited)
        return ll

def removeDup1(ll):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        while currNode:
            runner = currNode
            while runner.next:
                if currNode.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currNode = currNode.next
        return ll




customLL = LinkedList()
customLL.generate(10, 0, 5)
print(customLL)
removeDup(customLL)
print(customLL)