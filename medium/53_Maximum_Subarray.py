class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = total = nums[0]
        for num in nums[1:]:
            if total > 0:
                total += num
            else:
                total = num
            max_sum = max(total, max_sum)
        return max_sum
            
            
                
