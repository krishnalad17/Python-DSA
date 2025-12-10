def longest(n,k):
    maxlength=0
    for i in range(len(n)):
        curr_sum=0
        for j in range(i,len(n)):
            curr_sum+=n[j]
            if curr_sum==k:
                maxlength=max(maxlength,j-i+1)
    return maxlength
            
print(longest(n=[6,-1,1,1,1],k=5))
                

