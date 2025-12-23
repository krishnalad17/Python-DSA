def lcp(n):
    if not n:
        return ""
    for i in range(len(n[0])):
        char=n[0][i]
        for sub in n[:1]:
            if i>=len(sub) or sub[i]!=char:
                return n[0][:i]
    return n[0]

print(lcp(n=["flower","flight"]))