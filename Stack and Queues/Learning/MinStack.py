class Stack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self,value):
        self.stack.append(value)
        if not self.minstack or value<= self.minstack[-1]:
            self.minstack.append(value)
    
    def getmin(self):
        return self.minstack[-1]
    
    def top(self):
        return self.stack[-1]
    
    def pop(self):
        val=self.stack.pop()
        if val==self.minstack[-1]:
            return self.minstack.pop()
        

class Stackopt:
    def __init__(self):
        self.stack=[]
        self.curmin=None
    
    def pushpa(self,value):
        
        if not self.stack:
            self.stack.append(value)
            self.curmin=value

        elif value>=self.curmin:
            self.stack.append(value)
        
        else:
            encoded=2*value-self.curmin
            self.stack.append(encoded)
            self.curmin=value

    def getmin(self):
            if not self.stack:
                return -1
            return self.curmin
    
    def pop(self):
        if not self.stack:
            return
        top=self.stack.pop()
        
        if top<self.curmin:
            self.curmin=2*self.curmin-top
        
    def top(self):
        if not self.stack:
            return
        top=self.stack[-1]

        if top<self.curmin:
            return self.curmin
        return top
    
o=Stackopt()
o.pushpa(5)
o.pushpa(3)
o.pushpa(7)
o.pushpa(2)

print(o.stack)


