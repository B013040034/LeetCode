class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.recur(n,k,[],ans)
        return ans
        
    def recur(self, n, k, arr, ans):
        length = len(arr)
        if length == k:
            ans.append(arr)
            return
        start = 1 if length == 0 else arr[-1] +1     
        for i in range(start, n+2-k+length):
            self.recur(n,k, arr+[i],ans)
