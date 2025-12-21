def Floor(n,x):
    low=0
    high=len(n)-1
    while low<=high:
        mid=(low+high)//2
        if n[mid]<=x:
            floor=n[mid]
            low=mid+1
        else:
            high=mid-1
    return floor

def ceil(n,x):
    low=0
    high=len(n)-1
    while low<=high:
        mid=(low+high)//2
        if n[mid]>=x:
            ceil=n[mid]
            high=mid-1
        else:
            low=mid+1
    return ceil

x=9
n=[3,5,8,15,19]
print(Floor(n,x),ceil(n,x))
