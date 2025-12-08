def sumofDivisor(self,N):
    ans=0
    for i in range(1,N+1):
        k=N//i
        ans+=(i*k)
    return ans
