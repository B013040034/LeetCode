class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs([], nums, ans)
        return ans
    
    def dfs(self, arr, nums, ans):
        if nums == []:
            ans.append(arr)
        else:
            for i in range(len(nums)):
                self.dfs(arr+[nums[i]], nums[:i]+nums[i+1:], ans)
        
