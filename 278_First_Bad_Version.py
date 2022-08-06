# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if n == 1:
            return n
        while left != right:
            mid = (left + right)/2
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid+1
            elif isBadVersion(mid):
                right = mid
            else:
                left = mid
        return left
