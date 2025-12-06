def mergesort(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)
    return arr


def merge(arr,low,mid,high):
    left=low
    right=mid+1
    array=[]
    while(left<=mid and right<=high):
        if arr[left] < arr[right]:
            array.append(arr[left])
            left+=1
        else:
            array.append(arr[right])
            right+=1

    while(left<=mid):
        array.append(arr[left])
        left+=1

    while(right<=high):
        array.append(arr[right])
        right+=1
    
    for i in range(len(array)):
        arr[low+i]=array[i]

arr = [64, 25, 12, 22, 11]
print("Sorted array:", mergesort(arr,0,len(arr)-1))