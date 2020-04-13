class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = Node()

    # Add a new node data
    def append(self,data):
        new_data = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_data

    # Display the list of nodes
    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print ("Elements in the linked list : {}".format(elements))

    # Length of Linkedlist
    def count(self):
        count = 0
        current_node = self.head
        while current_node.next is not None:
            count += 1
            current_node = current_node.next
        print ("count of elements in the Linkedlist: {}".format(count))
        return int(count)

    # Get elements in a particular index
    def get(self,index):
        current_index = 0
        current_node = self.head
        current_node = current_node.next
        while True:
            current_node = current_node.next
            if current_index == index:
                ele = current_node.data
            current_index +=1


    # Erase an elements in Linkedlist
    def erase(self,index):
        if index >= self.count() or index < 0:
            print ("Invalid index value")
        current_node = self.head
        previous_node = current_node
        current_index = 0
        while True:
            if current_index == index:
                previous_node.next = current_node.next
            previous_node = current_node
            current_node = current_node.next
            current_index +=1

my_list = Linkedlist()
while True:
    print("Select the option below\n1. Append\n2. Display\n3. Length\n4. Get\n5.Erase\n")
    choose = int(input())
    if choose == 1:
        print("Enter data to be appened\n")
        data = input()
        my_list.append(data)
    elif choose == 2:
        print("Elements in the Linkedlist\n")
        my_list.display()
    elif choose == 3:
        print("Length of the Linkedlist\n")
        my_list.count()
    elif choose == 4:
        print("Enter the index of the elements to be return\n")
        index = int(input())
        my_list.get(index)
    elif choose == 5:
        print ("Enter the index of the elements to be erased\n")
        index = int(input())
        my_list.erase(index)
    else:
        print("Invalid entry")
