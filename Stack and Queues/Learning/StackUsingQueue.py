class Queue:
    def __init__(self):
        self.queue1=[]
        self.queue2=[]


    def push(self,value):
        self.queue2.append(value)
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))

        self.queue1,self.queue2=self.queue2,self.queue1
    
    def pop(self):
        if self.isEmpty():
            return "Queue UnderFlow"
        return self.queue1.pop(0)
    
    def isEmpty(self):
        return len(self.queue1)==0
    
    def peek(self):
        if self.isEmpty():
            return "Queue UnderFlow"
        return self.queue1[0]
    
    def size(self):
        return len(self.queue1)
    
q=Queue()

q.push(10)
q.push(20)

print(q.pop())