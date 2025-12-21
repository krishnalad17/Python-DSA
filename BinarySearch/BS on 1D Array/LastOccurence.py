def last(n,x):
    start=0
    end=len(n)-1
    res=-1
    while start<=end:
        mid=(start+end)//2
        if n[mid]==x:
            res=mid
            start=start+1
        elif n[mid]>x:
            start=mid+1
        else:
            end=mid-1
    return res

n=[1,2,12,12,12,12,1]
x=12
print(last(n,x))