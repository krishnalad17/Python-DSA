class Solution:
    def bubblesort(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    
arr = [64, 25, 12, 22, 11]
s=Solution()
print("Sorted array:", s.bubblesort(arr))