class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            nextelement = current.next
            current.next = previous
            previous = current
            current = nextelement
        self.head = previous

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

llist = LinkedList()
llist.head = n1
n1.next = n2
n2.next = n3

#llist.reverse()
llist.printList()