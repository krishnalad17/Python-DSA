def rotation(n):
    low=0
    high=len(n)-1
    while low<high:
        mid=low+high//2
        if n[mid]>n[high]:
            low=mid+1
        else:
            high=mid
    return low

n=[3,4,5,1,2]
print(rotation(n))