class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums)-1:
            return 1
        reach = nums[0]
        max_dist = 0
        step = 1
        for i in range(len(nums)):
            max_dist = max(max_dist, nums[i] + i)
            if max_dist >= len(nums)-1:
                step +=1
                break
            if i == reach:
                reach = max_dist
                step +=1
        return step
