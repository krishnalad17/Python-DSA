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
            return True
    return False

def detectloopusingmap(head):
    visited={}
    temp=head
    while temp and temp.next:
        if temp in visited:
            return True
        visited[temp]=True
        temp=temp.next 
    return False




def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")

print(detectloopusingmap(head))