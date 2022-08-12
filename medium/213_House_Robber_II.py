class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 4:
            return max(nums)
        elif len(nums) == 4:
            return max(nums[3]+nums[1], nums[0] + nums[2])
    
        return max(self.find(nums[:-1]), self.find(nums[1:]))
    
    def find(self, nums):
        arr = [0]*len(nums)
        arr[0] = nums[0]
        arr[1] = nums[1]
        arr[2] = nums[2] + nums[0]
        for i in range(3, len(nums)):
            arr[i] = max(arr[i-2], arr[i-3]) + nums[i]
        return max(arr[-1], arr[-2])
