class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        length = max(len(a), len(b))
        carry = 0
        ans = []
        for i in range(1, length+1):
            A = int(a[-i]) if i-1 < len(a) else 0
            B = int(b[-i]) if i-1 < len(b) else 0
            ans.insert(0, str((A+B+carry) %2))
            carry = (A+B+carry) /2
        if carry == 1:
            ans.insert(0, '1')
        return "".join(ans)
            
