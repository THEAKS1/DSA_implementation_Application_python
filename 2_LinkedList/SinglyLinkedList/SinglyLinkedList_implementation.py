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

    # To print the list    
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next

sLlist = SinglyLinkedList()
sLlist.append("A")
sLlist.append("B")
sLlist.append("C")
sLlist.print_list()
