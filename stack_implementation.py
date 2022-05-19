# Class for implementing stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)
    
    def isEmpty(self):
        return self.items == []
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def sizeOf(self):
        return len(self.items)

    def get_stack(self):
        return self.items
