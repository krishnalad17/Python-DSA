def spiral(n):
    rows=len(n)
    cols=len(n[0])
    res=[]
     
    top=0
    bottom=rows-1
    right=cols-1
    left=0
    while top<=bottom and left<=right:
         
        for i in range(left,right+1):
            res.append(n[top][i])
        top+=1

        for i in range(top,bottom+1):
            res.append(n[i][right])
        right-=1

        for i in range(right,left-1,-1):
            res.append(n[bottom][i])
        bottom-=1

        for i in range(bottom,top):
            res.append(n[i][left])
        left+=1
            
    return res
print(spiral(n=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
