# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2
        self.travel(root1, root2)
        return root1
    
    def travel(self, r1, r2):
        if not r1 and not r2:
            return 
        if not r1:
            r1 = TreeNode(0, None, None)
        r1.val = (r1.val if r1 else 0) + (r2.val if r2 else 0)
        r1.left = self.travel(r1.left if r1 else None, r2.left if r2 else None)
        r1.right = self.travel(r1.right if r1 else None, r2.right if r2 else None)
        return r1
