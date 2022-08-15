# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        return self.travel(root, head)
        
    def travel(self, root, head):
        if not root:
            return False
        if self.check(root, head):
            return True
        else:
            return self.travel(root.left, head) or self.travel(root.right, head)
        
    def check(self,  root, head):
        if not head:
            return True
        if not root:
            return False
        if head.val != root.val:
            return False
        return self.check(root.left, head.next) or self.check(root.right, head.next)
        
