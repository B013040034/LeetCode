class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if stack == [] or temperatures[i] < temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack != [] and temperatures[stack[-1]] < temperatures[i]:
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return ans
