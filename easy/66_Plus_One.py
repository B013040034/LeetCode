class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        next_val = 0
        digits[-1] +=1
        for i in range(len(digits)-1, -1, -1):
            next_val = digits[i] + carry
            if next_val >= 10:
                carry = 1
                digits[i] = next_val-10
            else:
                carry = 0
                digits[i] = next_val
        if carry == 1:
            digits.insert(0, 1)
        return digits
            
        
