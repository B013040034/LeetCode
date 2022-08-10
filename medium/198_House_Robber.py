class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        arr = [0]*len(nums)
        arr[0] = nums[0]
        arr[1] = nums[1]
        arr[2] = nums[0] + nums[2]
        if len(nums) == 3:
            return max(arr[2], arr[1])
        for i in range(3, len(nums)):
            arr[i] = max(arr[i-2], arr[i-3]) + nums[i]
        
        return max(arr[-1], arr[-2])
