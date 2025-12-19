class Node():
    def __init__(self,data):
        self.data=data 
        self.next=None

a=Node(10)
b=Node(20)
c=Node(30)

a.next=b
b.next=c

head=a

def search(head,k):
    temp=head
    p=1
    while temp.next:
        if temp.data==k:
            return p
        temp=temp.next
        p+=1
    return -1

pos=search(head,20)
if pos!=-1:
    print("Found At Position",pos)
else :
    print("Not Present")

