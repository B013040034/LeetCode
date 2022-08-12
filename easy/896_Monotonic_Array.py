class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        crease = None
        if len(nums) == 1:
            return True
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if crease == None:
                crease = True if nums[i] > nums[i-1] else False
            if (crease and nums[i] < nums[i-1]) or (not crease and nums[i] > nums[i-1]):
                return False
        return True
