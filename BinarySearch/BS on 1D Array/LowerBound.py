def lowerbound(n,x):
    low=0
    high=len(n)-1
    while low<high:
        mid=(low+high)//2
        if n[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

x=9
n=[3,5,8,15,19]
print(lowerbound(n,x))