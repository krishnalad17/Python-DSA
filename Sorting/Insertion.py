class Solution:
    def insertionsort(self,arr):
        for i in range (len(arr)):
            key=arr[i]
            j=i
            while (j>0 and arr[j-1]>key):
                arr[j]=arr[j-1]
                j-=1
            arr[j]=key
        return arr
    
arr = [64,25,12,22,11]
s=Solution()
print("Sorted array:", s.insertionsort(arr))