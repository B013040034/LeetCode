class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 1
        if s == "":
            return 0
        for i in range(len(s)):
            j = i
            curr = []
            while j < len(s) and s[j] not in curr:
                curr.append(s[j])
                j +=1
            if j == len(s):
                return max(ans, len(curr))
            ans = max(ans, len(curr))
        return max(ans, len(curr))
        
