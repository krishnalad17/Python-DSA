def findx(n,target):
    low=0
    high=len(n)-1
    while low<=high:
        mid=(low+high)//2

        if target==n[mid]:
            return mid
        elif target>n[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

def recursivefind(n,low,high,tar):
    while low<=high:
        mid=(low+high)//2
        if tar==n[mid]:
            return mid
        elif tar>n[mid]:
            return recursivefind(n,mid+1,high,tar)
        else:
            return recursivefind(n,low,mid-1,tar)
    return -1



tar=8
n=[1,2,4,5,3,4,3,5]
low=0
high=len(n)-1
print(recursivefind(n,low,high,tar))


