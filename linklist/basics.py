class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def nodecount(head):
        count = 1
        current = head
        while current.next is not  None:
            current = current.next
            count +=1
        return count

n1 = Node(12)
n2 = Node(10)
n3 = Node(15)
n4 = Node(50)
n5 = Node(100)
n6 = Node(200)
n7 = Node(150)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7


print("Node in linked list")
print(nodecount(n4))
