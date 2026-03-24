# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tmp = ListNode(0)  
        tmp.next = head
        prev = tmp
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                rep = cur.val
                while cur and cur.val == rep:
                    cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return tmp.next