class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
head=None

def insertathead(data,head):
    newnode=Node(data)
    newnode.next=head
    return newnode
    
def insertatend(data,head):
    newnode=Node(data)
    if head is None:
        return newnode
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=newnode 
    return head

def insertatposition(data,head,p):
    newnode=Node(data)
    if p==1:
        newnode.next=head
        return newnode
    
    temp=head
    count=1
    while temp is not None and count<p:
        temp=temp.next 
        count+=1
    newnode.next=temp.next 
    temp.next = newnode
    return head
    






head=insertathead(10,head)
head=insertathead(20,head)
head=insertathead(30,head)
head=insertathead(40,head)
insertatend(5,head)
insertatposition(1000,head,3)

temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("None")


