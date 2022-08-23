class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            sub = nums[l[i]:r[i]+1]
            sub.sort()
            print(sub)
            ari = True
            if len(sub) == 1:
                ans.append(True)
                continue
            diff = sub[1] - sub[0]
            for j in range(1, len(sub)):
                if sub[j] - sub[j-1] != diff:
                    ari = False
                    break
            ans.append(ari)
        return ans
