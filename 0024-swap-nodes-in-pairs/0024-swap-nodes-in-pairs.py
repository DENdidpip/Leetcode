class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)        # 0
        dummy.next = head          # 0 → A - B - C
        prev = dummy               

        while prev.next and prev.next.next: 
            first = prev.next                # A - B - C
            second = prev.next.next          # B - C

            first.next = second.next         # A → C
            second.next = first              # B → A
            prev.next = second               # prev → B

            prev = first                    

        return dummy.next                  