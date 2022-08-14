class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        num = [1,1]
        for i in range(2, n):
            num.append(sum(num))
            num.pop(0)
            #print(num)
        return num[-1]
        
