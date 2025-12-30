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
    
o=Stack()

def pretopost(s):
    operator=set("/*+-")
    for ch in reversed(s):
        if ch not in operator:
            o.push(ch)
        else:
            op1=o.pop()
            op2=o.pop()
            o.push(f"{op1}{op2}{ch}")
    return o.stack

print(pretopost(s="*+ab-cd"))

        