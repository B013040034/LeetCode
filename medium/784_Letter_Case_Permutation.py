class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.recur(s, "", ans)
        return ans
    
    def recur(self, s, arr, ans):
        if len(arr) == len(s):
            ans.append(arr)
            return 
        next_s = ""
        length = len(arr)
        while s[length].isdigit() and length < len(s)-1:
            next_s += s[length]
            length += 1
        self.recur(s, arr+next_s+s[length], ans)
        if not s[length].isdigit():
            self.recur(s, arr+next_s+(s[length].swapcase()), ans)
                
