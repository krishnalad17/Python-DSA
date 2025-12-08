def palindrom(self,x):
    if x<0:
        return False
    s=str(x) 
    res=s[::-1]
    return res==s   