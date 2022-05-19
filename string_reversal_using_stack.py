from stack_implementation import Stack

def reverseString(s):
    stack = Stack()
    for i in s:
        stack.push(i)
    out = ""
    while not stack.isEmpty():
        out += stack.pop()
    return out

s = input()
print(reverseString(s))