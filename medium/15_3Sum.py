class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        #print(nums)
        ans = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if left > i + 1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                elif right < (len(nums) - 1) and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                num = nums[left] + nums[right] + nums[i]
                if num == 0:
                    ans.append([nums[i], nums[left],  nums[right]])
                    left += 1
                    right -= 1
                elif num < 0:
                    left += 1
                else:
                    right -= 1
        return ans
