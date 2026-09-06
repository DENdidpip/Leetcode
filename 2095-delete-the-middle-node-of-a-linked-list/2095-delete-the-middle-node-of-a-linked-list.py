# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n = 1
        if head.next is None:
            return None
        tmp = head
        while tmp.next:
            n += 1
            tmp = tmp.next
        n = n // 2
        tmp = head
        prev = None
        for i in range(n):
            prev = tmp
            tmp = tmp.next
        prev.next = tmp.next
        return head