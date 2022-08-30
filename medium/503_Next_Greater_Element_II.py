class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        length = len(nums)
        res = [-1] * length
        for i in range(length*2):
            num = nums[i%length]
            while stack != [] and nums[stack[0]] < num:
                res[stack[0]] = num
                stack.pop(0)
            if i < len(nums):
                stack.insert(0, i)
        return res
