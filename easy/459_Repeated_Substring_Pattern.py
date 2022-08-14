class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        for i in range(1, len(s)/2+1):
            find = True
            if len(s) % i != 0:
                continue
            length = len(s[:i])
            for j in range(len(s)/(i)-1):
                if s[i+j*length:j*length+i+i] != s[:i]:
                    find = False
                    break
            if find:
                return True
        return False
