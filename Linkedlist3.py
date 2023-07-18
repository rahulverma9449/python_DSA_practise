class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                return  # Found and deleted the node, exit the function

            current = current.next

    def print_list(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next


# Create a new doubly linked list
my_list = DoublyLinkedList()

# Append elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Prepend an element to the list
my_list.prepend(0)

# Print the list
my_list.print_list()
# Output: 0 1 2 3

# Delete an element from the list
my_list.delete(2)

# Print the updated list
my_list.print_list()
# Output: 0 1 3