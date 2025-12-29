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


def intopre(s):
    s=s[::-1]
    
    swap=""
    for ch in s:
        if ch=='(':
            swap+=')'
        elif ch==')':
            swap+='('
        else:
            swap+=ch

    res=""
    priority={'+':1,'-':1,'*':2,'/':2,'^':3}

    for ch in swap:
        if ch.isalnum():
            res+=ch

        elif ch=='(':
            o.push(ch)

        elif ch==")":
            while o.stack and o.stack[-1] != '(':
                res+=o.pop()
            o.pop()
            
        else:
            while o.stack and o.stack[-1]!='(' and priority[ch]<=priority[o.stack[-1]]:
                res+=o.pop()
            o.push(ch)

    while o.stack:
        top=o.pop()
        if top!='(':
            res+=top
    
    return res[::-1]

                

print(intopre(s="(p+q)*(m-n)"))
    


