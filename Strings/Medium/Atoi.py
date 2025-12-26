def atoi(s: str)->int:
    i=0
    sign=0
    res=0
    n=len(s)

    while i<n:
        if s[i]=='':
            i+=1
        elif s[i]=='-':
            sign-=1
            i+=1
        elif s[i]=='+':
            i+=1
        elif s[i].isdigit():
            digit=ord(s[i])-ord('0')
            res=res*10+digit
            i+=1
        res*=sign
    return res
        
print(atoi(s="1337c0d3"))