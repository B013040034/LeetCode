class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(len(nums)/2):
            self.swap(nums,i,len(nums)-i-1)
        for i in range(k/2):
            self.swap(nums,i,k-1-i)     
        for i in range((len(nums)-k)/2):
            self.swap(nums,i+k,len(nums)-i-1)

    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
