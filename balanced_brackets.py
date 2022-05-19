from stack import Stack

def isMatching(c,o):
    if (c == ")" and o == "(") or (c == "}" and o == "{") or (c == "]" and o == "["):
        return True
    return False
    
def isBalOrNot(s):
    stack = Stack()
    for i in s:
        if i in "({[":
            stack.push(i)
        elif i in ")}]":
            if stack.isEmpty():
                print("Not balanced brackets.")
                return
            e = stack.pop()
            if not isMatching(i,e):
                print("Not balanced brackets.")
                return
    if stack.isEmpty():
        print("Balanced brackets.")
        return
    print("Not balanced brackets.")
    return
    
s = input()
isBalOrNot(s)