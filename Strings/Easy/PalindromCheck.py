def palindrom(s):
    res=s[::-1]
    if s==res:
        return True
    return False

def palindrom1(s):
    res=""
    for i in range(len(s)-1,-1,-1):
        if s[i]=="":
            continue
        res+=s[i]
    if s==res:
        return True
    return False

print(palindrom1(s="s a p"))