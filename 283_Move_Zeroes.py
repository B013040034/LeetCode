class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count +=1
            elif count == 0:
                continue
            else:
                nums[i-count]=nums[i]
        for i in range(len(nums)-count, len(nums)):
            nums[i] = 0
