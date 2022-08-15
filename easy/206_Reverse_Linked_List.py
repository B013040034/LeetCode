# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev, curr = None, head
        while head.next:
            head = head.next
            curr.next = prev
            prev = curr
            curr = head
        head.next = prev
        return head
            
            
            
