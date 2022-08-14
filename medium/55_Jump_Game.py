class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #if len(nums) == 1:
        #    return True
        reach = nums[0]
        for i in range(1, len(nums)):
            if i > reach:
                return False
            reach = max(reach, i+ nums[i])
                    
        return True
