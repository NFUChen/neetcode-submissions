# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow.next

        while (fast != slow):
            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next

        

        return True