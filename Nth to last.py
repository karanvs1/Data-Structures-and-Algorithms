from LinkedList import LinkedList

def nth_last(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head
    index = 0
    
    while index < n:
        pointer2 = pointer2.next
        index += 1

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1.value

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
print(nth_last(customLL, 9))