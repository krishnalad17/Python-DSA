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
            break
    else:
        return None
    slow=head
    while slow!=fast:
        slow=slow.next 
        fast=fast.next 
    return slow

def detectloopusingmap(head):
    visited=set()
    temp=head
    while temp and temp.next:
        if temp in visited:
            return temp.data
        visited.add(temp)
        temp=temp.next 
    return None


def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")

print(detectloop(head))