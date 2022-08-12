class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [0] * 10001
        for num in nums:
            arr[num] += num
        
        count = 0
        for i in range(2, len(arr)):
            if count == len(nums):
                return arr[i-1]
            if arr[i] != 0:
                count +=1
            arr[i] = max(arr[i-1], arr[i-2] + arr[i])
        return arr[-1]
            
            
        
