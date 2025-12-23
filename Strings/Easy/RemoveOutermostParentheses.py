def remove(s):
    res=""
    level=0
    for i in s:
        if i=='(':
            level+=1
            if level>1:
                res+='('
        if i==')':
            if level>1:
                res+=')'
            level-=1
    return res

print(remove(s="(()())(())"))