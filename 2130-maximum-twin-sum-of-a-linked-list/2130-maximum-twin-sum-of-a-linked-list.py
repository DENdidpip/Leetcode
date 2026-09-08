class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        leng = 0
        reverse = None
        curr = head
        while curr:
            curr = curr.next
            leng += 1
        curr = head
        for i in range(leng // 2):
            curr = curr.next

        while curr:
            nxt = curr.next
            curr.next = reverse
            reverse = curr
            curr = nxt

        res = float('-inf')

        for i in range(leng // 2):
            res = max(res, head.val + reverse.val)
            head = head.next
            reverse = reverse.next

        return res