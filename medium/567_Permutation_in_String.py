class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import Counter
        k = len(s1)    
        c1 = Counter(s1)
        c2 = Counter(s2[0:k])
        if c1 == c2:
            return True
        for i in range(1, len(s2)-k+1):
            if c2[s2[i-1]] == 1:
                del c2[s2[i-1]]
            else:
                c2[s2[i-1]] = c2[s2[i-1]] - 1
            if c2[s2[i+k-1]] == 0:
                c2[s2[i+k-1]] = 1
            else:
                c2[s2[i+k-1]] += 1
            if c1 == c2:
                return True
        return False
                
