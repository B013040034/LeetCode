class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        h = list(haystack)
        n = list(needle)
        for i in range(len(h)-len(n)+1):
            if h[i] == n[0]:
                if h[i+1:len(n)+i] == n[1:]:
                    return i
        return -1
                    
