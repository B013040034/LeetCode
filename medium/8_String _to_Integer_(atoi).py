class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        s = list(s)
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
        positive = True
        if s[i] == '-':
            positive = False
            i+=1
        elif s[i] == '+':
            i+=1
        elif s[i].isdigit():
            positive = True
        else:
            return 0
        start = i
        while i < len(s) and s[i].isdigit():
            i+=1
        try:
            ans = int("".join(s[start:i]))
        except Exception as e:
            return 0
        if positive and ans > 2**31 - 1:
            return 2**31 - 1
        elif not positive and ans > 2**31:
            return (2**31) * -1
        return ans if positive else ans*-1 
        
