# Assignment: Singly Linked List implementation

# Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. Your implementation should include 
# the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: Add a node to the end of the list
# Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge cases such as: Deleting a node from an empty list
# Deleting a node with an index out of range Test your implementation with at least one sample list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def print_list(self):
        current = self.head
        if current is None:
            print("List is empty.")
            return
        
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        
        print(" -> ".join(map(str, elements)))

    def delete_nth_node(self, n):
        if self.head is None:
            raise ValueError("Cannot delete from an empty list.")
        
        if n <= 0:
            raise ValueError("Index must be a positive integer. (1-based indexing)")
        
        if n == 1:
            self.head = self.head.next
            return
        
        current = self.head
        count = 1

        while current and count < n - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            raise ValueError("Index {n} out of range.")
        
        current.next = current.next.next

# Sample usage

if __name__ == "__main__":
    new_list = LinkedList()
    new_list.append(1)
    new_list.append(2)
    new_list.append(3)
    new_list.append(4)
    new_list.append(5)

    print("Original List:")
    new_list.print_list()
    print("Trial 1 (Deleting 3rd node)")
    try:
        new_list.delete_nth_node(3)
        print("List after deleting 3rd node:")
        new_list.print_list()
    except ValueError as e:
        print(f"Error: {e}")

    print("Trial 2 (Attempting to delete 10th node)")
    try:
        new_list.delete_nth_node(10)
        print("List after attempting to delete 10th node:")
        new_list.print_list()
    except ValueError as e:
        print(f"Error: {e}")

    print("Trial 3 (Attempting to delete 0th node)")
    # Attempting to delete the 0th node (which is invalid)
    try:
        new_list.delete_nth_node(0)
        print("List after attempting to delete 0th node:")
        new_list.print_list()
    except ValueError as e:
        print(f"Error: {e}")

    print("Trial 4 (Attempting to delete from an empty list)")
    # Attempting to delete from an empty list
    empty_list = LinkedList()
    try:
        empty_list.delete_nth_node(1)
    except ValueError as e:
        print(f"Error: {e}")