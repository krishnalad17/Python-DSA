def odd(s):
    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2==1:
            return s[0:i+1]
        return ""
    
print(odd(s="5347"))