# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.is_bal = True
        if root != None:
            self.travel(root)
        return self.is_bal
        
    def travel(self, root):
        if root == None:
            return 0
        left = self.travel(root.left)
        right = self.travel(root.right)
        if abs(left-right) > 1:
            self.is_bal = False
        return max(left, right) + 1
