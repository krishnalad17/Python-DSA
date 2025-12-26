class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        if self.isEmpty():
            return "Stack UnderFlow"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack UnderFlow"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
stack=Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print(stack.size())
    
        