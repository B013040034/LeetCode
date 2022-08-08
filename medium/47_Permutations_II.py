class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
          
        ans = []
        nums.sort()
        self.dfs([], nums, ans)
        return ans
    
    def dfs(self, arr, nums, ans):
        if nums == []:
            ans.append(arr)
        else:
            for i in range(len(nums)):
                if i == 0 or  nums[i] !=nums[i-1]:
                    self.dfs(arr+[nums[i]], nums[:i]+nums[i+1:], ans)
        
