# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        ans = head
        while list1 or list2:
            if not list1:
                head.next = list2
                break
            elif not list2:
                head.next = list1
                break
            node = ListNode()
            if list1.val > list2.val:
                node.val = list2.val
                list2 = list2.next
            else:
                node.val = list1.val
                list1 = list1.next
            head.next = node
            head = node
        return ans.next
