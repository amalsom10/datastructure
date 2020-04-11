class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = node()

    # Add a new node data
    def append(self,data):
        new_data = node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_data

    # Display the list of nodes
    def display(self):
        elements = []
        current_node = self.head
        print ("self.head : {}".format(current_node))
        while current_node.next is not None:
            elements.append(current_node)
        print ("Elements in the linked list : {}".format(elements))

    # Length of Linkedlist
    def count(self):
        count = 0
        current_node = self.head
        while current_node.next is not None:
            count += 1
            current_node = current_node.next
        print ("count of elements in the Linkedlist: {}".format(count))


    # Get elements in a particular index
    def get(self,index):
        if index >= self.count() or index <0 :
            print ("Invalid index value")
        current_index = 0
        current_node = self.head
        while True:
            if current_index = index:
                ele = current_node.data
            current_node = current_node.next
            current_index +=1

    # Erase an elements in Linkedlist
    def erase(self,index):
        if index >= self.count or index < 0:
            print ("Invalid index value")
        current_node = self.head
        previous_node = current_node
        current_index = 0
        while True:
            if current_index = index:
                previous_node.next = current_node.next
            previous_node = current_node
            current_node = current_node.next
            current_index +=1
                                









if __name__ == "__main__":
    main()
