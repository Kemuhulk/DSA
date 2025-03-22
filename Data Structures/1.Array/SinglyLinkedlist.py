class Node:
    """A Node of a Singly Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to next node

class LinkedList:
    """A Singly Linked List"""
    def __init__(self):
        self.head = None  # First node (head)

    def append(self, data):
        """Add a node at the end"""
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.next = new_node  # Link last node to new node

    def insert_at(self, index, data):
        """Insert a node at a specific position"""
        new_node = Node(data)
        if index == 0:  # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(index - 1):
            if not temp.next:
                raise IndexError("Index out of range")
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        """Print the linked list"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(40)
print("Before insertion:")
ll.display()

ll.insert_at(2, 30)  # Insert 30 at index 2
print("After inserting 30 at index 2:")
ll.display()
