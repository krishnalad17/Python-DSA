def armstrongnum(self,n):
    n=str(n)
    temp=0
    for i in n:
        temp+=int(i)^3
    return temp==n 
    
        
