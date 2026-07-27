class Solution(object):
    def get_len_and_times(self, head, k):
        cur = head
        length = 0

        while cur:
            length += 1
            cur = cur.next

        times = length // k
        return length, times

    def reverseKGroup(self, head, k):

        length, times = self.get_len_and_times(head, k)

        if times == 0:
            return head

        prev_group = None
        a = head

        for i in range(times):

            group_start = a
            for i in range(k - 1):

                temp = a.next
                a.next = temp.next

                if prev_group:
                    temp.next = prev_group.next
                    prev_group.next = temp
                else:
                    temp.next = head
                    head = temp
            prev_group = a
            a = a.next

        return head