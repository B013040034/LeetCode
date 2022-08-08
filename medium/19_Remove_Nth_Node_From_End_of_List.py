# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        first = head
        second = head
        while n>0:
            second = second.next
            n -= 1
        if not second:
            return head.next
        while second.next:
            first = first.next
            second = second.next
        first.next = first.next.next
        return head
        
