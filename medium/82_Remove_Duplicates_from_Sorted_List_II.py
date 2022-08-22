# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        h = head
        prev = ListNode()
        prev.next = head
        while h != None:
            find = False
            while h.next != None and h.next.val == h.val:
                h.next = h.next.next
                find = True
            if find:
                if head == prev.next:
                    head = h.next
                prev.next = h.next
                 
            else:
                prev = h
            h = h.next
        return head
        
