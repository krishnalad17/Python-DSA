def minimum(n):
    low=0
    high=len(n)-1
    m=0
    while low<=high:
        if n[low]<=n[high]:
            m=n[low]
            break
        mid=low+high//2
        if n[low]<=n[mid]:
            m=min(m,n[low])
            low=mid+1
        else:
            m=min(m,n[high])
            high=mid-1
    return m



n=[3,5,15,1,19]
print(minimum(n))