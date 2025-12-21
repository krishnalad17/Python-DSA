def start(n,x):
    start=0
    end=len(n)-1
    res=-1
    while start<=end:
        mid=(start+end)//2
        if n[mid]==x:
            res=mid
            end=mid-1
        elif n[mid]<x:
            start=mid+1
        else:
            end=mid-1
    return res

def last(n,x):
    start=0
    end=len(n)-1
    res=-1
    while start<=end:
        mid=(start+end)//2
        if n[mid]==x:
            res=mid
            start=mid+1
        elif n[mid]<x:
            start=mid+1
        else:
            end=mid-1
    return res

def occurence(n,x):
    f=start(n,x)
    if f==-1:
        return 0
    l=last(n,x)
    return l-f+1


n=[1,2,4,4,4,6,7]
x=4
print(occurence(n,x))