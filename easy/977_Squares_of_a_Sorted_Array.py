class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        ans = []
        if len(nums) == 1:
            return [nums[0]**2]
        while True:
            if abs(nums[left]) > abs(nums[right]):
                ans.insert(0, nums[left]**2)
                left += 1
            elif abs(nums[left]) <= abs(nums[right]):
                ans.insert(0, nums[right]**2)
                right -= 1
            if left == right:
                ans.insert(0, nums[right]**2)
                break
        return ans
            
