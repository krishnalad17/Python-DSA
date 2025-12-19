class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(10)
b=Node(20)
c=Node(30)

a.next=b
b.next=c
c.next=b
head=a

def detectloop(head):
    slow=head
    fast=head
    while fast.next and fast:
        fast=fast.next.next 
        slow=slow.next
        if fast==slow:
            count=1
            fast=fast.next 
            while slow!=fast:
                count+=1
                fast=fast.next
            return count
    return 0
            

def detectloopusingmap(head):
    visited={}
    index=0
    temp=head
    while temp :
        if temp in visited:
            return index-visited[temp]
        visited[temp]=index
        index+=1
        temp=temp.next 
    return 0

print(detectloop(head))