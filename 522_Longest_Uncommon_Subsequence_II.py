class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs = sorted(strs, key=len, reverse=True)
        res = -1
        for i in range(len(strs)):
            find = False
            for j in range(0, len(strs)):
                if j == i:
                    continue
                if self.findsub(strs[i], strs[j]):
                    find = True
                    break
            if find == False:
                return len(strs[i])                    
        return -1
        
    
    def findsub(self, a, b):
        #check a in b
        if len(a) > len(b):
            return False
        j=0
        for i in b:
            if i == a[j]:
                j+=1
            if j == len(a):
                #print(a, b, "True")
                return True
        #print(a, b, "False")
        return False
        
