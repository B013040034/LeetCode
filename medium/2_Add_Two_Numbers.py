# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        tail = head
        while l1 != None or l2 != None or carry != 0:
            add = l1.val if l1 else 0
            add += l2.val if l2 else 0
            add += carry
            newans = ListNode(add%10)
            carry=add/10
            tail.next = newans
            tail = newans 

            l1 = l1 if l1 == None else l1.next
            l2 = l2 if l2 == None else l2.next
        return  head.next;
        
