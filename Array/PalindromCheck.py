class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        res=""
        for i in range(len(x)-1,-1,-1):
            res += x[i]
        if res==x:
            return True
        else :
            return False
        