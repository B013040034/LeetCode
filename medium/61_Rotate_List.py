# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        tail = head
        length = 1
        while tail.next != None :
            tail = tail.next
            length += 1
        
        k = k % length
        tail.next = head
        new_head_prev = head
        for _ in range( length - k - 1 ):
            new_head_prev = new_head_prev.next
        new_head = new_head_prev.next
        new_head_prev.next = None
        return new_head
            
        
        
