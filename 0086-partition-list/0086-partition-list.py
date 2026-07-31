# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        less, more = ListNode(0), ListNode(0)
        less_tail, more_tail = less, more
        tmp = head
        while tmp:
            if tmp.val < x:
                less_tail.next = tmp
                less_tail = less_tail.next
            else:
                more_tail.next = tmp
                more_tail = more_tail.next
            tmp = tmp.next
        less_tail.next = more.next
        more_tail.next = None
        return less.next
        


        