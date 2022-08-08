"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.arr = []
        self.travel(root, 0)
        return root
    
    def travel(self, root, layer):
        if not root:
            return
        if len(self.arr) <= layer:
            self.arr.append([root])
        else:
            self.arr[layer].append(root)
            if len(self.arr[layer]) > 1:
                self.arr[layer][-2].next = self.arr[layer][-1]
        self.travel(root.left, layer+1)
        self.travel(root.right, layer+1)
