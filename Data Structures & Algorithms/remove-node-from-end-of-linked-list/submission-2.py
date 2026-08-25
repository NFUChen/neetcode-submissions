class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next
        
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next