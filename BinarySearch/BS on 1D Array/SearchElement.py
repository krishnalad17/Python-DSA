def search(n,x):
    i=0
    while n[i]!=x:
        i+=1
    return i

def search1(n,x):
    low=0
    high=len(n)-1
    while low<=high:
        mid=low+high//2

        if n[mid]==x:
            return mid
        if n[low]<=n[mid]:
            if n[low]<=x<n[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if n[high]>=x>n[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1




x=8
n=[3,5,15,19]
print(search1(n,x))