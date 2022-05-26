class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    # To append an element at the last
    def append(self, data):
        new_node = Node(data)
        
        # If list is empty
        if not self.head:
            self.head = new_node
            return
        
        # If list in not empty
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    # To prepend (insert at beginning) an element 
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # To insert element after a specific node (key)
    def afterNode(self, key, data):
        if not self.head:
            print("List is empty. Previous node not exist.")
            return
        node = self.head
        while node.data != key:
            node = node.next
            if not node:
                print("Previous node not exist.")
                return
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    # To print the list    
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next

    # To delete any node from the list by value
    def delete_node_by_val(self, key):
        node = self.head
        
        # If node is the head
        if node.data == key:
            self.head = node.next
            node.next = None
            return
            
        # If node is non head
        while node:
            if node.next.data == key:
                temp = node.next
                node.next = temp.next
                temp.next = None
                return
            node = node.next

    # To delete any node from the list by position
    def delete_node_by_pos(self, pos):
        # If given position is out of range
        if pos >= self.length() or pos < 0:
            print("Position not exist in list.")
            return

        node = self.head

        # If node is the head
        if not pos:
            self.head = node.next
            node.next = None
        
        # If node is non head
        count = 0
        while node:
            count += 1
            if count == pos:
                temp = node.next
                node.next = temp.next
                temp.next = None
                return
            node = node.next

    # Returns length of the linked list
    def length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
