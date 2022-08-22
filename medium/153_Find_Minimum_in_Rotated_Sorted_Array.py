class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right)/2 
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
        
