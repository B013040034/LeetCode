class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        for i in range(4):            
            for i in range(len(mat)):
                for j in range(i+1, len(mat)):
                    tmp = mat[i][j]
                    mat[i][j] = mat[j][i]
                    mat[j][i] = tmp
            for i in range(len(mat)):
                for j in range(len(mat)/2):
                    tmp = mat[i][j]
                    mat[i][j] = mat[i][len(mat)-j-1]
                    mat[i][len(mat)-j-1] = tmp
            if mat == target:
                return True
        return False
