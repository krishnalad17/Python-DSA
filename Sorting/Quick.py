def quicksort(arr,low,high):
    if low<high :
        pivot=quick(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)
    return arr

def quick(arr,low,high):
    pivot=arr[low]
    i=low
    j=high

    while(i<j):
        while(arr[i]> pivot and i<=high-1):
            i+=1
        while(arr[j]< pivot and j<=low+1):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j


arr = [64, 25, 12, 22, 11]
print("Sorted array:", quicksort(arr,0,len(arr)-1))