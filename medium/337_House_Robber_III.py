# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.travel(root))
        
        
    def travel(self, root):
        if root == None:
            return [0,0]
        left = self.travel(root.left)
        right = self.travel(root.right)
        ans = [0,0]
        ans[0]=root.val+left[1]+right[1]
        ans[1]=max(left[0],left[1])+max(right[0],right[1])
        print(root.val, ans)
        return ans
            
            
        
        
        
