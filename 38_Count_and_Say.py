class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.recur(n, "1")
                
    def recur(self, n, s):
        if n==1:
            return s
        res, i = "", 0
        num, count = s[i], 0
        while i < len(s)+1:
            if i<len(s) and s[i]!=num:
                res+=str(count)
                res+=str(num)
                num = s[i]
                count = 1
            elif i==len(s):
                res+=str(count)
                res+=str(s[-1])
            else:
                count+=1
            i+=1
        return self.recur(n-1, res)
