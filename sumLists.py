from LinkedList import LinkedList

def sum(ll1, ll2):
    n1 = ll1.head
    n2 = ll2.head
    ll = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add((result)%10)
        carry = (result)//10
    if carry != 0:
        ll.add(carry)
    return ll

list1 = LinkedList()
print(list1.generate(6, 0, 9))
list2 = LinkedList()
print(list2.generate(4, 0, 9))
print(sum(list1,list2))