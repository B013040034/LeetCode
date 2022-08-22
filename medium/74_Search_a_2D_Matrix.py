class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False
        width = len(matrix[0])
        height = len(matrix)
        left = 0
        right = width * height -1
        
        while left <= right:
            mid = (left + right)/2
            num = matrix[mid/width][mid%width]
            print(num)
            if target == num:
                return True
            if target > num:
                left = mid + 1
            else:
                right = mid -1
        return False
