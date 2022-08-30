class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s = list(s)
        p = list(p)
        n = len(p)
        if n > len(s):
            return []
        s_m = {}
        p_m = {}
        res = []
        for i in range(len(p)):
            if p[i] in p_m.keys():
                p_m[p[i]] += 1
            else:
                p_m[p[i]] = 1
            if s[i] in s_m.keys():
                s_m[s[i]] += 1
            else:
                s_m[s[i]] = 1
        for i in range(n, len(s)):
            if s_m == p_m:
                res.append(i-n)
            if s_m[s[i-n]] == 1:
                s_m.pop(s[i-n], None)
            else:
                s_m[s[i-n]] -= 1
            if s[i] in s_m.keys():
                s_m[s[i]] += 1
            else:
                s_m[s[i]] = 1
        if s_m == p_m:
            res.append(len(s)-n)
        return res
            
                
            
